from ChestClassifier import logger
from ChestClassifier.pipeline.step_1_data_ingestion import DataIngestionTrainingPipeline
from ChestClassifier.pipeline.step_2_prepare_base_model import PrepareBaseModelTrainingPipeline

# STEP 1 - Data Ingestion
STEP_NAME = 'Data Ingestion Step'
try:
    logger.info(f'>>>>>>>>>>>>> {STEP_NAME} started <<<<<<<<<<<<<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>>>>>>>> {STEP_NAME} completed <<<<<<<<<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e


# STEP 2 - Prepare Base Model
STEP_NAME = "PrepareBaseModel Step"
try:
    logger.info(f'>>>>>>>>>>>>> {STEP_NAME} started <<<<<<<<<<<<<<')
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>>>>>>>> {STEP_NAME} completed <<<<<<<<<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e