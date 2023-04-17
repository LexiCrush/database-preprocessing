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
            rows = []
            for row in csvreader:
                new_row = [field.rstrip() for field in row]
                rows.append(new_row)
        with open(os.path.join(folder_path, filename), 'w', newline='', encoding=result['encoding']) as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(rows)
            print(f"Trailing spaces removed from file {filename}")