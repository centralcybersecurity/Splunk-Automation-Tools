# Splunk Alert Script

This script polls the Splunk API and generates alerts based on search results.

## Usage

1. Install dependencies

pip install -r requirements.txt


2. Update `splunk_alert.py` with your Splunk credentials and desired search query.

3. Configure the alert threshold and polling interval as needed.

4. Run the script:

python src/splunk_alert.py


The script will poll the Splunk API based on the interval, run the search query, check the results against the alert threshold, and print an alert if exceeded.

## Configuration

The following variables can be configured in `splunk_alert.py`:

- HOST - Splunk host URL 
- PORT - Splunk port, usually 8089
- USERNAME - Splunk username
- PASSWORD - Splunk password
- Search query - The search query to run 
- Alert threshold - The threshold that triggers an alert
- Polling interval - How often to run the search in seconds  

## Troubleshooting

- Ensure the Splunk SDK is installed via `requirements.txt`
- Check for errors connecting to Splunk or running search
- Adjust alert threshold or polling interval as needed
- Validate Splunk credentials and network connectivity