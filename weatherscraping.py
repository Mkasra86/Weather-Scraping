# Importing Needed Libraries
from bs4 import BeautifulSoup
import time
import requests 

reftime = 10

# Writing The Brain Of The App
def sec_10_pollution(url):
    while True:
        response = requests.get(url)
        if response.ok:
            soup = BeautifulSoup(response.text , 'html.parser')
            quotes = soup.find_all('div', class_ = 'info-box-content')
            text = quotes[1].find('span', class_ = 'info-box-number aqival').get_text()
            now = time.localtime()
            current_time = time.strftime("%H:%M:%S", now)
            print(f"----------------------\n  *Pollutant : PM2.5*\nWeather Pollution : {text}\nCurrent Time : {current_time}\n  *REFRESH TIME {reftime}sec*\n     By MatinKasra")
        else:
            print("something went wrong")
        time.sleep(reftime)  


# Running The App
sec_10_pollution('https://airnow.tehran.ir/')