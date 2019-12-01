import demjson
from selenium import webdriver
import json
import requests
import time
import re
import request
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
def Headers():
    headers = {
        "Cookie":"ors_js=1; _ga=GA1.2.1617144318.1571974067; _gid=GA1.2.309460805.1571974067; _gcl_au=1.1.1830293888.1571974067; header_signin_prompt=1; BJS=-; zz_cook_tms_seg1=2; zz_cook_tms_ep=1; zz_cook_tms_seg3=7; cto_lwid=321ebeef-3d25-4b1d-8020-5e88310fcf51; has_preloaded=1; lang_signup_prompt=1; zz_cook_tms_hlist=182230; zz_cook_tms_ed=1; esadm=02UmFuZG9tSVYkc2RlIyh9YbxZGyl9Y5%2BPCobNw1iDkcc6eXKrqXbQASR7fbBGE93Ejqncb6XpoGM%3D; he=02UmFuZG9tSVYkc2RlIyh9YbxZGyl9Y5%2BPCobNw1iDkcfLCP57fWXVSpw%2B%2FuCxrDm%2F1J39VibohdM%3D; _fbp=fb.1.1571977797045.506872060; _ym_uid=1571977797460279212; _ym_d=1571977797; _hjid=e5db017d-82ce-4a9d-80e8-37aca77d00fa; ecid=AIRzGOD26RGrA20wyK76bQ03; header_joinapp_prompt_retargeting=1; b=%7B%22countLang%22%3A4%7D; _gcl_aw=GCL.1571980190.EAIaIQobChMIg__0xNK25QIVTZyzCh0XFAIjEAAYASAAEgKHK_D_BwE; _gac_UA-116109-18=1.1571980190.EAIaIQobChMIg__0xNK25QIVTZyzCh0XFAIjEAAYASAAEgKHK_D_BwE; utag_main=v_id:016e00f4b5490016f53190ec7a410208500ee07d009dc$_sn:2$_ss:0$_st:1571981993944$4split:1$4split2:0$ses_id:1571976336773%3Bexp-session$_pn:24%3Bexp-session; _tq_id.TV-451827-1.3b4c=fff03b8f948e0a98.1571974069.0.1571980194..; 11_srd=%7B%22features%22%3A%5B%7B%22id%22%3A9%7D%5D%2C%22score%22%3A3%2C%22detected%22%3Afalse%7D; bkng=11UmFuZG9tSVYkc2RlIyh9YfDNyGw8J7nzPnUG3Pr%2Bfv4g0Hr7%2FBnEed8jLrUVv22h1Ugldo%2F5wdQZMVYkyDCf6AV9DZ6zP7nfZ05x%2Fnv6TxOZS26FNfHkVC16HfPVdGioxLA2sY6zLK%2FkcxGhzRJ9pfJIOMZChMG7bkuv4CxBegwPZPD5CmvNccoQg82zr31dYOTiE0s4ArOgxZB7CSpLsA%3D%3D; lastSeen=1571981363569",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    }
    return headers
def getHTMLText(url, **kwargs):
    try:
        r = requests.get(url, **kwargs)
        r.raise_for_status()
        return r.text
    except:
        return None


CITIES = ['Los Angeles','San Francisco','San Diego','Sacramento','San Jose','Irvine','Oakland','Long Beach','California City','Anaheim','Berkeley','Santa Monica','Palo Alto','Pasadena','Glendale','Fresno','Santa Ana','Oceanside','Bakersfield','Fremont','Carlsbad','Santa Barbara','Stockton','Newport Beach','Riverside','Oxnard','San Bernardino','Santa Rosa','Chula Vista','Sunnyvale','Torrance','Mountain View','Huntington Beach','Santa Cruz','Thousand Oaks','Burbank','Beverly Hills','Modesto','Santa Clarita','Garden Grove','Ontario','Fontana','Encinitas','Manhattan Beach','Santee','Temecula','Moreno Valley','San Mateo','Costa Mesa','Rancho Cucamonga']
ans={}

for city in CITIES:
    option=webdriver.ChromeOptions()
    # option.add_argument('headless') 
    ans.setdefault(city,{})
    driver = webdriver.Chrome(executable_path="./chromedriver", port=0, options=None, service_args=None, desired_capabilities=None, service_log_path=None, chrome_options=option, keep_alive=True)
    # browser = webdriver.Chrome()
    headers = Headers()
    # driver.get('https://www.booking.com/searchresults.en-us.html?label=gen173nr-1FCAEoggI46AdIM1gEaJMCiAEBmAExuAEZyAEM2AEB6AEB-AECiAIBqAIDuAL-j43vBcACAQ&sid=8bcd1b3a88930b9b7889376c71d06371&tmpl=searchresults&ac_click_type=b&ac_position=0&checkin_month=2&checkin_monthday=5&checkin_year=2020&checkout_month=2&checkout_monthday=6&checkout_year=2020&class_interval=1&dest_id=20014181&dest_type=city&dtdisc=0&from_sf=1&group_adults=2&group_children=0&iata=LAX&inac=0&index_postcard=0&label_click=undef&no_rooms=1&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=index&src_elem=sb&srpvid=8e3022c3551f003c&ss=Los%20Angeles%2C%20California%2C%20USA&ss_all=0&ss_raw=Los%20Angeles&ssb=empty&sshis=0&top_ufis=1&rows=25&offset=375')
    driver.get('http://www.booking.com/')

    city_input = driver.find_element_by_name("ss")
    city_input.send_keys(city)
    time.sleep(2)
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
    # element_present = driver.presence_of_element_located((By.CLASS_NAME, 'xp__button'))
    # WebDriverWait(driver, 10).until(element_present)
    driver.find_element_by_class_name('xp__button').click()
    url = driver.current_url
    ans[city].setdefault('url',url)
    i=0
    while(1):
        
        
        soup = BeautifulSoup(driver.page_source, 'lxml')
        i+=1
        page=soup.find_all(class_="bui-u-inline")[-1].text
        # if(i>)
        page=int(page)
        if(i>page):
            break
        Hotels = soup.find_all(class_="sr-hotel__name")
        Score = soup.find_all(class_="bui-review-score__badge")
        Links = soup.find_all(class_="hotel_name_link url")
        for i in range(len(Hotels)):
            hotel_name=(re.sub(r'\n', '', Hotels[i].text))
            # overall_score=(Score[i].text)
            ans[city].setdefault(hotel_name,{})
            ans[city][hotel_name].setdefault('overall_score',0)
            # ans[city][hotel_name]['overall_score']=overall_score
            s="http://booking.com"+(re.sub(r'\n', '', Links[i].get('href')))
            # print(s)
            r = getHTMLText(s, headers=headers)
            # print(response.text)
            # driver2 = webdriver.Chrome(executable_path="./chromedriver", port=0, options=None, service_args=None, desired_capabilities=None, service_log_path=None, chrome_options=option, keep_alive=True)
            # driver2.get(s)
            # time.sleep(0.2)
            soup2 = BeautifulSoup(r, 'lxml')
            # print(soup2)
            # driver2.find_element_by_css_selector("[class='span.hp_address_subtitle.js-hp_address_subtitle.jq_tooltip']").text
            address=soup2.find_all(class_='hp_address_subtitle js-hp_address_subtitle jq_tooltip')[0].text
            ans[city][hotel_name].setdefault('address','')
            ans[city][hotel_name]['address']=address
            # print(address)
            price=soup2.find_all(class_='bui-price-display__value prco-ltr-center-align-helper prco-font16-helper')
            # print(price)
            ans[city][hotel_name].setdefault('price','')
            if(len(price)!=0):
                ans[city][hotel_name]['price']=price[0].text
            try:
                # driver2.find_element_by_class_name('bui-review-score__badge').click()
                # soup2 = BeautifulSoup(driver2.page_source, 'lxml')
                # overall_score=soup2.find_all(class_="bui-review-score__badge").text
                # ans[city][hotel_name]['overall_score']=overall_score
                Scores = soup2.find_all(class_="c-score-bar__score")
                rating_key=["Staff","Facilities","Cleanliness","Comfort","Value for money","Location","Free WiFi"]
                for i in range(len(Scores)):
                    ans[city][hotel_name][rating_key[i]]=Scores[i].text
            except:
                print('fail')
                pass
            # driver2.quit()
            # print(hotel_name)
            # print(ans)    
        # driver.implicitly_wait(5)
        try:
            driver.find_element_by_css_selector("[title='Next page']").click()
            # print('clicked')
            time.sleep(6)
            print(1)
        except:
            break 
        
        
    driver.quit()
    print(city)

    json=demjson.encode(ans)
    fo = open("city_url.json", "w")
    fo.write(json)
    fo.close()