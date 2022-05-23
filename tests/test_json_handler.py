from __future__ import annotations

import json
import pathlib

import pytest

import shopscraper
from shopscraper import json_handler, prod_objs


@pytest.fixture()
def temp_dir(tmp_path: pathlib.Path):
    d = tmp_path / "sub"
    d.mkdir()
    return d


@pytest.fixture
def temp_file(temp_dir: pathlib.Path):
    f = temp_dir.joinpath("test.json")
    f.touch(exist_ok=True)
    return f


@pytest.mark.parametrize("include_html", [True, False])
def test_save_json(include_html, temp_file: pathlib.Path, products: list[dict]):
    json_handler.save_json(products, temp_file, include_html)
    results = json.loads(temp_file.read_text())
    assert len(results) == len(products)
    for product, result in zip(products, results):
        expected = product.copy()
        expected["body_html"] = product["body_html"] if include_html else ""
        assert sorted(result.keys()) == sorted(expected.keys())
        assert result["body_html"] != "" if include_html else result["body_html"] == ""
        assert result["body_html"] == expected["body_html"]


@pytest.mark.parametrize("include_html", [True, False])
def test_read_json(include_html, temp_dir: pathlib.Path, products: list[dict]):
    file_path = temp_dir.joinpath("products.json")
    json_handler.save_json(products, file_path, include_html=include_html)
    results = shopscraper.read_json(file_path, include_html=include_html)
    expected = (prod_objs.product_factory(i, include_html=include_html) for i in products)
    for result, expect in zip(results, expected):
        assert result == expect
