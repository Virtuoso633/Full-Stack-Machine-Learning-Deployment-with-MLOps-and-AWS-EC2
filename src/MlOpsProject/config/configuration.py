from MlOpsProject.constants import *
from MlOpsProject.utils.common import read_yaml, create_directories
from MlOpsProject.entity.config_entity import (DataIngestionConfig,
                                                DataValidationConfig,
                                                DataTransformationConfig,
                                                ModelTrainerConfig,
                                                ModelEvaluationConfig)

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
    
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
        )

        return data_transformation_config


    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema =  self.schema.Target_Column

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=Path(config.root_dir),
            train_data_path=Path(config.train_data_path),
            test_data_path=Path(config.test_data_path),
            model_name=config.model_name,
            alpha=params.alpha,  
            l1_ratio=params.l1_ratio, 
            param_grid=params.param_grid, 
            target_column=schema.name
        )

        return model_trainer_config
    
    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema =  self.schema.Target_Column

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir=config.root_dir,
            test_data_path=config.test_data_path,
            model_path = config.model_path,
            all_params=params,
            metric_file_name = config.metric_file_name,
            target_column = schema.name,
            mlflow_uri="https://dagshub.com/Virtuoso633/Full-Stack-Machine-Learning-Deployment-with-MLOps-and-AWS-EC2.mlflow",

        )

        return model_evaluation_config