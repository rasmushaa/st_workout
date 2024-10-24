#!/bin/bash

# How To Run:
# 1. Create a Google Cloud Project manually or use an existing project to include a new dataset with the tables
# 2. Create a .env.<dev, stg, prod> files to root, and add required variables
# 2. Provide execution permissions to the shell script by running: chmod +x init_bigquery_database.sh
# 3. Run: bash init_bigquery_database.sh <dev, stg, prod>
# 4. The Terminal prints ether Success, or Provides Instructions


# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: ./init_bigquery_database.sh <dev, stg, prod>"
    exit 1
fi

ENV=$1

# Run the Python script
python3 init_bigquery_database.py "$ENV"
