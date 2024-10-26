#!/bin/bash

# Define the image name and Docker Compose service name
COMPOSE_FILE="docker-compose.yaml"

echo "----> Stopping and removing any running containers from the previous build"
docker-compose -f $COMPOSE_FILE down

echo "----> Building and running the new Docker image with Docker Compose"
docker-compose --env-file .env -f $COMPOSE_FILE up --build -d
