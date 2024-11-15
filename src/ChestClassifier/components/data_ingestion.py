from ChestClassifier import logger
import zipfile
import gdown
import os


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def download_file(self):
        """Download dataset from source URL"""
        try:
            dataset_url = self.config.source_url
            zip_download_dir = self.config.local_data_file

            logger.info(f'Downloading data from {dataset_url} into file {zip_download_dir}')
            file_id = dataset_url.split('/')[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix + file_id, zip_download_dir)
            logger.info(f'Downloaded data from {dataset_url} into {zip_download_dir}')
        except Exception as e:
            raise e
        
    def extract_zip_file(self):
        """Extract dataset zip file"""
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

    
