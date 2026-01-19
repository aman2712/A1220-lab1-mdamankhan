# main.py
import json
import argparse
from . import file_io as io_mod
from . import gpt

def process_directory(dirpath):
    """Process receipt images in a directory and extract structured data.
    Args:
        dirpath: Path to a directory containing receipt image files.
    Returns:
        A dict mapping each filename to extracted receipt data.
    Assumptions:
        The directory exists and contains readable files supported by the
        extraction pipeline.
    """
    results = {}
    for name, path in io_mod.list_files(dirpath):
        image_b64 = io_mod.encode_file(path)
        data = gpt.extract_receipt_info(image_b64)
        results[name] = data
    return results

def main():
    """Run the CLI to extract receipt data and print JSON output.

    Args:
        None. CLI arguments are parsed from sys.argv.

    Returns:
        None. Prints JSON to stdout when data is available.

    Assumptions:
        The provided directory path is valid and readable.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("dirpath")
    parser.add_argument("--print", action="store_true")
    args = parser.parse_args()

    data = process_directory(args.dirpath)
    if data:
        print(json.dumps(data, indent=2))

if __name__ == "__main__":
    main()
