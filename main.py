import parse_all_cources
import parse_cash
import get_all_urls
from datetime import datetime
import threading


starttime = datetime.now()
exchange_adresses, cash_adresses = get_all_urls.get_all_exchange_adresses()
#parse_all_cources.parse_all_courses(cash_adresses)
parse_cash.parse_all_cash(cash_adresses)
