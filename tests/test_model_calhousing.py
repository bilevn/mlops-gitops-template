import os
import pytest

from models.calhousing.model import CalhousingModel


@pytest.fixture(scope="session")
def model():
    model = CalhousingModel(model_id="calhousing_test")
    return model


def test_validation(model):
    score = model.validate()
    assert model.validation_parameters.metric_name == "r2"
    assert score > 0.5


def test_train(model):
    model.train()
    assert os.path.isfile(model.model_path)
    os.remove(model.model_path)
