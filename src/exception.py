# import logging
import sys                     #all exception happening will already be available on sys; we could also add it in req.txt but its always present

def error_message_detail(error,error_detail:sys):   #2 paramter is present inside sys;2 parameter is used to access exc.info() func. which crucial for obtaining error info
    _,_,exc_tb = error_detail.exc_info()        #first 2 return values are not useful;3 ret value is stored in variable which contains all info
    file_name = exc_tb.tb_frame.f_code.co_filename   #provide file name

    error_msg = "Error occured in py script name[{0}] line number[{1} error msg[{3}]]".format(
        file_name,exc_tb.tb_lineno,str(error)    #all placeholder are used for displaying msg
    )

    return error_msg

class CustomException(Exception):      #create a custom class which inherits exception class
    def __init__(self,error_message,error_detail:sys):    #constructor method;self-reference to instance of our custom class that is being created
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)    #custom class variable -> store

    def __str__(self):
        return self.error_message      #when we raise the error/print it, our custom msg will be printed

