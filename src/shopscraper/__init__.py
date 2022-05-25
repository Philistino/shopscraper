import logging
from logging import NullHandler

from shopscraper.api import read_json, scrape, scrape_to_json
from shopscraper.prod_objs import Image, Product, Variant

# Set default logging handler to avoid "No handler found" warnings.
logging.getLogger(__name__).addHandler(NullHandler())

# ... Clean up.
del NullHandler
