from src.cnnClassifier.constants import *
from src.cnnClassifier.utils.common import read_yaml,create_directories
from src.cnnClassifier import logger
from src.cnnClassifier.entity.config_entity import DataIngestionConfig









class ConfigurationManager:
    def __init__(self, config_filepath= CONFIG_FILE_PATH,
                 params_filepath= PARAMS_FILE_PATH):
        
        self.config_filepath = read_yaml(config_filepath)
        self.params_filepath = read_yaml(params_filepath)

        create_directories([self.config_filepath.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:
        config= self.config_filepath.data_ingestion

        data_ingestion_config= DataIngestionConfig(
                                root_dir= config.root_dir,
                                source_URL= config.source_URL,
                                local_data_file= config.local_data_file,
                                unzip_dir= config.unzip_dir,
                                prefix_ID=config.prefix_ID)
        return data_ingestion_config

