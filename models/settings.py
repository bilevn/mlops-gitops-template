import os
from pathlib import Path
from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Config:
    project_path: Path = Path(__file__).parent
    datasets_path: Path = project_path.joinpath("../data/datasets")
    models_path: Path = project_path.joinpath("../data/models")
    for p in (datasets_path, models_path):
        p.mkdir(parents=True, exist_ok=True)


config = Config()
