import requests
import pandas as pd
from src.data.dataset import Dataset

class APIDataset:
    def __init__(self, url):
        self.url = url

    def load(self):
        response = requests.get(self.url)
        data = response.json()

        df = pd.DataFrame(data)

        X = df.iloc[:,:-1].values
        y = df.iloc[:, -1].values


        return X, y