import requests
import pandas as pd
from bs4 import BeautifulSoup


keyword = "kit_ventoinhas"

url = f"https://lista.mercadolivre.com.br/{keyword}"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    search_result = soup.find_all("div", class_="ui-search-result")

    data = []
    for result in search_result:
        link = result.find("a", class_="ui-search-link").text.strip()
        title = result.find("h2", class_="ui-search-item__title").text.strip()
        price = result.find("span", class_="andes_money_ammount__fraction").text.strip()
        brand = result.find("span", class_="ui-search-item_title")

        if link:
            link = link.get("href")

        data.append({"Title": title, "Price": price, "Brand": brand, "Link": link})

    print(data)

else:
    print("error")
