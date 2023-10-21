from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation_comp import ModelEvaluation
from mlProject import logger


process = 'Model Evaluation'

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.log_into_mlflow()
        except Exception as e:
            raise e
    
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Process: {process} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Process: {process} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e