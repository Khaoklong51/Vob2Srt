# Vob2Srt
program to ocr text using google cloud vision ai api\
Using image extract from SubtitleEdit using BDN xml/png option\
Using blank Srt file save from SubtitleEdit

## options
```
usage: main.py [-h] [-i INPUT_FOLDER] [-o OUTPUT_SUB] [-l LANGUAGE] [-k KEY] [-s SUB] [--version]

Program to OCR PNG with SRT export from Subtitle Edit

options:
  -h, --help            show this help message and exit
  -i INPUT_FOLDER, --input-folder INPUT_FOLDER
                        Input folder path for PNG
  -o OUTPUT_SUB, --output-sub OUTPUT_SUB
                        Output location file for subtitle (e.g., Temp.srt)
  -l LANGUAGE, --language LANGUAGE
                        Language to help OCR process
  -k KEY, --key KEY     API key for Google Cloud Vision API
  -s SUB, --sub SUB     Blank SRT subtitle file
  --version             Print version and exit

```
