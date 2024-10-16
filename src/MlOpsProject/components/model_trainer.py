import pandas as pd
import os
import yaml  # Add this to load the params.yaml file
from MlOpsProject import logger
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import GridSearchCV
import joblib
from MlOpsProject.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def load_params(self):
        """Extract param_grid directly from the config (ConfigBox)."""
        try:
            # Debugging: print the config to verify its structure
            print(f"Loaded config: {self.config}")
            
            param_grid = self.config.param_grid
            return param_grid
        except KeyError as e:
            raise ValueError(f"Failed to load param_grid from config: {e}")
            
    
    def train(self):
        try:
            # Load params from the ConfigBox (which loads the YAML)
            params = self.load_params()
            
            # Load training and testing data
            train_data = pd.read_csv(self.config.train_data_path)
            test_data = pd.read_csv(self.config.test_data_path)

            train_x = train_data.drop([self.config.target_column], axis=1)
            test_x = test_data.drop([self.config.target_column], axis=1)
            train_y = train_data[[self.config.target_column]]
            test_y = test_data[[self.config.target_column]]

            # Logging the shapes of train and test data
            logger.info(f"Training data shape: {train_x.shape}, Target shape: {train_y.shape}")
            logger.info(f"Test data shape: {test_x.shape}, Target shape: {test_y.shape}")

            # Initialize ElasticNet model without specifying alpha and l1_ratio
            lr = ElasticNet(random_state=42)
            
            # GridSearchCV for hyperparameter tuning
            grid_search = GridSearchCV(estimator=lr, param_grid=params, 
                                        cv=5, scoring='neg_mean_squared_error', n_jobs=-1, verbose=2)

            # Fit the model with hyperparameter tuning
            grid_search.fit(train_x, train_y.values.ravel())  # .values.ravel() to flatten the target variable

            # Get the best model and parameters
            best_model = grid_search.best_estimator_
            best_params = grid_search.best_params_
            logger.info(f"Best parameters found: {best_params}")

            # Save the best model
            model_path = os.path.join(self.config.root_dir, self.config.model_name)
            joblib.dump(best_model, model_path)
            logger.info(f"Model saved at {model_path}")
            
        except Exception as e:
            logger.exception("Error during model training")
            raise e
