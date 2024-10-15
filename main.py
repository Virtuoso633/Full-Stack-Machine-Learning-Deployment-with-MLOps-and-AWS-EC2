# # Although I have src here then also I am calling this MlOpsProject directly, why ??
# # Because I have initialised my logging funcionality in the __init__ constructor of the MlOpsProject folder ,so I don't need to call the src separately.

# import sys
# import os

# # Add the src directory to the Python path
# sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# from MlOpsProject import logger

# def some_function():
#     logger.info("This is an informational message; only for custom logging")
#     logger.warning("This is a warning message.")
#     logger.error("This is an error message.")

# # Call the function to see logging in action
# some_function()

# # when you run this main.py file you will see the logs in the terminal as well as in the logs file.



from MlOpsProject import logger
from MlOpsProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from MlOpsProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from MlOpsProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from MlOpsProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from MlOpsProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

# Import and initialize MLflow and DagsHub
import mlflow
import dagshub
from mlflow.models.signature import infer_signature
import joblib

# Initialize the DagsHub connection (this sets the tracking URI)
dagshub.init(repo_owner='Virtuoso633', repo_name='Full-Stack-Machine-Learning-Deployment-with-MLOps-and-AWS-EC2', mlflow=True)

# Start the overall MLflow run
with mlflow.start_run() as main_run:
    mlflow.log_param('execution_stage', 'Pipeline Started')

    ## Stage 1 - Data Ingestion
    STAGE_NAME = "Data Ingestion stage"
    try:
        logger.info(f">>>> stage {STAGE_NAME} started <<<<")
        with mlflow.start_run(nested=True):  # Nested run for the stage
            data_ingestion = DataIngestionTrainingPipeline()
            data_ingestion.main()
            
            # Log that data ingestion completed
            mlflow.log_param('data_ingestion', 'completed')
        logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n\nx=================x")
        mlflow.end_run()  # End the nested run
    except Exception as e:
        logger.exception(e)
        raise e

    ## Stage 2 - Data Validation
    STAGE_NAME = "Data Validation stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        with mlflow.start_run(nested=True):  # Nested run for the stage
            data_validation = DataValidationTrainingPipeline()
            data_validation.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        mlflow.end_run()  # End the nested run
    except Exception as e:
        logger.exception(e)
        raise e

    ## Stage 3 - Data Transformation
    STAGE_NAME = "Data Transformation stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        with mlflow.start_run(nested=True):  # Nested run for the stage
            data_transformation = DataTransformationTrainingPipeline()
            data_transformation.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        mlflow.end_run()  # End the nested run
    except Exception as e:
        logger.exception(e)
        raise e


    ## Stage 4 - Model Training
    STAGE_NAME = "Model Trainer stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        with mlflow.start_run(nested=True):  # Nested run for the stage
            model_trainer = ModelTrainerTrainingPipeline()
            model = model_trainer.main()

            # Log the model using MLflow
            mlflow.sklearn.log_model(model, "model")
            mlflow.log_param('model_training', 'completed')
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        mlflow.end_run()  # End the nested run
    except Exception as e:
        logger.exception(e)
        raise e


    ## Stage 5 - Model Evaluation
    STAGE_NAME = "Model Evaluation Stage"
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        with mlflow.start_run(nested=True):  # Nested run for the stage
            model_evaluation = ModelEvaluationTrainingPipeline()
            model_evaluation.main()

        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        mlflow.end_run()  # End the nested run
    except Exception as e:
        logger.exception(e)
        raise e

# End the main run
mlflow.end_run()