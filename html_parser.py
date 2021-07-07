from bs4 import BeautifulSoup
import requests
import browser_imitation


HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    "accept": "*/*"
}


def get_html(url, params=None):
    response = requests.get(url, headers=HEADERS, params=params)
    return response


def has_param(param):
    if param:
        return True


def get_content(html_page):
    try:
        soup = BeautifulSoup(html_page, "html.parser")
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
            rates_required_data[exchanger_name] = {
                "manual": has_param(exchanger_params.find(class_="manual")),
                "otherout": has_param(exchanger_params.find(class_="otherout")),
                "otherin": has_param(exchanger_params.find(class_="otherin")),
                "floating": has_param(exchanger_params.find(class_="floating")),
                "verifying": has_param(exchanger_params.find(class_="verifying")),
                "percent": has_param(exchanger_params.find(class_="percent")),
                "cardverify": has_param(exchanger_params.find(class_="cardverify")),
                "reg": has_param(exchanger_params.find(class_="reg")),
                "card2card": has_param(exchanger_params.find(class_="card2card")),
                "airplane": has_param(exchanger_params.find(class_="airplane")),
                "purse": has_param(exchanger_params.find(class_="purse")),
                "official": has_param(exchanger_params.find(class_="official")),
                "delay": has_param(exchanger_params.find(class_="delay")),
            }
        return rates_required_data

    except AttributeError:
        pass


def parse(exchange_adress):
    exchange_course, url = exchange_adress
    html_page = get_html(url)
    if html_page.status_code == 503:
        while html_page.status_code == 503:
            browser_imitation.browse(url)
            html_page = get_html(url)
        browser_imitation.close()
        rates_required_data = get_content(html_page.text)
        return exchange_course, rates_required_data
    else:
        rates_required_data = get_content(html_page.text)
        return exchange_course, rates_required_data
