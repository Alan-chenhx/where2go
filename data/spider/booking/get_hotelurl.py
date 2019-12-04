import requests
import re
from bs4 import BeautifulSoup

def SearchInfo():
    kv = {
        'city':'20015732',
        'checkin_year':'2019',
        'checkin_month':'10',
        'checkin_monthday':'29',
        'checkout_year':'2019',
        'checkout_month':'11',
        'checkout_monthday':'2',
        'offset':'0',
    }
    return kv

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

def main():
    #input url
    url = 'https://www.booking.com/searchresults.en-us.html?'
    for i in range(10):
        kv = SearchInfo()
        headers = Headers()
        try:
            kv['offset']=i*25
            r = getHTMLText(url, params=kv, headers=headers)
            soup = BeautifulSoup(r, 'lxml')
            Hotels = soup.find_all(class_="sr-hotel__name")
            Score = soup.find_all(class_="bui-review-score__badge")
            Links = soup.find_all(class_="hotel_name_link url")
            # print("page %s" %(i+1))
            # for name in Hotels:
            #     print(re.sub(r'\n', '', name.text))
            # # for num in Score:
            # print(Score[2].text)
            # print(len(Hotels))
            for i in range(len(Hotels)):
                print(re.sub(r'\n', '', Hotels[i].text))
                print(Score[i].text)
                s="booking.com"+Links[i].get('href')
                print("https://www.booking.com", end='')
                print(re.sub(r"(?<=#).*",'tab-reviews',(re.sub(r'\n', '', Links[i].get('href')))))
               
        except:
            continue

main()