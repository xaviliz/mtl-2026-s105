from pathlib import Path


script_path = Path(__file__).resolve()
utils_dir = script_path.parent
root_dir = utils_dir.parent

data_dir = root_dir / "data"
generated_dir = data_dir / "generated"
base_model_dir = data_dir / "models"

fe_model_dir = base_model_dir / "feature-extractors"
head_model_dir = base_model_dir / "voice-instrumental"

dataset_dir = data_dir / "dataset"
podcastmix_ds_dir = dataset_dir / "podcastmix"

