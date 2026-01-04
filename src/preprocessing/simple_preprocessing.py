import numpy as np
from src.preprocessing.base_preprocessing import BasePreprocessing

class SimplePreprocessing(BasePreprocessing):
    def transform(self, X, y):
        X = np.array(X)
        y = np.array(y)


        X = X/X.max()

        return X, y