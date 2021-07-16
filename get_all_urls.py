from bs4 import BeautifulSoup
from parse_all_cources import get_html
import browser_imitation


def get_all_exchange_adresses():
    url = "https://www.bestchange.ru/bitcoin-to-bitcoin.html"
    html_page = get_html(url)
    if html_page.status_code == 503:
        while html_page.status_code == 503:
            browser_imitation.browse(url)
            html_page = get_html(url)
        browser_imitation.close()
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
    cash_currencies = ["dollar-cash", "ruble-cash", "euro-cash", "hryvnia-cash", "belarus-cash", "tenge-cash", "pound-cash"]
    cash_adresses = {}
    for сurrency_to_pay in currencies:
        for currency_to_get in currencies:
            exchange_course = f"{сurrency_to_pay}-to-{currency_to_get}"
            all_exchange_adresses[exchange_course] = f"https://www.bestchange.ru/{exchange_course}.html"
            if currency_to_get in cash_currencies or сurrency_to_pay in cash_currencies:
                cash_adresses[exchange_course] = f"https://www.bestchange.ru/{exchange_course}.html"
    return all_exchange_adresses, cash_adresses
