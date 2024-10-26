#!/bin/bash

# Define the image name and Docker Compose service name
IMAGE_NAME="st_workout"
IMAGE_TAG="stg"
COMPOSE_FILE="docker-compose.yaml"
ENV_FILE=".env.stg"

# Check if the .env.stg file exists
if [ ! -f "$ENV_FILE" ]; then
  echo "Error: $ENV_FILE file not found!"
  exit 1
fi

echo "----> Stopping and removing any running containers from the previous build"
docker-compose -f $COMPOSE_FILE down

echo "----> Removing previous Docker images with the tag $IMAGE_NAME:$IMAGE_TAG"
docker rmi -f $IMAGE_NAME:$IMAGE_TAG 2>/dev/null

echo "----> Building and running the new Docker image with Docker Compose"
docker-compose -f $COMPOSE_FILE up --build -d
