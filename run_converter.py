# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from converter.core import CsvJsonConverter

def main():
    parser = argparse.ArgumentParser(description="CSV <-> JSON Converter")
    parser.add_argument("file", help="Input file path")
    parser.add_argument("--to_csv", action="store_true", help="Convert JSON to CSV (Default is CSV to JSON)")
    parser.add_argument("--output", "-o", help="Output file path (prints to stdout if omitted)")
    parser.add_argument("--delimiter", "-d", default=",", help="CSV delimiter (default: ,)")

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: File '{args.file}' not found.")
        sys.exit(1)

    content = ""
    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    result = ""
    if args.to_csv:
        result = CsvJsonConverter.json_to_csv(content, delimiter=args.delimiter)
    else:
        result = CsvJsonConverter.csv_to_json(content, delimiter=args.delimiter)

    if result.startswith("Error"):
        print(result)
        sys.exit(1)

    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(result)
            print(f"Converted file saved to {args.output}")
        except Exception as e:
            print(f"Error writing output: {e}")
            sys.exit(1)
    else:
        print(result)

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
