from django.shortcuts import render
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from django.utils import timezone
from .models import CurrencyExchangeRate
import requests


def weather_bs4(request, mul: str):
    r = requests.get("https://weather.com/weather/monthly/l/5ead5bf0831e9c4adb7cc4a4f0f66264147a55a24823c075c67035cbfb30724b")
    text = r.text
    soup = BS(text, 'html.parser')
    weather_report = []
    day = int(mul) * soup.find('div', {'class': 'CalendarDateCell--tempHigh--3k9Yr'}).text
    weather_report.append({'day', day})
    night = int(mul) * soup.find('div', {'class': 'CalendarDateCell--tempLow--2WL7c'}).text
    weather_report.append({'night', night})
    date = int(mul) * soup.find('span', {'class': 'CalendarDateCell--date--JO3Db'}).text
    weather_report.append({'date', date})
    return render(request, 'weather.html', {'day': weather_report})


def currency_sel(request):
    options = Options()
    options.headless = True
    browser = webdriver.Chrome(options=options)
    browser.get('https://www.currenciesdirect.com/en/currency-tools/today-s-rate')
    sleep(3)
    currency = browser.find_elements_by_xpath("//tbody[@class='js-todaysrates-rows']").text
    browser.close()
    context = {'currency': currency}
    return render(request, 'currency.html', context=context)
