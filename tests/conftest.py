import json
import pathlib

import pytest


def pytest_addoption(parser):  # https://docs.pytest.org/en/6.2.x/example/simple.html
    parser.addoption("--run-slow", action="store_true", default=False, help="run slow tests")


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--run-slow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --run-slow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)


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
