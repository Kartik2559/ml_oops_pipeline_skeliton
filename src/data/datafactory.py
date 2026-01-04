from src.data.api_dataset import APIDataset
from src.data.excel_dataset import ExcelDataset
from src.data.csv_datatset import CSVDataSet

class DataFactory:
    @staticmethod
    def create_dataset(file_path):
        if file_path.endswith(".csv"):
            return CSVDataSet(file_path)
        elif file_path.endswith(".xlsx"):
            return ExcelDataset(file_path)
        elif file_path.startswith("http"):
            return APIDataset(file_path)
        else: 
            raise ValueError("Unsopported data source")