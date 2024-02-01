import csv
import re

def markdown_to_csv(markdown_text, csv_filename):
    # Split the input text into lines
    lines = markdown_text.strip().split('\n')

    # Prepare a list to hold all rows
    rows = []

    for line in lines:
        # Remove leading and trailing '|', then split by '|'
        columns = line.strip('|').split('|')

        # Strip whitespace and remove Markdown links
        processed_columns = [re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', col.strip()) for col in columns]

        # Append processed columns to rows
        rows.append(processed_columns)

    # Write to CSV
    with open(csv_filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# Example Markdown table
markdown_table = """
| TestDataHeader | TestIDHeader | TestAccountHeader |
| ---- | ---- | ---- |
| TestData | [LinkTitle](https://link.to/somewhere) | TestData |
"""

# Convert to CSV
markdown_to_csv(markdown_table, 'output.csv')
