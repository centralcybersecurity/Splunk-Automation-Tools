import splunklib.client as client
import time

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

while True:
  results = service.jobs.oneshot("search index=_internal | stats count by source")

  if int(results['count']) > 100:
    print("Alert! Internal event count > 100")

  time.sleep(10)