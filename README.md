# mtl-2026-s105

This project aims to build a physical data augmentation software application in Python using [`pyroomacoustics`](https://github.com/LCAV/pyroomacoustics) module. It is proposed to evaluate the augmentations with a multi-class classifier for instrumental-voice models from [Essentia](https://essentia.upf.edu/models.html#voice-instrumental). 

This repository contains some tools for Music Technology Lab subject:

- Initial notebook to show how to use `pyroomacoustics` for creating a physical data augmentation pipeline
- Inference code for voice-instrumental models

## Installation

Create a Python virtual environment

```bash
python -m venv .env
```

or a conda environment

```bash
conda create -n mtl-2026-s105 python=3.9
```

Activate your environment

```bash
source .env/bin/activate      # for venv
conda activate mtl-2026-s105  # for conda envs
```

Install some requirements with

```bash
pip install -r requirements.txt
```


## Preparation

First we'll need to download some models and data. It is almost ready in `scripts/` folder:

```bash
bash scripts/download-embeddings.sh                 # download Essentia feature extraction models
bash scripts/download-podcastmix-dataset.sh         # download podcastmix dataset
bash scripts/download-voice_instrumental-models.sh  # download voice-instrumental models
```

## Usage

For inferencing with the voice_instrumental-audioset-vggish model:

```bash
python voice_instrumental_inference.py
```
```

```
```
```
```
```
```

```
```
```
```
