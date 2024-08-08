#instead of creating a separate logging file ,I will write it in here ,the login functionality just to make the import easy..
#integrating logging functionality directly into your src/mlopsproject/__init__.py file can help streamline imports and centralize your logging configuration. Here’s how you can set it up:


#os: Provides functions for interacting with the operating system, such as file and directory operations.
import os
#sys: Provides access to some variables used or maintained by the interpreter and functions that interact with the interpreter.
import sys
#logging: The standard Python logging module, used for generating log messages.
import logging


"""
#This string defines the format of the log messages. The placeholders are:

%(asctime)s: Timestamp of the log message.
%(levelname)s: Log level of the message (e.g., INFO, WARNING).
%(module)s: Name of the module that generated the log message.
%(message)s: The actual log message.
"""
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"


# specifies the Log Directory where log files will be stored.:
log_dir = "logs"


# Create the Full Log File Path:
# Combines the log directory with the log file name to create the full path to the log file.
log_filepath = os.path.join(log_dir,"running_logs.log")


#Ensure the Log Directory Exists:
#Checks if the log directory exists. If not, it creates the directory. The exist_ok=True argument prevents an error if the directory already exists.
os.makedirs(log_dir, exist_ok=True)


"""
level=logging.INFO: Sets the logging level to INFO. This means all messages of level INFO and above (WARNING, ERROR, CRITICAL) will be logged.

format=logging_str: Uses the previously defined logging format string.

handlers: Defines where the log messages should be directed:
    logging.FileHandler(log_filepath): Sends log messages to the specified file.
    logging.StreamHandler(sys.stdout): Sends log messages to the console.
"""
logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)


#Creates a logger instance with the name "mlProjectLogger". This logger can be used to generate log messages throughout the project.
logger = logging.getLogger("MLOpsProjectLogger")

#This setup ensures that your log messages are consistently formatted and written to both a file and the console,
# making it easier to monitor and debug your application.