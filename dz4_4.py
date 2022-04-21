import requests


def currency_rates(kod):
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url)
    res_text = response.text

    # Разбор кода валюты
    start_kod = res_text.find("<CharCode>" + kod + "</CharCode>")
    end_kod = res_text.find("</Value>", start_kod)
    well = float(res_text[start_kod:end_kod][-7:-2].replace(',', '.'))

    # Разбор даты
    start_date = res_text.find("Date=")
    end_date = res_text.find("name", start_date)
    time = res_text[start_date:end_date][-12:-2]

    return [well, time]
