import json
from datetime import datetime
from pathlib import Path

import pytest

# from bjjorganizer import shopscraper
import shopscraper


@pytest.fixture(scope="module")
def test_domain():
    return "www.shopbeergear.com"


# @pytest.fixture(scope="session")
# def temp_dir(tmp_path_factory: Path) -> Path:
#     return tmp_path_factory.mktemp("test_shopscraper")


# @pytest.mark.slow
# def test_request_data_flow_control(test_domain):

#     assert (
#         len(
#             list(
#                 shopscraper._request_data_flow_control(
#                     test_domain, items_per_page=2, max_pages=2
#                 )
#             )
#         )
#         == 4
#     )


# @pytest.mark.slow
# def test_keys_in_response(
#     product_data_single: dict, json_response: dict[list[dict]]
# ):
#     assert product_data_single.keys() == json_response["products"][0].keys()

#     for key in ("images", "variants", "options"):
#         assert (
#             product_data_single[key][0].keys()
#             == json_response["products"][0][key][0].keys()
#         )


# @pytest.mark.slow
# def test_create_product_obj_from_web(test_domain: str):
#     assert (
#         len(
#             list(shopscraper.scrape(test_domain, items_per_page=2, max_pages=2))
#         )
#         == 4
#     )


# @pytest.mark.slow
# def test_scrape_to_json(
#     test_domain: str, temp_dir: Path, product_data_single: dict
# ):
#     file_path = temp_dir.joinpath("products.json")
#     shopscraper.scrape_to_json(
#         test_domain,
#         file_path,
#         items_per_page=2,
#         max_pages=2,
#         include_html=False,
#     )
#     assert file_path.exists()
#     result = json.loads(file_path.read_text())
#     assert len(result) == 4
#     assert sorted(result[0].keys()) == sorted(product_data_single.keys())


# @pytest.mark.parametrize("include_html", [True, False])
# def test_read_json(include_html, temp_dir: Path, products: list[dict]):
#     file_path = temp_dir.joinpath("products.json")
#     shopscraper._write_products_to_json(
#         products, file_path, include_html=include_html
#     )
#     results = shopscraper.read_json(file_path, include_html=include_html)
#     expected = (
#         shopscraper._create_product_obj(i, include_html=include_html)
#         for i in products
#     )
#     for result, expect in zip(results, expected):
#         assert result == expect
