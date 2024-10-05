from MlOpsProject.constants import *
from MlOpsProject.utils.common import read_yaml, create_directories
from MlOpsProject.entity.config_entity import (DataIngestionConfig,
                                                DataValidationConfig)

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH
    ):
        # Load the configuration, parameters, and schema from the YAML files
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)
        
        # Create directories for the artifacts root
        create_directories([self.config.artifacts_root])
    
    # Method to retrieve Data Ingestion Configuration
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        # Read the data_ingestion section from the config
        config = self.config.data_ingestion
        
        # Create necessary directories for data ingestion
        create_directories([config.root_dir])
        
        # Return a DataIngestionConfig object
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    # Method to retrieve Data Validation Configuration
    def get_data_validation_config(self) -> DataValidationConfig:
        # Read the data_validation section from the config
        config = self.config.data_validation
        # Read schema information from the schema file
        schema = self.schema.Columns
        
        # Create necessary directories for data validation
        create_directories([config.root_dir])
        
        # Return a DataValidationConfig object
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            unzip_data_dir=config.unzip_data_dir,
            STATUS_FILE=config.STATUS_FILE,
            all_schema=schema
        )
        
        return data_validation_config
