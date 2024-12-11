from bs4 import BeautifulSoup
import requests

URL = "https://burgerkingrus.ru/actions"

async def fetch_promotions():
    """
    Парсер сайта с акциями.
    Возвращает список акций.
    """
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Парсим акции
    articles = soup.find_all("article", class_="sc-wlfkge-1")
    promotions = []
    for article in articles:
        title = article.find("h1", class_="title").get_text(strip=True)
        description = article.find("div", class_="description").p.get_text(strip=True)
        image_url = article.find("img", class_="image")["src"]
        promotions.append({"title": title, "description": description, "image_url": image_url})
    return promotions
