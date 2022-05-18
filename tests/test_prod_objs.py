from shopscraper import prod_objs


def test_create_product_obj_from_file(product_data_single: dict):
    expected_dict = product_data_single.copy()
    assert prod_objs.Product(**expected_dict) == prod_objs.product_factory(
        product_data_single, include_html=True
    )


def test_create_product_obj_from_file_no_html(product_data_single: dict):
    expected_dict = product_data_single.copy()
    expected_dict["body_html"] = ""
    assert prod_objs.Product(**expected_dict) == prod_objs.product_factory(
        product_data_single, include_html=False
    )
