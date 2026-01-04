from src.data.dataset import Dataset

class SimpleDataset(Dataset):
    def load(self):
        X = [1,2,3,4,5]
        Y = [2,3,4,5,6]
        return X, Y
    

dataset = SimpleDataset()

X, y = dataset.load()