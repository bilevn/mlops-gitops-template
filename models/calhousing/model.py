import pandas as pd
import joblib
from pathlib import Path
from dataclasses import dataclass
from pandas.core.indexes import base
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import GradientBoostingRegressor


from .parameters import BaseParameters, HyperParameters, ValidationParameters


class CalhousingModel:
    def __init__(self, model_id: str) -> None:
        self.model_id: str = model_id
        self.base_parametes = BaseParameters()
        self.hyper_parameters = HyperParameters()
        self.validation_parameters = ValidationParameters()
        self.model_path: Path = self.base_parametes.get_model_path(model_id)
        df: pd.DataFrame = pd.read_csv(
            self.base_parametes.data_path, names=self.base_parametes.data_columns_names
        )
        self.features: pd.DataFrame = df.loc[
            :, df.columns != self.base_parametes.target_column_name
        ]
        self.target: pd.DataFrame = df[self.base_parametes.target_column_name]
        self.model = GradientBoostingRegressor(
            n_estimators=self.hyper_parameters.n_estimators,
            subsample=self.hyper_parameters.subsample,
            max_depth=self.hyper_parameters.max_depth,
        )

    def validate(self) -> float:
        return cross_val_score(
            self.model,
            self.features,
            self.target,
            cv=self.validation_parameters.cross_validation_folds_number,
            scoring=self.validation_parameters.metric_name,
        ).mean()

    def train(self):
        self.model.fit(self.features, self.target)
        joblib.dump(self.model, self.model_path)
