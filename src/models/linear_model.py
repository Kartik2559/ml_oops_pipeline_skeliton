from src.models.base_model import BaseModel

class LinearModel(BaseModel):
    def __init__(self, logger):
        self.logger = logger
        self.weight = 0

    def train(self, X, y):
        self.logger.info('Training Linear model')
        self.weight = sum(y)/sum(X)

    def predict(self, X):
        return [self.weight * x for x in X]
    
    