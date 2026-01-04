class Trainer:
    def __init__(self, dataset, preprocessor, model, evaluator, logger):
        self.dataset = dataset
        self.prprocessor = preprocessor
        self.model = model
        self.evaluator = evaluator
        self.logger = logger


    def run(self):
        self.logger.info('Loading Data')
        X, y = self.dataset.load()

        self.logger.info('Preprocessing data')
        X, y = self.prprocessor.transform(X, y)

        self.logger.info("Starting training")
        self.model.train(X, y)

        self.logger.info('Training Complete')
        predictions = self.model.predict(X)

        self.logger.info("Evaluating model")
        accuracy = self.evaluator.evaluate(y, predictions)

        self.logger.info(f"Accuracy: {accuracy}")