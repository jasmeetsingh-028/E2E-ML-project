from mlProject import logger
from mlProject.pipeline.data_ingestion_pipe01 import DataIngestionTrainingPipeline
from mlProject.pipeline.data_validation_pipe02 import DataValidationTrainingPipeline
from mlProject.pipeline.data_transformation_pipe03 import DataTransformationTrainingPipeline

#logger.info('Custom log execution')

process = 'Data Ingestion'

try:
    logger.info(f">>>>>> Process: {process} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Process: {process} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

process = 'Data Validation'

try:
    logger.info(f">>>>>> Process: {process} started <<<<<<")
    obj = DataValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Process: {process} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

process = 'Data Transformation'

try:
    logger.info(f">>>>>> Process: {process} started <<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Process: {process} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e