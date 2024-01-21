import csv
import re

import pandas as pd
f = open('SKU1.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=['Part_Number'])
csv_writer.writeheader()
# Read data from the Excel file
df = pd.read_excel("input_file.xlsx")

urls = df['ln']

for sku in urls:
    match = re.search(r"starter-(.*)", sku)

    # If a match is found, print the extracted data
    if match:
        extracted_data = match.group(1)
        dit = {
            'Part_Number':extracted_data
        }
        csv_writer.writerow(dit)
        print(extracted_data)
    else:
        print("No data found after 'starter-'")