# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import csv
import json
import io

class CsvJsonConverter:
    @staticmethod
    def csv_to_json(csv_content, delimiter=","):
        try:
            # Use StringIO so csv module can read it like a file
            f = io.StringIO(csv_content)
            reader = csv.DictReader(f, delimiter=delimiter)
            
            rows = list(reader)
            return json.dumps(rows, indent=4)
        except Exception as e:
            return f"Error converting CSV: {e}"

    @staticmethod
    def json_to_csv(json_content, delimiter=","):
        try:
            data = json.loads(json_content)
            if not isinstance(data, list):
                # Attempt to handle if root is not list (e.g. wrapper obj), but standard assumption is list of dicts
                return "Error: JSON root must be a list of objects for CSV conversion."
            
            if not data:
                return "" # Empty

            # Get headers from all keys in all objects (to handle sparse data)
            headers = set()
            for item in data:
                if isinstance(item, dict):
                    headers.update(item.keys())
            
            headers = sorted(list(headers))
            
            output = io.StringIO()
            writer = csv.DictWriter(output, fieldnames=headers, delimiter=delimiter)
            writer.writeheader()
            writer.writerows(data)
            
            return output.getvalue()

        except json.JSONDecodeError as e:
            return f"Error: Invalid JSON - {e}"
        except Exception as e:
            return f"Error converting JSON to CSV: {e}"

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
