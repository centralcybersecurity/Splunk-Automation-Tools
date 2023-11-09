# Splunk CSV Exporter

This script exports Splunk search results to a CSV file. 

## Usage

1. Install dependencies

```
pip install -r requirements.txt
```

2. Update the splunk_csv_exporter.py script with your Splunk credentials and desired search query.

3. Run the script:

```
python src/splunk_csv_exporter.py
```

This will export the search results to `splunk_metrics.csv` in the current directory.

4. The exported CSV file can be opened in any spreadsheet program for analysis and visualization.

## Configuration

The following variables can be configured in splunk_csv_exporter.py:

- HOST - Splunk host URL
- PORT - Splunk port, usually 8089
- USERNAME - Splunk username 
- PASSWORD - Splunk password
- search_query - The search query to run and export results for

## Troubleshooting

- Ensure the Splunk SDK is installed via `requirements.txt`
- Check for any errors connecting to Splunk or running the search
- Verify Splunk credentials and connectivity
- Try modifying the search query if no results are exported

