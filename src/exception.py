import sys
from src.logger import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
     file_name,exc_tb.tb_lineno,str(error))

    return error_message

    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    

"""
The code defines a custom exception class CustomException, which is designed to log and handle exceptions with additional details.

Here's a breakdown of the code:

The code imports the sys module to work with system-specific parameters and the logging module from a custom package named src.logger. 
The logging module is used to log the exceptions.

The function error_message_detail(error, error_detail: sys) is defined to extract relevant information from the error and return a formatted error message. 
It uses the sys.exc_info() function to get information about the exception. 
It retrieves the filename and line number where the exception occurred and combines them with the error message to create a descriptive error message.

The CustomException class is defined as a subclass of the built-in Exception class. It takes two arguments in the constructor: error_message and error_detail: sys. 
It calls the super() function to initialize the parent class (Exception) with the provided error_message.

The CustomException class overrides the __str__() method, which is called when the exception is converted to a string. It returns the error_message attribute, 
which contains the detailed error message generated by the error_message_detail() function.

Overall, this code creates a custom exception class that captures exceptions and logs additional information about the errors, such as the filename and line number where the exception occurred. 
It can be used to enhance error handling and debugging in Python applications. However, it's important to note that the logging module should be appropriately configured to log the exceptions effectively.
"""