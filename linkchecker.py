import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

#open and separate sentence and remove new lines
with open("C:/Users/Arkadiusz/Desktop/FV/Październik/check.txt") as file:
    # text = (file.read())
    # print(text)
    licz = 0
    linklist = {}
    # line itteraction
    for line in file:
        line = line.rstrip("\n")
        r = requests.get(line)
        soup = BeautifulSoup(r.text, 'lxml')
        links = soup.find_all('a')
        scheme = (urlparse(line)).scheme
        domain = (urlparse(line)).netloc
        fullurl = str(scheme)+ "://" + str(domain)
        if line.startswith("http"):
            linklist[line] = []
            for link in links:
                link = str(link.get('href')).rstrip("//")
                if link.startswith("http") and not link.startswith(fullurl):
                    linklist[line].append(link)

# Print results
for k, v in linklist.items():
    licz = licz + 1
    print(str(licz)+ "." " Na stronie: " + str(k) + " są linki zewnętrzne:")
    for results in v:
        print(results)
