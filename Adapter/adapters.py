from data_handler import JSONDataHandler, CSVDataHandler
import csv


class CSV2JSONAdapter:
    def __init__(self, csv_handler: CSVDataHandler) -> None:
        self.csv_handler = csv_handler


    def load_data(self, filepath):
        csv_data = self.csv_handler.load_data(filepath)
        return [dict(row) for row in csv_data]
    

class JSON2CSVAdapter:


    def __init__(self, json_handler: JSONDataHandler) -> None:
        self.json_handler = json_handler


    def load_data(self, filepath):
        csv_data = self.json_handler.load_data(filepath)
        csv_header = csv_data[0].keys()
        
        with open('output_data/output.csv',mode='w',encoding='utf8',newline='') as output_to_csv:
            dict_csv_writer = csv.DictWriter(output_to_csv, fieldnames=csv_header,dialect='excel')
            dict_csv_writer.writeheader()
            dict_csv_writer.writerows(csv_data)
