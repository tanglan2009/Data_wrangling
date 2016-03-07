from bs4 import BeautifulSoup
import requests
import html5lib


url = "http://shop.oreilly.com/category/browse-subjects/data.do?%20sortby=publicationDate&page=1"

soup = BeautifulSoup(requests.get(url).text, 'html5lib')
tds = soup.find_all('td', 'thumbtext')
print tds

print type(tds)
print len(tds)


def is_video(td):

    pricelabels = td('span', 'pricelabel')
    return (len(pricelabels) == 1 and pricelabels[0].text.strip().startswith('Video'))


print len([td for td in tds if not is_video(td)])