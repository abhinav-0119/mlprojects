#logger.py helps keep track of the application's execution by
# recording important events and errors in log files."
import logging
import os
from datetime import datetime
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs")
os.makedirs(logs_path,exist_ok=True)
LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
# A LogRecord is an object created automatically by Python whenever you call logging levels
# This object contains many predefined attributes (variables).
''' LogRecord
│
├── asctime      → Current date & time
├── lineno       → Line number
├── filename     → Current file name
├── module       → Module name
├── funcName     → Function name
├── levelname    → INFO / ERROR / WARNING
├── message      → Your log message
├── name         → Logger name
├── pathname     → Full file path
├── process      → Process ID
├── thread       → Thread ID
└── ...'''
'''
Jo level hum set karte hain, us level aur usse upar 
(higher severity) ke saare log messages record hote hain. 
Usse niche wale levels ignore ho jaate hain.
'''