# file_io.py
import os
import base64

def encode_file(path):
    """Read a file from disk and return its base64-encoded contents.
    Args:
        path: Filesystem path to the file to encode.
    Returns:
        A UTF-8 string containing the base64-encoded file bytes.
    Assumptions:
        The file exists and is readable.
    """
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def list_files(dirpath):
    """Yield filenames and paths for regular files in a directory.
    Args:
        dirpath: Path to the directory to scan.
    Returns:
        An iterator of (name, path) tuples for files in the directory.
    Assumptions:
        The directory exists and is readable.
    """
    for name in os.listdir(dirpath):
        path = os.path.join(dirpath, name)
        if os.path.isfile(path):
            yield name, path
