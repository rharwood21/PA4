"""
Author: Riley Harwood
Last Edit: 10 October 2023
The main file is what will be run from the terminal. Argparse, paths, and file IO are used
together to open the input and output files. The 'with' function in python allows
the user and programmer not to worry so much about closing files.
"""
import sys
from pathlib import Path
import argparse
from PA4 import process_files

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("in_file", type=str, help="Input File Pathname")
arg_parser.add_argument("out_file", type=str, help="Output File Pathname")
args = arg_parser.parse_args()

in_path = Path(args.in_file)
out_path = Path(args.out_file)


try:
    with in_path.open('r') as input_file, out_path.open('w') as output_file:
        process_files(input_file, output_file)
except IOError:
    print("Please check validity of input and output paths given.")
