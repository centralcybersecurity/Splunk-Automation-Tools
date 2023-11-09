import splunklib.client as client
import xml.etree.ElementTree as ET

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

# Load dashboard XML
tree = ET.parse('dashboards/sample_dashboard.xml')
xml = ET.tostring(tree.getroot(), encoding='utf8', method='xml')

# Create dashboard
service.dashboards.create('Sample Dashboard', xml, overwrite=True)

print("Dashboard created!")