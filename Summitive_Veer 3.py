from bs4 import BeautifulSoup 
import requests as req

url = req.get("https://www.statsheep.com/p/Top-Video-Views?page=1")

source = url.content
soup = BeautifulSoup(source, 'lxml')
links = soup.find_all("a")
page = []
#data = soup.find_all("div", {"class": "user-icon round"})

for link in links:
    #print("<a href='%s'>%s</a>" % (link.get("href"), link)
    page.append(link.get("name"))
    pageNew = page.copy()
    while(None in pageNew): 
       pageNew.remove(None)
    while('Top Subscribed YouTube Channels' in pageNew):
       pageNew.remove('Top Subscribed YouTube Channels')
    while('Top Video Views For YouTube Channels' in pageNew):
       pageNew.remove('Top Video Views For YouTube Channels')

print(pageNew)
url2 = req.get(f"http://statsheep.com/{pageNew}")
#print(result2)
source2 = url2.content
soup2 = BeautifulSoup(source2, 'lxml')

link2 = soup2.find_all('strong')
#print(link2)




#Data visualisation
    
import pandas
from matplotlib import pyplot as plt

x = []
y = []
plt.plot(x, y, 'o')
plt.title("Average Views per Video of Top 100 Youtuber's")
plt.xlabel("youtuber's")
plt.ylabel("Average Views per video")
plt.show()
