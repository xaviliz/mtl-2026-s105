#!/bin/bash

# Create a directory for the models
MODEL_DIR="data/models/feature-extractors"
mkdir -p "$MODEL_DIR"

# Base URL
BASE_URL="https://essentia.upf.edu/models/feature-extractors"

# Define models with their suffixes
declare -A MODELS=(
  ["vggish"]="audioset-vggish-3"
  ["discogs-effnet"]="discogs-effnet-bs64-1"
  ["musicnn"]="msd-musicnn-1"
)

# Download each model and its metadata
for model in "${!MODELS[@]}"; do
  filename_base="${MODELS[$model]}"

  # Download the model file (.pb)
  model_url="${BASE_URL}/${model}/${filename_base}.pb"
  echo "Downloading $model model from $model_url..."

  wget -P "$MODEL_DIR" "$model_url"
  if [ $? -eq 0 ]; then
    echo "✅ $model model downloaded successfully."
  else
    echo "❌ Failed to download $model model."
  fi

  # Download the metadata file (.json)
  json_url="${BASE_URL}/${model}/${filename_base}.json"
  echo "Downloading $model metadata from $json_url..."
  wget -P "$MODEL_DIR" "$json_url"
  if [ $? -eq 0 ]; then
    echo "✅ $model metadata downloaded successfully."
  else
    echo "❌ Failed to download $model metadata."
  fi

  echo "---"
done

echo "All downloads complete. Models saved in $MODEL_DIR"
