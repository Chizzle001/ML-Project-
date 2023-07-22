import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,


)
    



"""
The code sets up a basic logging configuration in Python. Here's what each part of the code does:

1. LOG_FILE: This variable stores the name of the log file with a timestamp generated using the current date and time in the format "mm_dd_yyyy_HH_MM_SS.log".

2. logs_path: This variable is set to the path of the log file within the "logs" directory. 
   The "logs" directory is created if it doesn't exist using os.makedirs(logs_path, exist_ok=True).

3. LOG_FILE_PATH: This variable stores the complete path of the log file by joining the "logs" directory path and the log file name.

4. logging.basicConfig(): This function sets up the basic configuration for logging in Python. 
   It takes several arguments to customize the logging behavior:

    - filename: The path of the log file where log messages will be written. In this case, it's set to LOG_FILE_PATH, which points to the log file within the "logs" directory.

    - format: The format of the log messages. The format specifies how each log message will look. In this case, it's set to "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", which includes the timestamp, line number, logger name, log level, and log message.

    - level: The logging level threshold. It determines which log messages will be written to the log file. In this case, it's set to logging.INFO, which means only messages with the log level "INFO" and above will be logged.

With this configuration, any log messages of level "INFO" and above will be written to the log file with the specified format. 
The log file will have a timestamp in its name to avoid overwriting previous logs and will be stored in the "logs" directory under the current working directory.
"""