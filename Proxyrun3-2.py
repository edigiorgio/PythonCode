import random, time, requests
from selenium import webdriver
from selenium.webdriver.common.proxy import *
from bs4 import BeautifulSoup

USER_AGENTS_FILE = './user_agents.txt'
RUNNING = True

def LoadUserAgents(uafile = USER_AGENTS_FILE):
    uas = []
    with open(uafile, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[0:-1-1])
    random.shuffle(uas)
    return uas

uas = LoadUserAgents()

while RUNNING == True:
    address = []
    
    ip = []
    
    port = []
    
    response = requests.get('https://www.sslproxies.org')
    
    soup = BeautifulSoup(response.content, "html.parser")
    
    rows = soup.findAll("tr")
    
    for row in rows:
        if (len(row.findAll("td")) == 8):
            ip.append(row.contents[0].contents[0])
            port.append(row.contents[1].contents[0])
            address.append(row.contents[0].contents[0] + ':' + row.contents[1].contents[0])
    select = random.randint(0,(len(address) - 1))
    
    PROXY = random.choice(address[select])
    
    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': PROXY,
        'ftpProxy': PROXY,
        'sslProxy': PROXY,
        'noProxy': ''
        })
    
    profile = webdriver.FirefoxProfile()
    profile.set_preference('general.useragent.override', random.choice(uas).decode("utf-8"))
    profile.set_preference("network.proxy.type", 1)
    profile.set_preference("network.proxy.share_proxy_settings", True)
    profile.set_preference("network.http.use-cache", False)
    profile.set_preference("network.proxy.http", ip[select])
    profile.set_preference("network.proxy.http_port", int(port[select]))
    profile.set_preference('network.proxy.ssl_port', int(port[select]))
    profile.set_preference('network.proxy.ssl', ip[select])
    profile.set_preference('network.proxy.socks', ip[select])
    profile.set_preference('network.proxy.socks_port', int(port[select]))
    driver = webdriver.Firefox(firefox_profile=profile, proxy=proxy)
    driver.set_page_load_timeout(25)
    try:
        driver.get('https://www.youtube.com/watch?v=iuupZT9ZF_M&t=4s')
        time.sleep(600)
        driver.quit()
    except:
        driver.quit()
    
