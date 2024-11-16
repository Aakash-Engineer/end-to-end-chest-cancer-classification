from ChestClassifier import logger
from ChestClassifier.pipeline.step_1_data_ingestion import DataIngestionTrainingPipeline
from ChestClassifier.pipeline.step_2_prepare_base_model import PrepareBaseModelTrainingPipeline
from ChestClassifier.pipeline.step_3_training import TrainingPipeline
from ChestClassifier.pipeline.step_4_evaluation import EvaluationPipeline

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

# STEP 3 - Training
STEP_NAME = "Training Step"
try:
    logger.info(f'>>>>>>>>>>>>> {STEP_NAME} started <<<<<<<<<<<<<<')
    obj = TrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>>>>>>>> {STEP_NAME} completed <<<<<<<<<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e


# STEP 4 - Evaluation
STEP_NAME = "Evaluation Step"   
try:
    logger.info(f'>>>>>>>>>>>>> {STEP_NAME} started <<<<<<<<<<<<<<')
    obj = EvaluationPipeline()
    obj.main()
    logger.info(f'>>>>>>>>>>>>> {STEP_NAME} completed <<<<<<<<<<<<<<')
except Exception as e:
    logger.exception(e)
    raise e