import argparse
import os
import sys


parser = argparse.ArgumentParser(description="Program to ocr png with xml export from subtitle edit")
parser.add_argument("-i", "--input-folder", type=str, required=True, help="input folder path for png")
parser.add_argument("-o", "--output-sub",type=str, required=True, help="output location file for sub ex. Temp.srt")
parser.add_argument("-l", "--language", type=str, default=None, help="language parse to help ocr process")
parser.add_argument("-k", "--key", type=str, required=True ,help="apikey for google clound vision ai api")
parser.add_argument("-s", "--sub", type=str,  required=True ,help="blank srt subtitle file")


args = parser.parse_args()


input_folder = args.input_folder
output_sub = args.output_sub
lang = args.language
key = args.key
sub_file = args.sub
