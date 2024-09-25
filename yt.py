from selenium import webdriver
driver = webdriver.Chrome(
    executable_path="C:\\Users\\krome\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get(
    "https://chromedriver.storage.googleapis.com/index.html?path=108.0.5359.125 /")

"Youtube views"
from selenium import webdriver
import time
import random
driver = webdriver.Chrome()
videos = [
    
]

for i in range(1000):
    print("Running the video for {} time".format(i))
    random_video = random.randint(0, 14)
    driver.get(videos[random_video])
    sleep_time = random.randint(10, 20)
    time.sleep(sleep_time)
driver.quit()

#Youtube copy URLS 

import scrapetube
import pandas as pd
channelid = input("Enter the Youtube Channel ID ")
list = []
url = "https://www.youtube.com/watch?v="
dataframe = pd.DataFrame(columns=["URL"])
videos = scrapetube.get_channel(channelid)

for video in videos:
    url1 = url + str(video['videoId'])
    print(url1)
    list.append(url1)
dataframe['URL'] = list
dataframe.to.excel("MYURL.xlsx")
print("Task Complete")