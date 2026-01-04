import pandas as pd
from src.data.dataset import Dataset

class CSVDataSet(Dataset):
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        df = pd.read_csv(self.file_path)

        X = df.iloc[:, :-1].values
        y = df.iloc[:, -1].values

        return X, y