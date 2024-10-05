import os
from MlOpsProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from MlOpsProject.entity.config_entity import DataTransformationConfig


class DataTransformer:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        
    # Dataset I am using is already clean, so I am not doing any EDA
    # Only train-test split is done (for now)
        
    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        #This line of code saves the training data train (a pandas DataFrame) to a CSV file named train.csv in the directory specified by self.config.root_dir.
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        #This line of code saves the testing data test (a pandas DataFrame) to a CSV file named test.csv in the directory specified by self.config.root_dir.
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)