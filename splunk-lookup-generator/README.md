# Splunk Lookup Table Generator

This app generates Splunk lookup tables from external data sources.

## Overview

The `generate_lookups.py` script pulls data from the `/data` folder and outputs CSV lookup files to the `/lookups` folder.

Lookup logic is defined in `/README/transforms.conf`.

## Usage

1. Place external data source files (JSON, CSV, etc) in the `/data` folder.

2. Update `transforms.conf` to define the lookup table generation logic.

    Example config:

    ```
    [countries]
    sourcetype = csv
    source = data/countries.csv
    key = country

    [cities]
    sourcetype = json
    source = data/cities.json
    key = city
    ```

3. Run `python bin/generate_lookups.py` to generate the lookups in `/lookups`.

4. Deploy the app to Splunk to make the lookups available.

## Lookup Configuration

- Lookup key fields are specified in `transforms.conf`
- Generated CSVs will include this key field and lookup values
- Lookup names will match the stanza name in `transforms.conf`

## Adding Data Sources

- Add new data source files to the `/data` folder
- Define generation logic in `transforms.conf` 
- Re-run `generate_lookups.py` to create the new lookups

## Troubleshooting

- Validate `transforms.conf` contains valid stanzas for each lookup
- Ensure `source` paths are correct
- If lookups are not seen in Splunk, check they are defined in `transforms.conf` and the app is deployed

