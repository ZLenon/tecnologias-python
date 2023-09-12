import time
import requests
from parsel import Selector


# Req 1
def fetch(r):
    time.sleep(2)
    cabeçalho = {"user-agent": "Fake user-agent"}

    try:
        response = requests.get(r, headers=cabeçalho, timeout=5)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except requests.exceptions.Timeout:
        return None


# Req 2
def scrape_updates(r):
    x = Selector(text=r)
    n = x.css(".entry-title a::attr(href)").getall()
    return n


# Req 3
def scrape_next_page_link(r):
    x = Selector(text=r)
    n = x.css(".next.page-numbers")
    if n:
        y = n.css("::attr(href)").get()
        return y
    else:
        return None


# Req 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Req 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
