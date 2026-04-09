#!/usr/bin/env bash
set -e

# ==========================================================
# PodcastMix Dataset Downloader
# ==========================================================
#
# Usage:
#   ./download_podcastmix.sh <output_dir> [GDRIVE_TOKEN]
#
# Examples:
#   ./download_podcastmix.sh ../data/dataset/
#   ./download_podcastmix.sh data YOUR_TOKEN
#
# If token is provided → downloads podcastmix-synth subset
# ==========================================================

OUTPUT_DIR=${1:-podcastmix_data}
GDRIVE_TOKEN=${2:-""}

DATA_URL="https://zenodo.org/record/5597047/files/podcastmix.zip"
ZIP_FILE="podcastmix.zip"

mkdir -p "$OUTPUT_DIR"
cd "$OUTPUT_DIR"

echo "========================================"
echo " PodcastMix downloader"
echo " Destination: $(pwd)"
echo "========================================"
echo

# ----------------------------------------------------------
# Download main dataset
# ----------------------------------------------------------
if [ ! -f "$ZIP_FILE" ]; then
  echo "Downloading PodcastMix..."
  curl -L -C - \
    --retry 10 \
    --retry-delay 5 \
    --fail \
    -o "$ZIP_FILE" "$DATA_URL"
else
  echo "$ZIP_FILE already exists — skipping download"
fi

# ----------------------------------------------------------
# Extract main dataset
# ----------------------------------------------------------
if [ ! -d "podcastmix" ]; then
  echo "Extracting PodcastMix..."
  unzip -q "$ZIP_FILE"
else
  echo "PodcastMix already extracted"
fi

# ----------------------------------------------------------
# Optional: Synth subset
# ----------------------------------------------------------
if [ -n "$GDRIVE_TOKEN" ]; then

  echo
  echo "Downloading PodcastMix-Synth subset..."

  cd podcastmix

  # remove previous version if exists
  rm -rf podcastmix-synth

  SYNTH_ARCHIVE="podcastmix-synth.tar.gz"

  curl -L \
    -H "Authorization: Bearer ${GDRIVE_TOKEN}" \
    -o "$SYNTH_ARCHIVE" \
    "https://www.googleapis.com/drive/v3/files/1jouTryUzC9u3SNzwHiMN7kjQigXt-PPG?alt=media"

  echo "Extracting synth subset..."
  tar xzvf "$SYNTH_ARCHIVE"

  echo "Cleaning archive..."
  rm -f "$SYNTH_ARCHIVE"

  cd ..
else
  echo
  echo "Skipping PodcastMix-Synth (no token provided)"
fi

echo
echo "✅ PodcastMix dataset ready!"
echo "Location: $(pwd)/podcastmix"
