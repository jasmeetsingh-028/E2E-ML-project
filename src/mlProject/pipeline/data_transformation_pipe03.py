from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_transformation_comp import DataTransformation
from mlProject import logger
from pathlib import Path


process = 'Data Transformation'

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]
                print(status)

            if status == "True" or "Successful":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()

            else:
                raise Exception("You data schema is not valid")

        except Exception as e:
            print(e)

        
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Process: {process} started <<<<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Process: {process} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e