import re
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
def scrape_news(r):
    x = Selector(text=r)
    endereco = x.css('link[rel="canonical"]::attr(href)').get()
    titulo = x.css("h1.entry-title::text").get().strip("\xa0")
    data = x.css(".meta-date::text").get()
    escritor = x.css(".author a::text").get()
    temp_leitura = int(x.css(".meta-reading-time::text").get().split(" ")[0])
    sumario = x.css(".entry-content p").get()
    sumario = re.sub("<.*?>", "", sumario).strip()
    categoria = x.css(".label::text").get()
    obj_final = {
        "url": endereco,
        "title": titulo,
        "timestamp": data,
        "writer": escritor,
        "reading_time": temp_leitura,
        "summary": sumario,
        "category": categoria,
    }
    return obj_final


# Req 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
