import json
import pathlib

import pytest

from shopscraper import api, json_handler, prod_objs, scraper


@pytest.fixture(scope="module")
def test_domain():
    return "www.shopbeergear.com"


@pytest.fixture()
def temp_dir(tmp_path: pathlib.Path):
    d = tmp_path / "sub"
    d.mkdir()
    return d


@pytest.mark.slow
def test_scrape_to_json(
    test_domain: str, temp_dir: pathlib.Path, product_data_single: dict
):
    file_path = temp_dir.joinpath("products.json")
    api.scrape_to_json(
        test_domain,
        file_path,
        items_per_page=2,
        max_pages=2,
        include_html=False,
    )
    assert file_path.exists()
    result = json.loads(file_path.read_text())
    assert len(result) == 4
    assert sorted(result[0].keys()) == sorted(product_data_single.keys())


@pytest.mark.parametrize("include_html", [True, False])
def test_read_json(include_html, temp_dir: pathlib.Path, products: list[dict]):
    file_path = temp_dir.joinpath("products.json")
    json_handler.save_json(products, file_path, include_html=include_html)
    results = api.read_json(file_path, include_html=include_html)
    expected = (
        prod_objs.product_factory(i, include_html=include_html)
        for i in products
    )
    for result, expect in zip(results, expected):
        assert result == expect
