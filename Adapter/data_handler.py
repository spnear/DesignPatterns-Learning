import json
import csv


class JSONDataHandler:
    def load_data(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
        

class CSVDataHandler:
    def load_data(self, file_path):
        with open(file_path, newline='') as file:
            return list(csv.DictReader(file))