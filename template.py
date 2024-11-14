import os
import logging
from pathlib import Path

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

PROJECT_NAME = 'Chest_classifier'
LIST_OF_FILES = [
    '.github/workflows/.gitkeep',
    f'src/{PROJECT_NAME}/__init__.py',
    f'src/{PROJECT_NAME}/components/__init__.py',
    f'src/{PROJECT_NAME}/config/__init__.py',
    f'src/{PROJECT_NAME}/config/configuration.py',
    f'src/{PROJECT_NAME}/entity/__init__.py',
    f'src/{PROJECT_NAME}/pipeline/__init__.py',
    f'src/{PROJECT_NAME}/utils/__init__.py',
    f'src/{PROJECT_NAME}/constants/__init__.py',
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'setup.py',
    'research/trials.ipynb',
    'templates/index.html',
    'requirements.txt',
]

for filepath in LIST_OF_FILES:
    filepath = Path(filepath)
    filedir = os.path.dirname(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath} already exists")
