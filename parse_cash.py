import requests
from bs4 import BeautifulSoup
from connect_redis import redis_set_hash
import browser_imitation

HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "accept": "*/*"
}


def parse_all_cash(cash_adresses):
    for exchange_adress in cash_adresses.items():
        exchange_course, url = exchange_adress
        parse_cash(exchange_course, url)


def get_html(url, params=None):
    response = requests.get(url, headers=HEADERS, params=params)
    return response


def parse_cash(exchange_course, url):
    html_page = get_html(url).text
    soup = BeautifulSoup(html_page, "html.parser")
    content = soup.find(class_="content")
    text_field = content.find(class_="text")
    cities_block = text_field.find_all("p")[-1]
    cities_divs = cities_block.find_all("a")
    for city_div in cities_divs:
        city_url = city_div.get("href")
        city_rates_required_data = parse(city_url)
        city = city_url.split("-in-")[1].replace(".html", "")
        redis_set_hash(exchange_course, city, city_rates_required_data)
        print(f"{exchange_course} in {city} is done")


def get_content(html_page):
    try:
        soup = BeautifulSoup(html_page.text, "html.parser")
        rates_block = soup.find("div", {"id": "rates_block"})
        rates_table = rates_block.find("table", {"id": "content_table"})
        rates_table_entries = rates_table.find("tbody")
        rates_findings = rates_table_entries.find_all("tr")
        rates_required_data = {}

        for rate_findings in rates_findings:
            exchanger_params = rate_findings.find("td", class_="bj")
            if not exchanger_params:
                continue
            exchanger_name = exchanger_params.find("div", class_="ca").text
            exchange_values = rate_findings.find_all("td", class_="bi")
            rates_required_data[exchanger_name] = {
                "pay": exchange_values[0].find("div", class_="fs").text,
                "get": exchange_values[1].text,
                "reserve": rate_findings.find("td", class_="ar arp").text,
            }
        return rates_required_data

    except AttributeError:
        pass


def parse(url):
    html_page = get_html(url)
    if html_page.status_code == 503:
        while html_page.status_code == 503:
            browser_imitation.browse(url)
            html_page = get_html(url)
        browser_imitation.close()
        rates_required_data = get_content(html_page)
        return rates_required_data
    else:
        rates_required_data = get_content(html_page)
        return rates_required_data
