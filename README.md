# CSV <-> JSON Converter

A bidirectional converter tool for CSV and JSON files. Easily transform data exports for use in APIs or spreadsheets.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **CSV to JSON**: Converts rows to a list of JSON objects.
*   **JSON to CSV**: Flattens a list of JSON objects back into a CSV table.
*   **Zero Dependencies**: Uses Python's standard `csv` and `json` libraries.

## Usage

```bash
python run_converter.py [file] [options]
```

### Options

*   `--to_csv`: Switch mode to convert JSON input to CSV output.
*   `--output`, `-o`: Save the result to a file.
*   `--delimiter`, `-d`: Specify a custom delimiter (e.g., `;` or `\t`).

### Examples

**1. CSV to JSON**
```bash
python run_converter.py data.csv
```

**2. CSV to JSON (Save to file)**
```bash
python run_converter.py data.csv -o data.json
```

**3. JSON to CSV**
```bash
python run_converter.py data.json --to_csv -o export.csv
```

## Requirements

*   Python 3.x

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel-anunzio/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
