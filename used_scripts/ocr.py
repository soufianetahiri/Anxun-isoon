import os
import json
from PIL import Image
import pytesseract

def ocr_to_json(input_directory, output_file, language='chi_sim'):
    data = [] 

    if not os.path.exists(input_directory):
        print(f"The directory {input_directory} does not exist.")
        return
    else:
        print(f"Processing images in directory: {input_directory}")

    for filename in os.listdir(input_directory):
        if filename.endswith(".png"):
            file_path = os.path.join(input_directory, filename)
            print(f"Processing file: {filename}")
            try:
                img = Image.open(file_path)
                print(f"Extracting text from {filename} using Tesseract OCR with language '{language}'")
                text = pytesseract.image_to_string(img, lang=language)
                # Append a new dictionary for each file
                data.append({"file": filename, "content": text.strip()})
                print(f"Text extraction complete for {filename}.")
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

    print(f"Writing OCR results to {output_file}")
    with open(output_file, 'w') as outfile:
        json.dump(data, outfile, indent=4, ensure_ascii=False)
        print(f"OCR results have been successfully written to {output_file}")

# use
input_directory = '/home/soufiane/Desktop/anxun_leak/I-S00N/0'
output_file = 'ocr_output.json'
ocr_to_json(input_directory, output_file)
