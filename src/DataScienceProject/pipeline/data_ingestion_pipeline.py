from src.DataScienceProject.config.configuration import ConfigurationManager

from src.DataScienceProject.components.data_ingestion import DataIngestion
from src.DataScienceProject import logger


STAGE_NAME = "Data Ingestion stage"

class DataIngestion_TrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config= ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_zip_file()

if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestion_TrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f"Stage {STAGE_NAME} completed! All the components are executed successfully.")
    except Exception as e:
        logger.error(f"Error occurred in stage {STAGE_NAME}: {e}")
        raise e 
