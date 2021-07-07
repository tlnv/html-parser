from bs4 import BeautifulSoup
from html_parser import get_html
import browser_imitation


def get_all_exchange_urls():
    url = "https://www.bestchange.ru/bitcoin-to-bitcoin.html"
    html_page = get_html(url)
    if html_page.status_code == 503:
        browser_imitation.browse()
    else:
        soup = BeautifulSoup(html_page.text, "html.parser")
        curr_tab = soup.find("div", {"id": "curr_tab"})
        curr_tab_body = curr_tab.find("tbody")
        all_urls = curr_tab_body.find_all(class_="rc")
        courses = ["bitcoin", ]
        for url in all_urls:
            url = url.find("a").get("href")
            if not url:
                continue
            course = url.replace("https://www.bestchange.ru/bitcoin-to-", "").replace(".html", "")
            courses.append(course)
        all_exchange_urls = []
        for course_to_pay in courses:
            for cource_to_get in courses:
                all_exchange_urls.append(f"https://www.bestchange.ru/{course_to_pay}-to-{cource_to_get}.html")
        return(all_exchange_urls)
