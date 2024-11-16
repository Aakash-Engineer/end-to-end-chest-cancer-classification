from ChestClassifier.config.configuration import ConfigurationManager
from ChestClassifier.components.training import Training
from ChestClassifier import logger



STEP_NAME = 'TRAINING STEP'

class TrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_trainig_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

if __name__ == '__main__':
    try:
        logger.info(f'>>>>>>>>>>>>> {STEP_NAME} started <<<<<<<<<<<<<<')
        obj = TrainingPipeline()
        obj.main()
        logger.info(f'>>>>>>>>>>>>> {STEP_NAME} completed <<<<<<<<<<<<<<')
    except Exception as e:
        logger.exception(e)
        raise e