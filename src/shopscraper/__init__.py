__version__ = "0.0.4"
import logging

from shopscraper.api import read_json, scrape, scrape_to_json
from shopscraper.prod_objs import Image, Product, Variant

log = logging.getLogger("shopscraper")
