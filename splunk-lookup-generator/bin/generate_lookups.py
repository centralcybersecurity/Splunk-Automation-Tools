import csv
import json
from pathlib import Path

import yaml

CONFIG_FILE = Path(__file__).parent.parent / 'README' / 'transforms.conf'

def generate_lookup(name, config):
    # Load source data
    if config['sourcetype'] == 'csv':
        data = load_csv(config['source']) 
    elif config['sourcetype'] == 'json':
        data = load_json(config['source'])

    # Extract key and values    
    keys = [row[config['key']] for row in data]
    values = [[row[v] for v in config['values']] for row in data]

    # Write CSV lookup
    with open(f'lookups/{name}.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(zip(keys, *values))

def load_csv(filename):
    with open(filename) as f:
        reader = csv.DictReader(f)
        return list(reader)

def load_json(filename):
    with open(filename) as f:
        return json.load(f)

def main():
    config = yaml.safe_load(open(CONFIG_FILE)) 
    for name, options in config.items():
        generate_lookup(name, options)

if __name__ == '__main__':
    main()