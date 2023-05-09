import csv
import os
import chardet

folder_path = "nounbanks"

for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        with open(os.path.join(folder_path, filename), 'rb') as f:
            result = chardet.detect(f.read())
        with open(os.path.join(folder_path, filename), 'r', encoding=result['encoding']) as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                for field in row:
                    if field.endswith(" "):
                        print(f"Trailing space found in file {filename}, field: {field}")