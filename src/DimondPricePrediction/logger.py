import logging
import os
from datetime import datetime

# Define log file name
LOG_FILE = f"{datetime.now().strftime('%y_%m_%d_%H_%M_%S')}.log"

# Set log path
log_path = os.path.join(os.getcwd(), "logs")

# Create log directory if it doesn't exist
os.makedirs(log_path, exist_ok=True)

# Set log file path
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

# Configure logging
logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILEPATH,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")

if __name__ == '__main__':
    logging.info("here again I am testing ")

