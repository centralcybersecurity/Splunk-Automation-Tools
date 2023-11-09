import splunklib.client as client
import logging
import time

# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Splunk credentials and configuration  
HOST = "localhost"
PORT = 8089  
USERNAME = "admin"
PASSWORD = "password"

# Connect to Splunk
service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD)

# Get list of indexes
indexes = service.indexes

# Loop through indexes
for index in indexes:

    # Check if index is cold
    if index.is_cold():

        # Attach index
        index.attach()

        # Delete index
        index.delete()

        # Log deletion
        logging.info(f"Deleted index: {index.name}")

    else:
        logging.info(f"Index {index.name} is not cold, skipping")

# Wait 1 day        
time.sleep(86400)