from bs4 import BeautifulSoup 
import requests as req

url = req.get("https://www.statsheep.com/p/Top-Video-Views?page=1")

source = url.content
soup = BeautifulSoup(source, 'lxml')
links = soup.find_all("a")
page = []
page2 = []
page3 = []
#Change dataQuantity for the number of youtubers(max = 100)
#The more the dataQuantity, the longer it takes for the data to load
#The graph becomes coruded with a higher data quantity
dataQuantity = 10

for link in links:
    page.append(link.get("name"))

while(None in page): 
    page.remove(None)
while('Top Subscribed YouTube Channels' in page):
    page.remove('Top Subscribed YouTube Channels')
while('Top Video Views For YouTube Channels' in page):
    page.remove('Top Video Views For YouTube Channels')


x = 0
while (x < dataQuantity):
    page2.append(page[x].split())
    x = x +1    
y = 0
while (y < dataQuantity):
    page3.append(page2[y][0])
    y = y + 1

while('page' in page3):
    page3.remove('page')

url2 = []
source2 = []
soup2 = []
link2 = []
videoViews = []
videoViews2 = []
videoViews3 = []
finalViews = []
uploadedVideos = []
uploadedVideos2 = []
uploadedVideos3 = []
finalUploaded = []
avgViews = []
allValues = 0

while (allValues < dataQuantity):
    url2.append(req.get(f"http://statsheep.com/{page3[allValues]}"))
    source2.append(url2[allValues].content)
    soup2.append(BeautifulSoup(source2[allValues], 'lxml'))
    link2.append(soup2[allValues].find_all("div", {"class": "columns left p-top-small p-bottom-small info b-bottom"}))
   
    videoViews.append(str(link2[allValues][2]).split('>'))
    videoViews2.append((videoViews[allValues][3]).split('<'))
    videoViews3.append(videoViews2[allValues][0])
    finalViews.append(int(videoViews3[allValues].replace(',','')))
   
    uploadedVideos.append(str(link2[allValues][6]).split('>'))
    uploadedVideos2.append((uploadedVideos[allValues][3]).split('<'))
    uploadedVideos3.append(uploadedVideos2[allValues][0])
    finalUploaded.append(int(uploadedVideos3[allValues].replace(',','')))
    
    allValues = allValues + 1


while (0 in finalUploaded):
    finalUploaded.remove(0)
while (0 in finalViews):
    finalViews.remove(0)
while ('muyap' in page3):
    page3.remove('muyap')
while ('sonybmg' in page3):
    page3.remove('sonybmg')

if (dataQuantity > 9):
    if (dataQuantity < 80):
        dataQuantity = dataQuantity - 1

if (dataQuantity > 80):
    dataQuantity = dataQuantity - 2

num = 0
while (num < dataQuantity):
    avgViews.append((finalViews[num]) / (finalUploaded[num]))
    num = num + 1


print(avgViews)

#Data visualisation

import pandas
from matplotlib import pyplot as plt

y1 = []
plt.plot(page3[0:dataQuantity], avgViews)
plt.title(f"Average Views per Video of Top {dataQuantity} Youtuber's")
plt.xlabel("Youtuber Channel Name")
plt.ylabel("Average Views per video")
plt.show()
