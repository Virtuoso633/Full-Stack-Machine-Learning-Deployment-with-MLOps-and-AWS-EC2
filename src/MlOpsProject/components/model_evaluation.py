# import os
# import pandas as pd
# from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
# from urllib.parse import urlparse
# import mlflow
# import mlflow.sklearn
# import numpy as np
# import joblib
# from MlOpsProject.entity.config_entity import ModelEvaluationConfig
# from MlOpsProject.utils.common import save_json
# from pathlib import Path


# class ModelEvaluation:
#     def __init__(self, config: ModelEvaluationConfig):
#         self.config = config

    
#     def eval_metrics(self, actual, pred):
#         rmse = np.sqrt(mean_squared_error(actual, pred))
#         mae = mean_absolute_error(actual, pred)
#         r2 = r2_score(actual, pred)
#         return rmse, mae, r2
    

#     def log_into_mlflow(self):
#         # Check if there's an active run
#         if mlflow.active_run():
#             mlflow.end_run()  # End any active run before starting a new one

#         test_data = pd.read_csv(self.config.test_data_path)
#         model = joblib.load(self.config.model_path)

#         test_x = test_data.drop([self.config.target_column], axis=1)
#         test_y = test_data[[self.config.target_column]]


#         mlflow.set_registry_uri(self.config.mlflow_uri)
#         tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        
#         with mlflow.start_run():

#             predicted_qualities = model.predict(test_x)

#             (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)
            
#             # Saving metrics as local
#             scores = {"rmse": rmse, "mae": mae, "r2": r2}
#             save_json(path=Path(self.config.metric_file_name), data=scores)

#             mlflow.log_params(self.config.all_params)

#             mlflow.log_metric("rmse", rmse)
#             mlflow.log_metric("r2", r2)
#             mlflow.log_metric("mae", mae)

#             # Model registry does not work with file store
#             if tracking_url_type_store != "file":

#                 # Register the model
#                 # There are other ways to use the Model Registry, which depends on the use case,
#                 # please refer to the doc for more information:
#                 # https://mlflow.org/docs/latest/model-registry.html#api-workflow
#                 mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")
#             else:
#                 mlflow.sklearn.log_model(model, "model")


                
"""
    Modified after this Exception:
    Exception: Run with UUID 99ad35a6154f44ed9cc6ff39cb64be73 is already active. To start a new run, first end the current run with mlflow.end_run(). To start a nested run, call start_run with nested=True
"""

import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from MlOpsProject.entity.config_entity import ModelEvaluationConfig
from MlOpsProject.utils.common import save_json
from pathlib import Path


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    # Evaluation metrics calculation
    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    # Main function to log into MLflow
    def log_into_mlflow(self):
        # Check if there's an active run
        if mlflow.active_run():
            mlflow.end_run()  # End any active run before starting a new one

        # Load test data
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]

        # Set the tracking URI and determine the type of tracking store
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        # Start the MLflow run
        with mlflow.start_run():
            # Predict using the loaded model
            predicted_qualities = model.predict(test_x)

            # Calculate evaluation metrics
            rmse, mae, r2 = self.eval_metrics(test_y, predicted_qualities)
            
            # Save metrics locally
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            # Log all hyperparameters from config
            mlflow.log_params(self.config.all_params)

            # Log metrics
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)

            # Model registry only works if the tracking store is not a file system
            if tracking_url_type_store != "file":
                # Log the model and register it
                mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticnetModel")
            else:
                # If using a file store, just log the model without registering
                mlflow.sklearn.log_model(model, "model")
        
        # Ensure that the MLflow run is ended properly after logging
        mlflow.end_run()
