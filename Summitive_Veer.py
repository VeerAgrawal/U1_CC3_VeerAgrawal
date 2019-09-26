from bs4 import BeautifulSoup 
import requests as req

result = req.get("https://www.statsheep.com/p/Top-Video-Views?page=1")

print(result.status_code)
src = result.content
soup = BeautifulSoup(src, 'lxml')

links = soup.find_all("a")
#print(links)

for link in links:
    print(link.text)
    if "name" in link.text:
        #print(link)
        print(link.attrs['href'])

