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



## Stage 2 - Data Ingestion
from MlOpsProject import logger
from MlOpsProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<< \n\nx=================x")
except Exception as e:
    logger.exception(e)
    raise e

