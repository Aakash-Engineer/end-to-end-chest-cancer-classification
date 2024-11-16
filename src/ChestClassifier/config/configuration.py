from ChestClassifier.constants import *
from ChestClassifier.utils.common import read_yaml, create_directories
import gdown
import os
from ChestClassifier.entity.config_entity import DataIngestionConfig
from ChestClassifier.entity.config_entity import PrepareBaseModelConfig
from ChestClassifier.entity.config_entity import TrainingConfig
from ChestClassifier.entity.config_entity import EvaluationCinfig


class ConfigurationManager:
    def __init__(self,
                 config_filepath=CONFIG_FILE_PATH,
                 params_filepath=PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])
    
    def get_dataingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        return DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        create_directories([config.root_dir])

        return PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_include_top=self.params.INCLUDE_TOP,
            params_classes=self.params.CLASSES,
            params_weights=self.params.WEIGHTS,
        )
    
    def get_trainig_config(self):
        training = self.config.training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, 'Chest-CT-Scan-data')
        create_directories([training.root_dir])

        return TrainingConfig(
            root_dir=training.root_dir,
            trained_model_path=training.trained_model_path,
            updated_base_model_path=prepare_base_model.updated_base_model_path,
            training_data=training_data,
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_learning_rate=params.LEARNING_RATE,
            params_image_size=params.IMAGE_SIZE,
            params_is_augmentation=params.AUGMENTATION
        )
    def get_evaluation_config(self) -> EvaluationCinfig:
        return EvaluationCinfig(
            model_path=self.config.training.trained_model_path,
            training_data='artifacts/data_ingestion/Chest-CT-Scan-data',
            mlflow_uri='https://dagshub.com/Aakash-Engineer/end-to-end-chest-cancer-classification.mlflow',
            all_params=self.params,
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )
