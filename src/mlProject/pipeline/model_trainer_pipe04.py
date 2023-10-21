from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer_comp import ModelTrainer
from mlProject import logger


process = 'Model Triner'

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.train()
        except Exception as e:
            raise e

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Process: {process} started <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Process: {process} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e