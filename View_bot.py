import webbrowser
import time
import os
import ipaddress
import requests
from lxml.html import fromstring
from itertools import cycle
import traceback


def main():    
    """proxies = get_proxies()
    proxy_pool = cycle(proxies)
    print(proxies)
    url = 'https://www.youtube.com/watch?v=w77JRCKVeb0&feature=youtu.be'
    for i in range(1,11):
        proxy = next(proxy_pool)
        print("Request #%d" %i)
        try:
            response = requests.get(url, proxies ={"http": proxy, "https":proxy})
        except:
            print("Skipping. Connection error")
    for ip in ipaddress.IPv4Network('192.168.0.0/24'):
        print(ip)"""
    webbrowser.open('https://www.youtube.com/watch?v=w77JRCKVeb0&feature=youtu.be', new=2)
    run = 'yes'
    mins = 0
    browserExe = 'tor.exe'
    if run == 'yes':
        while mins != 1:
            time.sleep(10)
            print("time is up")
            mins += 1
        else:
            mins -= 1
            os.system("taskkill /f /im "+browserExe)
            main()
        
def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies
main()
