from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation_comp import DataValiadtion
from mlProject import logger


process = 'Data Validation'

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValiadtion(config=data_validation_config)
            data_validation.validate_all_columns()
        except Exception as e:
            raise e
    
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Process: {process} started <<<<<<")
        obj = DataValidationTrainingPipeline
        obj.main()
        logger.info(f">>>>>> Process: {process} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e