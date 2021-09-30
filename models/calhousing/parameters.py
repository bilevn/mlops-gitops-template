import os
import pathlib
from typing import Tuple
from pathlib import Path
from dataclasses import dataclass

from ..settings import config


@dataclass(frozen=True)
class BaseParameters:
    data_path: Path = config.datasets_path.joinpath("cal_housing.data")
    target_column_name: str = "medianHouseValue"
    data_columns_names: Tuple = (
        "longitude",
        "latitude",
        "housingMedianAge",
        "totalRooms",
        "totalBedrooms",
        "population",
        "households",
        "medianIncome",
        "medianHouseValue",
    )

    @staticmethod
    def get_model_path(model_id):
        return config.models_path.joinpath(f"{model_id}.joblib")


@dataclass(frozen=True)
class HyperParameters:
    n_estimators: int = 50
    subsample: float = 0.8
    max_depth: int = 5


@dataclass(frozen=True)
class ValidationParameters:
    cross_validation_folds_number: int = 3
    metric_name: str = "r2"
