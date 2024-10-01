import os
from pathlib import Path

list_of_files = [
    ".github/workflows/.gitkeep",
    "xray/__init__.py",
    "xray/cloud_storage/__init__.py",
    "xray/cloud_storage/s3_operations.py",
    "xray/cloud_storage/s3_ops.py",
    "xray/components/data_ingestion.py",
    "xray/components/data_transformation.py",
    "xray/components/model_trainer.py",
    "xray/components/model_evaluation.py",
    "xray/components/model_pusher.py",
    "xray/pipeline/__init__.py",
    "xray/pipeline/training_pipeline.py",
    "xray/pipeline/prediction_pipeline.py",
    "xray/constant/__init__.py",
    "xray/constant/training_pipeline/__init__.py",
    "xray/entity/__init__.py",
    "xray/entity/artifacts_entity.py",
    "xray/entity/config_entity.py",
    "xray/utils/utils.py",
    "xray/logger/logging.py",
    "xray/exception/exception.py",
    "xray/ml/__init__.py",
    "xray/ml/model/__init__.py",
    "xray/ml/model/model_service.py",
    "xray/ml/model/arch.py",
    "tests/unit/__init__.py",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent
    filename = filepath.name

    # Create directories if they don't exist
    if filedir:
        filedir.mkdir(parents=True, exist_ok=True)
    
    # Create the file if it doesn't exist or is empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
