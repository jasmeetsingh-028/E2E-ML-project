from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion_comp import DataIngestion
from mlProject import logger


process = 'Data Ingestion'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        except Exception as e:
            raise e
        

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Process: {process} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Process: {process} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e