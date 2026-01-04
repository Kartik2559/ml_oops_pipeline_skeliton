from src.Logging.logger import AppLogger
from src.preprocessing.simple_preprocessing import SimplePreprocessing
from src.models.linear_model import LinearModel
from src.evaluation.evaluator import Evaluator
from src.training.trainer import Trainer
from src.data.datafactory import DataFactory



def main():
    logger = AppLogger("ML_pipeline")


    data_source = "data/train_data.csv"
    dataset = DataFactory.create_dataset(data_source)
    preprocessor = SimplePreprocessing()
    model = LinearModel(logger)
    evaluator = Evaluator()


    trainer = Trainer(
        dataset = dataset,
        model = model,
        preprocessor = preprocessor,
        evaluator = evaluator,
        logger = logger)

    trainer.run()

if __name__ == "__main__":
    main()