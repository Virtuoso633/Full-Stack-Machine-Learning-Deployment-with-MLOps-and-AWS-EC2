import os 
import urllib.request as request
import zipfile
from MlOpsProject import logger
from MlOpsProject.utils.common import get_size
from pathlib import Path
from MlOpsProject.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig): # The constructor (__init__) initializes the class with a configuration object config of type DataIngestionConfig.
        self.config = config # self.config: This stores the configuration object, which is expected to contain the settings needed for data ingestion, such as the source URL and the local file path.
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve( 
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
            # If the file does not exist:
            # It uses 'request.urlretrieve' to download the file from the URL specified by 'self.config.source_URL' and saves it to the local path specified by 'self.config.local_data_file'.
            # 'filename' and 'headers' capture the file path and the HTTP headers received during the download.
            # A log message is generated using 'logger.info', indicating the download is complete, along with information from the headers.
        else:
            logger.info(f"File already exists of size : {get_size(Path(self.config.local_data_file))}")
            #It logs a message indicating that the file already exists and displays its size using the get_size function, which takes the local file path as a parameter.
            
    def extract_zip_file(self):
        """
        zip_file path : str
        Extracts the zip file into the data directory
        Funtion returns None
        """
        
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)

