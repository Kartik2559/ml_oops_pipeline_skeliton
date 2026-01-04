import numpy as np

class Evaluator:
    def evaluate(self, y_true, y_pred):
        y_true = np.array(y_true)
        y_pred = np.array(y_pred)

        accuracy = (y_true == y_pred).mean()
        return accuracy