from bs4 import BeautifulSoup
import requests
from build_table import build_table


HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "accept": "*/*"
}


def get_html(url, params=None):
    response = requests.get(url, headers=HEADERS, params=params)
    return response


def has_param(param):
    if param:
        return "True"
    else:
        return "False"


def get_content(html_page):
    soup = BeautifulSoup(html_page, "html.parser")
    rates_block = soup.find("div", {"id": "rates_block"})
    rates_table = rates_block.find("table", {"id": "content_table"})
    rates_table_entries = rates_table.find("tbody")
    rates_findings = rates_table_entries.find_all("tr")
    rates_required_data = []

    for rate_findings in rates_findings:
        exchanger_params = rate_findings.find("td", class_="bj")
        exchange_values = rate_findings.find_all("td", class_="bi")
        if not (exchanger_params and exchange_values):
            continue

        rates_required_data.append((
            exchanger_params.find("div", class_="ca").text,
            exchange_values[0].find("div", class_="fs").text,
            exchange_values[1].text,
            has_param(exchanger_params.find(class_="manual")),
            has_param(exchanger_params.find(class_="overout")),
            not has_param(exchanger_params.find(class_="floating")),
            has_param(exchanger_params.find(class_="verifying")),
            has_param(exchanger_params.find(class_="percent"))
        ))
    table_headers = ("Обменник", "Отдаете", "Получаете", "Ручной режим", "Работа со сторонними платежыми системами", "Фиксация курса на момент заявки", "Верификация", "Комиссия")
    results_count = 15
    table_title = "Топ-15 обменников"
    print(build_table(
        table_headers,
        rates_required_data,
        results_count,
        table_title
        )
    )


def parse():
    url = input("Введите url страницы для парсинга: ")
    html_page = get_html(url)
    if html_page.status_code == 200:
        get_content(html_page.text)
    else:
        print("Error")


parse()
