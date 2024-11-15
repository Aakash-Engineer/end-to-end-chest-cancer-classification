from ChestClassifier.config.configuration import ConfigurationManager
from ChestClassifier.components.data_ingestion import DataIngestion
from ChestClassifier import logger

STEP_NAME = 'Data Ingestion Step'

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_dataingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()
    

if __name__ == '__main__':
    try:
        logger.info(f'>>>>>>>>>>>>> {STEP_NAME} started <<<<<<<<<<<<<<')
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>>>>>>>>> {STEP_NAME} completed <<<<<<<<<<<<<<')
    except Exception as e:
        logger.exception(e)
        raise e