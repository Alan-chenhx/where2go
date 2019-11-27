import requests
import re
from bs4 import BeautifulSoup
import json
import demjson
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
ans={}
base_url='https://trip-planner.visittheusa.com/united-states/'
def main():
    #input url
    CITIES = ['Los Angeles','San Francisco','San Diego','Sacramento','San Jose','Irvine','Oakland','Long Beach','Anaheim','Berkeley','Santa Monica','Palo Alto','Pasadena','Fresno','Santa Ana','Oceanside','Bakersfield','Fremont','Carlsbad','Santa Barbara','Stockton','Newport Beach','Riverside','Oxnard','San Bernardino','Santa Rosa','Chula Vista','Sunnyvale','Torrance','Mountain View California','Huntington Beach','Santa Cruz','Thousand Oaks','Burbank','Beverly Hills','Modesto','Santa Clarita','Garden Grove','Fontana','Encinitas','Manhattan Beach','Temecula','Moreno Valley','San Mateo','Costa Mesa','Rancho Cucamonga']
    for city in CITIES:
        url=base_url+city
        url=url.replace(" ", "-")
        # print(url)
            # url = 'https://www.booking.com/hotel/us/economy-inn-san-francisco.html?label=gen173nr-1DCAQoggI4ogRIMVgEaJMCiAEBmAExuAEXyAEM2AED6AEB-AEDiAIBqAIDuALWu8rtBcACAQ&sid=7ffb886c4c43c7ea81140ca5815ff720&all_sr_blocks=18129301_104071734_0_0_0&checkin=2019-10-29&checkout=2019-11-02&dest_id=20015732&dest_type=city&group_adults=2&group_children=0&hapos=1&highlighted_blocks=18129301_104071734_0_0_0&hpos=1&no_rooms=1&sr_order=popularity&srepoch=1571986902&srpvid=9f6b316ba3fc014d&ucfs=1&from=searchresults;highlight_room=#tab-reviews'
            # print(url
        response = requests.get(url)
        datas = response.text
        headers = Headers()
        # kv['offset']=i*25

        r = getHTMLText(url,headers=headers)
        # print(data)
        soup = BeautifulSoup(datas, 'lxml')
        # print(soup)
        tree = soup.find_all(class_="where-in-world")
        # print(tree)
        names=tree[0].find_all(property="name")
        cur=ans
        for index,i in enumerate(names):
            cur.setdefault(i.text,{})
            cur=cur[i.text]
        print(city)
    json=demjson.encode(ans)
    fo = open("data.json", "w")
    fo.write(json)
    fo.close()
main()