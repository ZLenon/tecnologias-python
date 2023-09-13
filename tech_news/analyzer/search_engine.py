from tech_news.database import find_news


# Req 7
def search_by_title(title):
    print(title)
    noticias = find_news()
    novas_infos = list()
    for n in noticias:
        if title.lower() in n["title"].lower():
            novas_infos.append((n["title"], n["url"]))
    return novas_infos


# Req 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Req 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
