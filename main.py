# Although I have src here then also I am calling this MlOpsProject why ??
# Because I have initialised my logging funcionality in the __init__ constructor of the MlOpsProject folder ,so I don't need to call the src separately.

import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from MlOpsProject import logger

def some_function():
    logger.info("This is an informational message; only for custom logging")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")

# Call the function to see logging in action
some_function()

# when you run this main.py file you will see the logs in the terminal as well as in the logs file.
