import os, re, sys

def read_file(relative_path, **kwargs):
    absolute_path = get_abs_path(relative_path)  # Construct the absolute path to the target file

    with open(absolute_path) as f:
        content = remove_code_fences(f.read())

    # Replace placeholders with values from kwargs
    for key, value in kwargs.items():
        placeholder = "{{" + key + "}}"
        strval = str(value)
        # strval = strval.encode('unicode_escape').decode('utf-8')
        # content = re.sub(re.escape(placeholder), strval, content)
        content = content.replace(placeholder, strval)

    return content

def remove_code_fences(text):
    """
    Removes code fence markers from the given text.

    This function uses a regular expression to remove code fence markers
    (triple tildes '~~~') from the input text. It handles both opening
    fences (which may include a language specifier) and closing fences.

    Args:
        text (str): The input text containing code fences.

    Returns:
        str: The input text with all code fence markers removed.

    Example:
        Input:  "Some text\n~~~python\nprint('Hello')\n~~~\nMore text"
        Output: "Some text\nprint('Hello')\nMore text"
    """
    return re.sub(r'~~~\w*\n|~~~', '', text)

def get_abs_path(*relative_paths):
    return os.path.join(get_base_dir(), *relative_paths)

def exists(*relative_paths):
    path = get_abs_path(*relative_paths)
    return os.path.exists(path)


def get_base_dir():
    # Get the base directory from the current file path
    base_dir = os.path.dirname(os.path.abspath(os.path.join(__file__,"../../")))
    return base_dir

# This function will return the absolute path of the project's root directory.
# Specifically:
# 1. It starts from the current file's location (__file__)
# 2. It goes up two directory levels ("../../")
# 3. It then gets the absolute path of this location
# 4. Finally, it returns the directory name of this absolute path

# For example, if this file is located at:
# /home/user/project/python/helpers/files.py
# The function will return:
# /home/user/project