from bs4 import BeautifulSoup 
import requests as req

result = req.get("https://www.statsheep.com/p/Top-Video-Views?page=1")

source = result.content
soup = BeautifulSoup(source, 'lxml')

links = soup.find_all("a")

#data = soup.find_all("div", {"class": "user-icon round"})

for link in links:
    #print("<a href='%s'>%s</a>" % (link.get("href"), link))
    #print(link.get("href"))

#Page =          

#result2 = req.get(f"statsheep.com/" {page})

#source2 = result2.content
#soup = BeautifulSoup(source2, 'lxml')

#views = soup.find_all("div", {"class": "columns left p-top-small p-bottom-small info b-bottom"})



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