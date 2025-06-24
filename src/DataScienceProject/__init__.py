## all the information
import os
import sys
import logging

## able to log each & every details - in all the files we be able to see all the information
logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

logging_dir = "logs"
log_filepath = os.path.join(logging_dir, "running_logs.log")
os.makedirs(logging_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("DataScience_Logger")



