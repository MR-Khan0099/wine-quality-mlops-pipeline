from src.DataScienceProject import logger
from src.DataScienceProject.pipeline.data_ingestion_pipeline import DataIngestion_TrainingPipeline
from src.DataScienceProject.pipeline.data_validation_pipeline import DataValidation_TrainingPipeline
from src.DataScienceProject.pipeline.data_transformation_pipeline import DataTransformationTrainingPipeline
from src.DataScienceProject.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.DataScienceProject.pipeline.mode_evaluation_pipeline import ModelEvaluationTrainingPipeline




STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestion_TrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f"Stage {STAGE_NAME} completed!")
except Exception as e:
    logger.error(f"Error occurred in stage {STAGE_NAME}: {e}")
    raise e 



STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_validation = DataValidation_TrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f"Stage {STAGE_NAME} completed!")
except Exception as e:
    logger.error(f"Error occurred in stage {STAGE_NAME}: {e}")
    raise e 



STAGE_NAME = "Data Transformation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataTransformationTrainingPipeline()
   data_ingestion.initiate_data_transformation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Model Trainer stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   model_trainer = ModelTrainerPipeline()
   model_trainer.initiate_model_training()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model evaluation stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_evalution = ModelEvaluationTrainingPipeline()
   data_evalution.initiate_model_evaluation()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e







