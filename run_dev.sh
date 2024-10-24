#!/bin/bash

# How To Run:
# 1. Provide execution permissions to the shell script by running: chmod +x init_bigquery_database.sh
# 2. Run: bash run_dev.sh
# 3. Previous Running Streamlit is terminated, and a new streamlit is created

# Function to kill any running Streamlit process
kill_previous_streamlit() {
    echo "\nChecking for running Streamlit instances..."
    # Find the process running on port 8501 (default Streamlit port) and kill it
    PID=$(lsof -ti:8501)  # Get the process ID for port 8501
    if [ -n "$PID" ]; then
        echo "Killing previous Streamlit process (PID: $PID)..."
        kill -9 $PID
    else
        echo "No running Streamlit instance found."
    fi
}

run_dev() {
    kill_previous_streamlit
    echo "Running in DEV environment..."
    export STREAMLIT_ENV=dev
    streamlit run app.py
}


run_dev
