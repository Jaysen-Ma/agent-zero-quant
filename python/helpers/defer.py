import asyncio  # For asynchronous programming
import threading  # For multi-threading support
from concurrent.futures import Future  # For representing the eventual result of an asynchronous computation

class DeferredTask:
    def __init__(self, func, *args, **kwargs):
        self._loop = asyncio.new_event_loop()  # Create a new event loop for this task
        self._task = None  # Will hold the asyncio task
        self._future = Future()  # Will hold the result of the task
        self._task_initialized = threading.Event()  # Event to signal when the task is initialized
        self._start_task(func, *args, **kwargs)  # Start the task

    def _start_task(self, func, *args, **kwargs):
        def run_in_thread(loop, func, args, kwargs):
            asyncio.set_event_loop(loop)  # Set the event loop for this thread
            self._task = loop.create_task(self._run(func, *args, **kwargs))  # Create the task
            self._task_initialized.set()  # Signal that the task has been initialized
            loop.run_forever()  # Run the event loop

        # Create and start a new thread for this task
        self._thread = threading.Thread(target=run_in_thread, args=(self._loop, func, args, kwargs))
        self._thread.start()

    async def _run(self, func, *args, **kwargs):
        try:
            result = await func(*args, **kwargs)  # Run the provided function
            self._future.set_result(result)  # Set the result in the future
        except Exception as e:
            self._future.set_exception(e)  # Set any exception in the future
        finally:
            self._loop.call_soon_threadsafe(self._loop.stop)  # Stop the event loop

    def is_ready(self):
        return self._future.done()  # Check if the task has completed

    async def result(self, timeout=None):
        # Wait until the task is initialized
        if not self._task_initialized.wait(timeout):
            raise RuntimeError("Task was not initialized properly.")

        try:
            # Wait for the result with a timeout
            return await asyncio.wait_for(asyncio.wrap_future(self._future), timeout)
        except asyncio.TimeoutError:
            raise TimeoutError("The task did not complete within the specified timeout.")

    def result_sync(self, timeout=None):
        # Wait until the task is initialized
        if not self._task_initialized.wait(timeout):
            raise RuntimeError("Task was not initialized properly.")
        
        try:
            return self._future.result(timeout)  # Get the result synchronously
        except TimeoutError:
            raise TimeoutError("The task did not complete within the specified timeout.")

    def kill(self):
        # Cancel the task if it's still running
        if self._task and not self._task.done():
            self._loop.call_soon_threadsafe(self._task.cancel)

    def is_alive(self):
        # Check if the thread is alive and the task is not done
        return self._thread.is_alive() and not self._future.done()

    def __del__(self):
        # Cleanup method called when the object is about to be destroyed
        if self._loop.is_running():
            self._loop.call_soon_threadsafe(self._loop.stop)  # Stop the event loop
        if self._thread.is_alive():
            self._thread.join()  # Wait for the thread to finish
        self._loop.close()  # Close the event loop