import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"   #f"....log " creates a filename by appending .log at last;datetime.now returns current date and time; strftime formats the input 
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)    #.getcwd returns the name of current working directory
os.makedirs(logs_path,exist_ok=True)      #exists_ok - if directory already exists no error will be raised

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,    

)

# if __name__ == '__main__':
#     logging.info('Logging has started')