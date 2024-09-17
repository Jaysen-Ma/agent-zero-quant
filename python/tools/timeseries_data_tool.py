from python.helpers.tool import Tool, Response
import arcticdb

class TimeSeriesData(Tool):
    async def execute(self, **kwargs):
        action = kwargs.get('action', '')
        symbol = kwargs.get('symbol', '')
        start_date = kwargs.get('start_date', '')
        end_date = kwargs.get('end_date', '')

        try:
            store = arcticdb.Arctic('/data/TimeSeriesDB')
            library = store['market_data']

            if action == 'list_symbols':
                symbols = library.list_symbols()
                return Response(message=f"Available symbols: {', '.join(symbols)}", break_loop=False)

            elif action == 'get_data':
                if not symbol:
                    return Response(message="Error: Symbol is required for get_data action", break_loop=False)

                data = library.read(symbol, date_range=(start_date, end_date))
                return Response(message=f"Data for {symbol} retrieved successfully. Shape: {data.shape}", break_loop=False)

            else:
                return Response(message="Error: Invalid action. Use 'list_symbols' or 'get_data'.", break_loop=False)

        except Exception as e:
            return Response(message=f"Error: {str(e)}", break_loop=False)