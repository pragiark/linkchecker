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
        line = line.rstrip()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        r = requests.get(line, headers=headers)
        soup = BeautifulSoup(r.text, 'lxml')
        links = soup.find_all('a')
        scheme = (urlparse(line)).scheme
        domain = (urlparse(line)).netloc
        fullurl = str(scheme)+ "://" + str(domain)
        # print(fullurl)
        if line.startswith("http"):
            linklist[line] = []
            for link in links:
                anchor = link.text
                link = str(link.get('href')).rstrip("//")
                if link.startswith("http://korkgeschaft.de") or link.startswith("https://korkgeschaft.de"):
                    linklist[line].append(link)
                    linklist[line].append(anchor)

# print(linklist)


for k, v in linklist.items():
    licz = licz + 1
    print(str(licz)+ "." " Na stronie: " + str(k))
    if not v:   # is not operator according to:  https://www.python.org/dev/peps/pep-0008/#id51
        print('nie ma szukanych linków')
    else:
        print("są następujące linki zewnętrzne i anchory:")
    for results in v:
        if v == []:
            print("links not found")
        else:
            print(results)
    print(" ")