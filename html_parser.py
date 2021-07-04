from bs4 import BeautifulSoup
import requests
from urllib.parse import urlsplit
from connect_redis import redis_set_hash


HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "accept": "*/*"
}


def get_html(url, params=None):
    response = requests.get(url, headers=HEADERS, params=params)
    return response


def fetch_exchange_course(url):
    path = urlsplit(url).path
    exchange_course = path.replace(".html", "").replace("/", "")
    return exchange_course


def has_param(param):
    if param:
        return param.text


def get_content(html_page):
    soup = BeautifulSoup(html_page, "html.parser")
    rates_block = soup.find("div", {"id": "rates_block"})
    rates_table = rates_block.find("table", {"id": "content_table"})
    rates_table_entries = rates_table.find("tbody")
    rates_findings = rates_table_entries.find_all("tr")
    rates_required_data = {}

    for rate_findings in rates_findings:
        exchanger_params = rate_findings.find("td", class_="bj")
        exchange_values = rate_findings.find_all("td", class_="bi")
        if not (exchanger_params and exchange_values):
            continue
        exchanger_name = exchanger_params.find("div", class_="ca").text
        rates_required_data[exchanger_name] = {
            "pay": exchange_values[0].find("div", class_="fs").text,
            "get": exchange_values[1].text,
            "manual": has_param(exchanger_params.find(class_="manual")),
            "overout": has_param(exchanger_params.find(class_="overout")),
            "floating": has_param(exchanger_params.find(class_="floating")),
            "selfverify": has_param(exchanger_params.find(class_="verifying")),
            "percent": has_param(exchanger_params.find(class_="percent")),
            "cardverify": has_param(exchanger_params.find(class_="cardverify")),
            "registration": has_param(exchanger_params.find(class_="reg"))
        }

    return rates_required_data


def parse():
    url = input("Введите url страницы для парсинга: ")
    html_page = get_html(url)
    if html_page.status_code == 200:
        rates_required_data = get_content(html_page.text)
        exchange_course = fetch_exchange_course(url)
        print(exchange_course)
        redis_set_hash(exchange_course, rates_required_data)
    else:
        print("Error")


parse()
