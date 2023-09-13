from tech_news.database import find_news, db
from datetime import datetime


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
    try:
        hora = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")

        horario = {"timestamp": hora}
        infos = {"_id": 99, "title": 99, "url": 99}
        r = db.news.find(horario, infos)

        return [(news["title"], news["url"]) for news in r]
    except ValueError:
        raise ValueError("Data inválida")


# Req 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    raise NotImplementedError
