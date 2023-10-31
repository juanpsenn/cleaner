import csv

from core.models import Catalog

from .base import FileAdapter

class CsvFileAdapter(FileAdapter):
    def extract_data(self, file_path: str) -> Catalog:
        try:
            with open(file_path, "r", newline="", encoding="utf-8") as csvfile:
                reader = csv.reader(csvfile)
                data = [row for row in reader]
                filename = csvfile.name
                return Catalog(filename=filename, data=data)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error reading CSV: {str(e)}")
