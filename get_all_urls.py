from bs4 import BeautifulSoup
from html_parser import get_html


def get_all_exchange_adresses():
    url = "https://www.bestchange.ru/bitcoin-to-bitcoin.html"
    html_page = get_html(url)
    soup = BeautifulSoup(html_page.text, "html.parser")
    curr_tab = soup.find("div", {"id": "curr_tab"})
    curr_tab_body = curr_tab.find("tbody")
    all_urls = curr_tab_body.find_all(class_="rc")
    currencies = ["bitcoin", ]
    for url in all_urls:
        url = url.find("a").get("href")
        if not url:
            continue
        сurrency = url.replace("https://www.bestchange.ru/bitcoin-to-", "").replace(".html", "")
        currencies.append(сurrency)
    all_exchange_adresses = {}
    for сurrency_to_pay in currencies:
        for currency_to_get in currencies:
            exchange_course = f"{сurrency_to_pay}-to-{currency_to_get}"
            all_exchange_adresses[exchange_course] = f"https://www.bestchange.ru/{exchange_course}.html"
    return all_exchange_adresses
