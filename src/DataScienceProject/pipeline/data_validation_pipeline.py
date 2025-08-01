from src.DataScienceProject.config.configuration import ConfigurationManager
from src.DataScienceProject.components.data_validation import DataValidation
from src.DataScienceProject import logger

STAGE_NAME = "Data Validation stage"

class DataValidation_TrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config= ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()

    
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidation_TrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f"Stage {STAGE_NAME} completed! All the components are executed successfully.")
    except Exception as e:
        logger.error(f"Error occurred in stage {STAGE_NAME}: {e}")
        raise e