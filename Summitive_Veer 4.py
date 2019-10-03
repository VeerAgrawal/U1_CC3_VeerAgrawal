from bs4 import BeautifulSoup 
import requests as req

url = req.get("https://www.statsheep.com/p/Top-Video-Views?page=1")

source = url.content
soup = BeautifulSoup(source, 'lxml')
links = soup.find_all("a")
page = []
page2 = []
page3 = []
#data = soup.find_all("div", {"class": "user-icon round"})

for link in links:
    #print("<a href='%s'>%s</a>" % (link.get("href"), link)
    page.append(link.get("name"))

while(None in page): 
    page.remove(None)
while('Top Subscribed YouTube Channels' in page):
    page.remove('Top Subscribed YouTube Channels')
while('Top Video Views For YouTube Channels' in page):
    page.remove('Top Video Views For YouTube Channels')


x = 0
while (x < 100):
    page2.append(page[x].split())
    x = x +1    
y = 0
while (y < 100):
    page3.append(page2[y][0])
    y = y + 1

while('page' in page3):
    page3.remove('page')

#print(page3)

allPages = 0
while (allPages < 100):
    url2 = req.get(f"http://statsheep.com/{page3[allPages]}")
    allPages = allPages + 1


source2 = url2.content
soup2 = BeautifulSoup(source2, 'lxml')

#link2 = soup2.find_all("div", {"class": "columns left p-top-small p-bottom-small info b-bottom"})
#a.append(link2[0])
#print(a)
#print(type(a[0]))
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

