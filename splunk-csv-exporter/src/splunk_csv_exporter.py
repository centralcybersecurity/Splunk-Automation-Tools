import splunklib.client as client
import csv

# Splunk credentials
HOST = "localhost"  
PORT = 8089
USERNAME = "admin"
PASSWORD = "password" 

service = client.connect(
    host=HOST,
    port=PORT,
    username=USERNAME,
    password=PASSWORD
)

# Search query
search_query = "search index=_internal | stats count by source"

# Export results 
results = service.jobs.export(search_query)  

# Write CSV file
with open('splunk_metrics.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(results)

print("Exported to splunk_metrics.csv")