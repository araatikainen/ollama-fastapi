#!/bin/bash

./bin/ollama serve &

pid=$!

sleep 5

# Use the environment variable MODEL_NAME
echo "Pulling ${OLLAMA_VISION_MODEL} model"
ollama pull "${OLLAMA_VISION_MODEL}"

wait $pid