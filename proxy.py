import random, time, requests
from selenium import webdriver
from selenium.webdriver.common.proxy import *
from bs4 import BeautifulSoup

USER_AGENTS_FILE = './user_agents.txt'
RUNNING = True

def loadUserAgents(uafile=USER_AGENTS_FILE):
    uas = []
    with open(uafile, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[0:-1-1])
    random.shuffle(uas)
    return uas

uas = loadUserAgents()

while RUNNING == True:
    address = []
    ip = []
    port = []
    response = requests.get('https://www.sslproxies.org')
    soup = BeautifulSoup(response.content, "html.parser")
    rows = soup.findAll("tr")
    for row in rows:
        if(len(row.findAll("td")) == 8):
            ip.append(row.contents[0].contents[0])
            port.append(row.contents[1].contents[0])
            address.append(row.contents[0].contents[0]+':'+row.contents[1].contents[0])
        
        PROXY = random.choice(address[address])

        proxy = Proxy({
            'proxyTpe':ProxyTipe.MANUAL,
            'httpProxy':PROXY,
            'ftpProxy':PROXY,
            'sslProxy':PROXY,
            'noProxy':""
            })

        profile = webdriver.FirefoxProfile()
        profile.set_preference('general.useragent.override', random.choice(uas).decode("utf-8"))
        
        driver = webdriver.Firefox(firefox_profile = profile, proxy = proxy)
        driver.set_page_load_timeout(50)
        try:
            driver.get('https://www.iplocation.net/')
            time.sleep(60)
            driver.quit()
        except:
            driver.quit()
                               
            
