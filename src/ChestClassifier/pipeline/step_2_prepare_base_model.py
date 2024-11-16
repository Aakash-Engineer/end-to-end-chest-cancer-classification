from ChestClassifier.config.configuration import ConfigurationManager
from ChestClassifier.components.prepare_base_model import PrepareBaseModel
from ChestClassifier import logger



STEP_NAME = "PrepareBaseModel Step"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()



if __name__ == '__main__':
    try:
        logger.info(f'>>>>>>>>>>>>> {STEP_NAME} started <<<<<<<<<<<<<<')
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>>>>>>>>> {STEP_NAME} completed <<<<<<<<<<<<<<')
    except Exception as e:
        logger.exception(e)
        raise e