import argparse
import sys


parser = argparse.ArgumentParser(description="Program to OCR PNG with SRT export from Subtitle Edit")
parser.add_argument("--version", action="store_true", help="Print version and exit")
args = parser.parse_args()


if args.version:
    print("Vob2Srt version 1.0.0")
    sys.exit(0)

parser.add_argument("-i", "--input-folder", type=str, required=True, help="Input folder path for PNG")
parser.add_argument("-o", "--output-sub", type=str, required=True, help="Output location file for subtitle (e.g., Temp.srt)")
parser.add_argument("-l", "--language", type=str, default=None, help="Language to help OCR process")
parser.add_argument("-k", "--key", type=str, required=True, help="API key for Google Cloud Vision API")
parser.add_argument("-s", "--sub", type=str, required=True, help="Blank SRT subtitle file")



args = parser.parse_args()


input_folder = args.input_folder
output_sub = args.output_sub
lang = args.language
key = args.key
sub_file = args.sub
