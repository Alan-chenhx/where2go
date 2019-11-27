# coding=utf-8

import sender
import json
import time
from seleniumrequests import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

trip_data = dict()

def openDriver():
    global driver
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--incognito')
    options.add_argument('--log-level=3')
    driver = Chrome(options=options)


def getAttractionDetail():
    with open('data.json') as f:
        data = json.load(f)
    for city in data:
        attrs = data[city]
        for i,attr in enumerate(attrs):
            if attr['url'].find("-tours") != -1:
                del data[city][i]
                continue
            driver.get(attr['url'])
            if not driver.find_elements_by_class_name("attraction-metadata"):
                del data[city][i]
                continue
            html = driver.find_element_by_class_name('attraction-metadata').get_attribute('innerHTML')
            soup = BeautifulSoup(html, 'html.parser')
            asides = soup.findAll('aside')
            for aside in asides:
                if aside.div.text == "Contact":
                    data[city][i]['address'] = aside.p.text.replace("<br/>","")
                elif aside.div.text == "Price range":
                    data[city][i]['price'] = aside.p.text
            html = driver.find_element_by_class_name('desc-in').get_attribute('innerHTML')
            soup = BeautifulSoup(html, 'html.parser')
            data[city][i]['description'] = soup.find('blockquote').text.strip()
            with open('data.json', 'w') as outfile:
                json.dump(data, outfile)
        print(city)
    return data

def parseTripData(city, data):
    soup = BeautifulSoup(data, 'html.parser')
    tags = soup.div.attrs
    attraction = dict()
    attraction['name'] = tags['data-name']
    attraction['duration'] = tags['data-duration']
    attraction['url'] = tags['data-details-url']
    attraction['url'] = 'https://www.inspirock.com' + attraction['url'][attraction['url'].find('/united-states'):]
    attraction['photo'] = soup.find("div", {"class", "clickable-image"})
    attraction['photo'] = attraction['photo']["style"] if attraction['photo'] else ''
    attraction['rating'] = float(soup.find("span", {"class": "rating-with-count"}).text.strip())
    attraction['tag'] = list()
    for tag in soup.findAll('span', {"class": "tag"}):
        attraction['tag'].append(tag.text.strip())
    trip_data[city].append(attraction)


def openTripPlanner(city):
    while(True):
        try:
            driver.get(
                'https://trip-planner.visittheusa.com/')
            input_box = driver.find_element_by_id("home-planning-form").find_element_by_xpath(".//div[@class='destination']/input")
            input_box.send_keys(city)
            time.sleep(0.2)
            input_box.send_keys(Keys.ENTER)
            driver.find_element_by_class_name("calendar-input").click()
            time.sleep(0.2)
            driver.find_element_by_class_name("ui-datepicker-next").click()
            time.sleep(0.2)
            driver.find_element_by_class_name("dt-1575176400000").click()
            time.sleep(0.2)
            driver.find_element_by_class_name("dt-1580274000000").click()
            time.sleep(0.2)
            driver.find_element_by_class_name("plan-button").click()
            while(driver.current_url.find('/trip/')==-1):
                time.sleep(1)
            driver.get(driver.current_url[:-8]+'itinerary/list')
            element_present = EC.presence_of_element_located((By.CLASS_NAME, 'visit-row'))
            WebDriverWait(driver, 10).until(element_present)
            data = driver.find_elements_by_class_name("visit-row")
            for d in data:
                parseTripData(city, d.get_attribute("outerHTML"))
        except Exception as error:
            print(error)
            time.sleep(1)
            continue
        break


def closeDriver():
    driver.quit()

CITIES = ['Los Angeles','San Francisco','San Diego','Sacramento','San Jose','Irvine','Oakland','Long Beach','California City','Anaheim','Berkeley','Santa Monica','Palo Alto','Pasadena','Glendale','Fresno','Santa Ana','Oceanside','Bakersfield','Fremont','Carlsbad','Santa Barbara','Stockton','Newport Beach','Riverside','Oxnard','San Bernardino','Santa Rosa','Chula Vista','Sunnyvale','Torrance','Mountain View','Huntington Beach','Santa Cruz','Thousand Oaks','Burbank','Beverly Hills','Modesto','Santa Clarita','Garden Grove','Ontario','Fontana','Encinitas','Manhattan Beach','Santee','Temecula','Moreno Valley','San Mateo','Costa Mesa','Rancho Cucamonga']

if __name__ == '__main__':
    driver = []
    browser = []
    openDriver()
    # for city in CITIES:
    #     trip_data[city] = list()
    #     openTripPlanner(city)
    #     with open('data.json', 'w') as outfile:
    #         json.dump(trip_data, outfile)
    #     print(city)
    getAttractionDetail()

    closeDriver()
