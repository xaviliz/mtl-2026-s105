# Estimate Vggish embeddings and compute voice-instrumental probabilities with an Essentia voice-instrumental model
# https://essentia.upf.edu/models.html#voice-instrumental
#

# An example to infer voice-instrumental models with audio files in Essentia using the
# `voice_instrumental-audioset-vggish.pb` model

import json
from essentia import Pool
from essentia.standard import (
    MonoLoader,
    TensorflowPredictVGGish,
    TensorflowPredict2D
)
from pathlib import Path
from utils.main import export_to_csv, format_predictions
from utils.dir import root_dir, data_dir, generated_dir, base_model_dir, fe_model_dir, head_model_dir, podcastmix_ds_dir

script_path = Path(__file__).resolve()

# Define dataset details
dataset_path = podcastmix_ds_dir / "podcastmix-real-with-reference"
subsets = ("mix", "music", "speech")

# Classes in voice-instrumental model
classes = ("instrumental", "voice")

# Let's process a mix (music + speech)
subset = subsets[2]
audio_path = dataset_path / subset / "1.wav"
audio = MonoLoader(filename=str(audio_path), sampleRate=16000, resampleQuality=4)()
print(f"Processing an excerpt from the {subset} subset: {audio_path}")

embedding_model_path = fe_model_dir / "audioset-vggish-3.pb"
print(f"embedding_model_path: {embedding_model_path}")
embedding_model = TensorflowPredictVGGish(graphFilename=str(embedding_model_path), output="model/vggish/embeddings")
embeddings = embedding_model(audio)

head_model_path = head_model_dir / "voice_instrumental-audioset-vggish-1.pb"
model = TensorflowPredict2D(graphFilename=str(head_model_path), output="model/Softmax")
predictions = model(embeddings)
# print(f"voice_instrumental-audioset-vggish.predictions: {predictions}")

format_predictions(predictions)
out_path = generated_dir / script_path.stem / f"{audio_path.stem}-{subset}.predictions"
out_path.parent.mkdir(parents=True, exist_ok=True)
export_to_csv(predictions, out_path)

