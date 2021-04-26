import pandas as pd
import argparse
import os
import sys


def create_parser() -> argparse.ArgumentParser:
    '''
    Creates command line argument parser
    '''
    parser = argparse.ArgumentParser(description='Convert a CSV file to JSON')
    parser.add_argument('Path', metavar='path', type=str,
                        help='The path of the CSV file to convert')
    parser.add_argument('OutDirectory', metavar='outdir', type=str,
                        help='The path of the directory to save the JSON file')
    return parser


def csv_to_json(file_path: str, out_directory: str) -> int:
    '''
    Opens a csv file, converts it to JSON, and  downloads it to the specified output directory
    '''
    try:
        os.path.abspath("%s" % out_directory)
        file_name = file_path.split('.')[0]
        df = pd.read_csv(file_path)
        df.to_json(path_or_buf="%s.json" %
                   (file_name), orient="records")
    except Exception as e:
        print('Could not transform CSV file to JSON. Please ensure file is in the correct format')
        print(e)
        sys.exit()


def main():
    parser = create_parser()
    args = parser.parse_args()

    file_path = args.Path
    out_directory = args.OutDirectory

    if not os.path.isfile(file_path):
        print('The path specified does not exist.')
        sys.exit()
    if not os.path.isdir(out_directory):
        print('The specified output directory does not exist')
        sys.exit()

    else:
        csv_to_json(file_path=file_path, out_directory=out_directory)


if __name__ == "__main__":
    main()
