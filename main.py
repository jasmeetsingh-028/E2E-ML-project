from mlProject import logger
from mlProject.pipeline.data_ingestion_pipe01 import DataIngestionTrainingPipeline
from mlProject.pipeline.data_validation_pipe02 import DataValidationTrainingPipeline

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