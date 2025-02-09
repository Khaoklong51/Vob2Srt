import os
import re
import argument  # Custom argument module
import request  # Custom OCR module
import shutil
from tqdm import tqdm  # Progress bar
import sys

if not os.path.exists(argument.input_folder):
    print(f"{argument.input_folder} does not exist")
    sys.exit(1)

origin_extension = (".png",)

# Get list of images in input folder
files = sorted([f for f in os.listdir(argument.input_folder)
     if os.path.isfile(os.path.join(argument.input_folder, f)) 
     and f.endswith(origin_extension)])

# Ensure output directory exists
output_dir = os.path.abspath(os.path.dirname(argument.output_sub))
os.makedirs(output_dir, exist_ok=True)

# Remove existing output file if present
if os.path.exists(argument.output_sub):  
    os.remove(argument.output_sub)

def ocr_image():
    """Perform OCR on images and write subtitles immediately with a progress bar"""
    text_idx = 0  # Track which image we're processing

    # Read input SRT and write output SRT at the same time
    with open(argument.sub_file, "r", encoding="utf-8") as infile:
         

        with tqdm(total=len(files), desc="Processing Images", unit="img") as pbar:
            for id ,line in enumerate(infile):
                with open(argument.output_sub, "a", encoding="utf-8") as outfile:
                    if re.match(r"^\d+$", line.strip()) or "-->" in line or id == 0:
                        outfile.write(line)  # Keep index and timestamp lines unchanged
                    elif line.strip() and (id % 2 == 0):
                        outfile.write("\n")
                    if line.strip() and (id % 2 != 0):
                        # Perform OCR for each image immediately
                        if text_idx < len(files):
                            img_path = os.path.join(argument.input_folder, files[text_idx])

                            if not os.path.exists(img_path):
                                print(f"File {files[text_idx]} is missing. Skipping...")
                                outfile.write("[Missing Image]\n")
                            else:
                                text = request.request_text(img_path).strip()
                                outfile.write(f"{text}\n\n")

                            text_idx += 1
                            pbar.update(1)  # Update progress bar
                        else:
                            outfile.write("\n")  # Preserve format if no more images left

ocr_image()
