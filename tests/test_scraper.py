import json

import pytest
import requests

from shopscraper import scraper


def test_validate_integer_arg():
    assert 2 == scraper._validate_integer_arg(2)
    with pytest.raises(ValueError):
        scraper._validate_integer_arg("a")
        scraper._validate_integer_arg("2.1")


def test_construct_url():
    assert "https://bingo.com/products.json?limit=2&page=1" == scraper._construct_url(
        "bingo.com", 2, 1
    )


@pytest.mark.slow
def test_request_json():
    expected = {
        "args": {"foo1": "bar1", "foo2": "bar2"},
        "url": "https://postman-echo.com/get?foo1=bar1&foo2=bar2",
    }
    returned = scraper._request_json(expected["url"])
    assert expected["args"] == returned["args"]
    assert expected["url"] == returned["url"]


def test_request_json_exception():
    with pytest.raises(requests.JSONDecodeError):
        scraper._request_json("https://www.amazon.com")


@pytest.mark.slow
def test_yield_product_dicts(product_data_single: dict):
    """will fail if dict keys change"""
    domain = "www.shopbeergear.com"
    returned = list(scraper.yield_product_dicts(domain, 2, 2))
    assert len(returned) == 4
    assert product_data_single.keys() == returned[0].keys()
    assert product_data_single["images"][0].keys() == returned[0]["images"][0].keys()
    assert product_data_single["variants"][0].keys() == returned[0]["variants"][0].keys()
    assert product_data_single["options"][0].keys() == returned[0]["options"][0].keys()
