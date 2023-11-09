# Splunk Dashboard Creator

This script creates and updates Splunk dashboards from XML template files.

## Usage

1. Install dependencies

pip install -r requirements.txt


2. Modify `dashboards/sample_dashboard.xml` or add other dashboard XML files

The `sample_dashboard.xml` contains a more advanced sample with:

- Index picker for main and history indexes
- Alerts overview panel
- Key metrics showing tables and charts
- Additional search commands and macros

3. Update Splunk credentials in `create_dashboards.py`

4. Run the script:

python src/create_dashboards.py


This will create the dashboards in Splunk from the template XML files. To update, simply run the script again.

## Creating Dashboard XML

The [Splunk dashboard XML schema](https://docs.splunk.com/Documentation/Splunk/8.0.4/Viz/DashboardXml) can be used to build custom dashboard XML files. These can be saved in the `dashboards` folder and will be created when running the script.

## Scheduling

To automatically update dashboards on a schedule, configure the script to run as a cron job or use a scheduler like Airflow.

## Troubleshooting

- Ensure Splunk SDK is installed via `requirements.txt`
- Validate Splunk credentials and connectivity 
- Check `dashboards` folder contains valid XML
- Adjust cron schedule if dashboards are not updating