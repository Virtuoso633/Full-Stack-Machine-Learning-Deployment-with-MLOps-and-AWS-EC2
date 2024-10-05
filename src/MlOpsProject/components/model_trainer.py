import pandas as pd
import os
from MlOpsProject import logger
from sklearn.linear_model import ElasticNet
import joblib
from MlOpsProject.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    
    def train(self):
        try:
            train_data = pd.read_csv(self.config.train_data_path)
            test_data = pd.read_csv(self.config.test_data_path)

            train_x = train_data.drop([self.config.target_column], axis=1)
            test_x = test_data.drop([self.config.target_column], axis=1)
            train_y = train_data[[self.config.target_column]]
            test_y = test_data[[self.config.target_column]]

            # Logging the shapes of train and test data
            logger.info(f"Training data shape: {train_x.shape}, Target shape: {train_y.shape}")
            logger.info(f"Test data shape: {test_x.shape}, Target shape: {test_y.shape}")

            lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
            lr.fit(train_x, train_y)

            joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))
            logger.info(f"Model saved at {os.path.join(self.config.root_dir, self.config.model_name)}")

        except Exception as e:
            logger.exception("Error during model training")
            raise e
