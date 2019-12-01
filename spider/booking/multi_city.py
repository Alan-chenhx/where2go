from selenium import webdriver
import json
import time
import re
import request
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
CITIES = ['Los Angeles','San Francisco','San Diego','Sacramento','San Jose','Irvine','Oakland','Long Beach','California City','Anaheim','Berkeley','Santa Monica','Palo Alto','Pasadena','Glendale','Fresno','Santa Ana','Oceanside','Bakersfield','Fremont','Carlsbad','Santa Barbara','Stockton','Newport Beach','Riverside','Oxnard','San Bernardino','Santa Rosa','Chula Vista','Sunnyvale','Torrance','Mountain View','Huntington Beach','Santa Cruz','Thousand Oaks','Burbank','Beverly Hills','Modesto','Santa Clarita','Garden Grove','Ontario','Fontana','Encinitas','Manhattan Beach','Santee','Temecula','Moreno Valley','San Mateo','Costa Mesa','Rancho Cucamonga']
ans={}

for city in CITIES:
    option=webdriver.ChromeOptions()
    # option.add_argument('headless') 
    ans.setdefault(city,{})
    driver = webdriver.Chrome(executable_path="./chromedriver", port=0, options=None, service_args=None, desired_capabilities=None, service_log_path=None, chrome_options=option, keep_alive=True)
    # browser = webdriver.Chrome()
    
    # driver.get('https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggI46AdIM1gEaJMCiAEBmAExuAEZyAEM2AEB6AEB-AECiAIBqAIDuALK7ovvBcACAQ&sid=7ffb886c4c43c7ea81140ca5815ff720&tmpl=searchresults&checkin=2020-01-08&checkout=2020-01-09&class_interval=1&dest_id=20014181&dest_type=city&dtdisc=0&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&shw_aparth=1&slp_r_match=0&srpvid=0ff5a741f20c0064&ss=Los%20Angeles&ss_all=0&ssb=empty&sshis=0&top_ufis=1&rows=25&offset=725')
    driver.get('http://www.booking.com/')

    city_input = driver.find_element_by_name("ss")
    city_input.send_keys(city)
    time.sleep(1)
    driver.find_element_by_class_name('xp__dates-inner').click()
    time.sleep(1)
    calender=driver.find_element_by_css_selector("[class='bui-calendar__control bui-calendar__control--next']").click()
    time.sleep(0.2)
    calender=driver.find_element_by_css_selector("[class='bui-calendar__control bui-calendar__control--next']").click()
    time.sleep(0.2)
    calender=driver.find_element_by_css_selector("[class='bui-calendar__control bui-calendar__control--next']").click()

    # Feb
    row=driver.find_elements_by_tag_name('tr')
    date=row[2].find_elements_by_tag_name('td')
    date[3].click()
    time.sleep(0.2)
    row=driver.find_elements_by_tag_name('tr')
    date=row[2].find_elements_by_tag_name('td')
    date[4].click()
    time.sleep(0.2)
    driver.find_element_by_class_name('xp__button').click()
    url = driver.current_url
    ans[city].setdefault('url',url)
    while(1):
        soup = BeautifulSoup(driver.page_source, 'lxml')
        Hotels = soup.find_all(class_="sr-hotel__name")
        Score = soup.find_all(class_="bui-review-score__badge")
        Links = soup.find_all(class_="hotel_name_link url")
        for i in range(len(Hotels)):
            hotel_name=(re.sub(r'\n', '', Hotels[i].text))
            overall_score=(Score[i].text)
            ans[city].setdefault(hotel_name,{})
            ans[city][hotel_name].setdefault('overall_score',0)
            ans[city][hotel_name]['overall_score']=overall_score
            s="http://booking.com"+(re.sub(r'\n', '', Links[i].get('href')))
            driver2 = webdriver.Chrome(executable_path="./chromedriver", port=0, options=None, service_args=None, desired_capabilities=None, service_log_path=None, chrome_options=option, keep_alive=True)
            driver2.get(s)
            time.sleep(0.2)
            soup2 = BeautifulSoup(driver2.page_source, 'lxml')
            # driver2.find_element_by_css_selector("[class='span.hp_address_subtitle.js-hp_address_subtitle.jq_tooltip']").text
            address=soup2.find_all(class_='address address_clean')[0].text
            ans[city][hotel_name].setdefault('address','')
            ans[city][hotel_name]['address']=address
            price=soup2.find_all(class_='bui-price-display__value prco-ltr-center-align-helper prco-font16-helper')
            # print(price)
            ans[city][hotel_name].setdefault('price','')
            if(len(price)!=0):
                ans[city][hotel_name]['price']=price[0].text
            driver2.find_element_by_class_name('bui-review-score__badge').click()
            soup2 = BeautifulSoup(driver2.page_source, 'lxml')
            Scores = soup.find_all(class_="c-score-bar__score")
            rating_key=["Staff","Facilities","Cleanliness","Comfort","Value for money","Location","Free WiFi"]
            for i in range(len(Scores)):
                ans[city][hotel_name][rating_key[i]]=Scores[i].text
            driver2.quit()
        # driver.implicitly_wait(5)
        try:
            prev=driver.current_url
            driver.find_element_by_css_selector("[title='Next page']").click()
            # print('clicked')
            time.sleep(6)
        except:
            break 
        
        
    driver.quit()
    print(city)

    json=demjson.encode(ans)
    fo = open("city_url.json", "w")
    fo.write(json)
    fo.close()