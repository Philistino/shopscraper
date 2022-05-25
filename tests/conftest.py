import json
import pathlib

import pytest


@pytest.fixture(scope="session")
def RESOURCES_PATH() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parent.joinpath("resources")


@pytest.fixture
def products(RESOURCES_PATH):
    p = pathlib.Path(RESOURCES_PATH, "shopifyapi_response.json")
    data = json.loads(p.read_text())
    return data["products"]


@pytest.fixture
def product_data_single(products):
    return products[0]


@pytest.fixture
def images(product_data_single: dict):
    return product_data_single["images"]


@pytest.fixture
def variants(product_data_single: dict):
    return product_data_single["variants"]


@pytest.fixture
def options(product_data_single: dict):
    return product_data_single["options"]


@pytest.fixture
def dict_fixtures(product_data_single, images, variants, options):
    return {
        "product_data_single": product_data_single,
        "images": images,
        "variants": variants,
        "options": options,
    }
