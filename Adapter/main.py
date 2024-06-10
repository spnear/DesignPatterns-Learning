from adapters import CSV2JSONAdapter, JSON2CSVAdapter
from data_handler import JSONDataHandler, CSVDataHandler


def load_and_display_data(data_handler, filepath):
    data = data_handler.load_data(filepath)
    print(data)


if __name__ == '__main__':
    json_handler = JSONDataHandler()
    json_filepath = 'data/sample_data.json'
    load_and_display_data(json_handler, json_filepath)


    csv_handler = CSVDataHandler()
    csv_filepath = 'data/sample_data.csv'
    csv_adapter = CSV2JSONAdapter(csv_handler)
    load_and_display_data(csv_adapter, csv_filepath)
