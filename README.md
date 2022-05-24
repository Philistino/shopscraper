# ShopScraper
[![Supported Python versions](https://img.shields.io/pypi/pyversions/shopscraper)](https://pypi.org/project/shopscraper/)
[![Build status](https://img.shields.io/github/workflow/status/Philistino/shopscraper/merge-to-main)](https://img.shields.io/github/workflow/status/Philistino/shopscraper/merge-to-main)
[![License](https://img.shields.io/github/license/Philistino/shopscraper)](https://img.shields.io/github/license/Philistino/shopscraper)

ShopScraper is a thin python wrapper for Shopify webshop product APIs used to scrape information from online stores. Every Shopify webshop has a "hidden" api with access to all of the store's products. This python package uses the requests library to grab the product information and return objects representing each product. There are also convenience functions for saving to and reading from a JSON file.

```python
>>> import shopscraper
>>>
>>> products = shopscraper.scrape("bjjfanatics.com", include_html=False, items_per_page=2, max_pages=1)
>>> type(products)
<class 'generator'>
>>> for product in products:
>>>    print(product)
id=6706690981986, 
title='New Wave Jiu Jitsu: Side Attacks - Building a Devastating Side Control System by John Danaher'
handle='new-wave-jiu-jitsu-side-attacks-building-a-devastating-side-control-system-by-john-danaher',
body_html='',
published_at=datetime.datetime(2022, 5, 18, 8, 2, 9, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 
created_at=datetime.datetime(2022, 5, 4, 23, 14, 55, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 
updated_at=datetime.datetime(2022, 5, 18, 11, 55, 59, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 
vendor='John Danaher', 
product_type='COMBO', 
tags=['Facebook', 'Fighter_John Danaher', 'MC_Side_Control_Attacks', 'New', 'new_and_popular', 'Show_More_App'], 
variants=[
    Variant(
        id=39769726582882, 
        title='Default Title', 
        option1='Default Title', 
        option2=None, 
        option3=None, 
        sku='JDNWJJSA-01', 
        requires_shipping=False, 
        taxable=True, 
        featured_image=None, 
        available=True, 
        price=19700, 
        grams=0, 
        compare_at_price=None, 
        position=1, 
        product_id=6706690981986, 
        created_at=datetime.datetime(2022, 5, 4, 23, 14, 55, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 
        updated_at=datetime.datetime(2022, 5, 18, 11, 55, 15, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000)))
    )
]
images=[
    Image(
        id=28542700257378, 
        created_at=datetime.datetime(2022, 5, 4, 23, 14, 55, 
        tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 
        position=1, 
        updated_at=datetime.datetime(2022, 5, 4, 23, 14, 57, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000))), 
        product_id=6706690981986, 
        variant_ids=[], 
        src='https://cdn.shopify.com/s/files/1/1800/2299/products/JohnDanaher_NewWaveJiu-Jitsu-SideAttacks_CoverFRONT.jpg?v=1651720497', 
        width=1631, 
        height=2194
    ),
]
options=[
    Options(
        name='Title', 
        position=1, 
        values=['Default Title']
    )
]


```


## Installation

ShopScraper is available on PyPI:

```console
$ python -m pip install shopscraper
```

ShopScraper officially supports Python 3.9+.


# Usage

The 'scrape' and 'read_json' functions yield product objects with lists of Variant, Image, and Options objects.

```python

class Image:
    """
    Attributes:
        id (int): image id
        created_at (datetime.datetime): datetime object of when image was created
        position (int): position of image in product
        updated_at (datetime.datetime): datetime object of when image was last updated
        product_id (int): product id associated with the image
        variant_ids (list[int]): list of variant ids associated with the image
        src (str): url to image
        width (int): width of image in pixels
        height (int): height of image in pixels
    """

class Options:
    """
    Attributes:
        name (str): name of option
        position (int): position of option in product
        values (list[Any]): list of values for option
    """


class Variant:
    """
    Attributes:
        id (int): variant id
        title (str): title of variant
        option1 (str): first option of variant
        option2 (str): second option of variant
        option3 (str): third option of variant
        sku (Optional[str]): sku of variant
        requires_shipping (bool): whether variant requires shipping
        taxable (bool): whether variant is taxable
        featured_image (Image): featured image of variant
        price (float): price of variant
        grams (int): weight of variant in grams
        compare_at_price (Optional(float)): compare at price of variant
        position (int): position of variant in product
        product_id (int): product id associated with the variant
        created_at (datetime.datetime): datetime object of when variant was created
        updated_at (datetime.datetime): datetime object of when variant was last updated
    """


class Product:
    """
    Attributes:
        id (int): product id
        title (str): name of product
        handle (str): url safe name of product
        body_html (str): description of product (html)
        published_at (datetime.datetime): date product was published
        created_at (datetime.datetime): date product was created
        updated_at (datetime.datetime): date product was last updated
        vendor (str): name of product vendor
        product_type (str): type of product
        tags (list[str]): tags associated with product
        variants (list[Variants]): list of variants for product
        images (list[Image]): list of images for product
        options (list[Options]): list of options for product
    """
```

The 'scrape' function yields product objects:
```python
>>> import shopscraper
>>>
>>> products = shopscraper.scrape("bjjfanatics.com")
>>> type(products)
<class 'generator'>
```

The 'scrape_to_json' function saves the scraped data to the specified file path:
```python
>>> import shopscraper
>>>
>>> save_path = shopscraper.scrape_to_json("bjjfanatics.com", "C:\\scraped_data.json")
>>> type(save_path)
<class 'pathlib.Path'>
```

The 'read_json' function reads the saved json file and yields Product objects:
```python
>>> import shopscraper
>>>
>>> products = shopscraper.read_json("C:\\scraped_data.json")
>>> type(products)
<class 'generator'>
```

Note that both functions that provide product objects are generators, which are more memory efficient than lists but can only be iterated over one time. If you want to use the product objects in more than one operation, accumulate them into a list:
```python
>>> import shopscraper
>>>
>>> products = shopscraper.read_json("C:\\scraped_data.json")
>>> product_list = list(products)
>>> len(product_list)
200
>>> combo_products = [i for i in product_list if i.product_type == "COMBO"]
>>> len(combo_products)
10
```

