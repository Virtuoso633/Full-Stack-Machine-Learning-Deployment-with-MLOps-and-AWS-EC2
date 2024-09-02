from MlOpsProject.config.configuration import ConfigurationManager
from MlOpsProject.components.data_ingestion import DataIngestion
from MlOpsProject import logger

STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager() 
        data_ingestion_config = config.get_data_ingestion_config() 
        data_ingestion = DataIngestion(config= data_ingestion_config) 
        data_ingestion.download_file()
        data_ingestion.extract_zip_file() 

if __name__ == '__main__': #is commonly used in Python scripts to ensure that certain parts of the code are only executed when the script is run directly, not when it is imported as a module into another script.When a Python file is imported as a module, the code inside the if __name__ == '__main__': block will not execute, preventing unintended behavior.
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n\nx=================x")
    except Exception as e:
        logger.exception(e)
        raise e 