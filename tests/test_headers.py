from __future__ import annotations

import random

from shopscraper import headers


def test_random_user_agent():
    random.seed(5)
    exp_result = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
    assert headers._random_user_agent() == exp_result


def test_get_headers():
    random.seed(5)
    exp_result = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-us,en;q=0.5",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Accept-Encoding": "gzip, deflate",
    }
    assert headers.get_headers() == exp_result
