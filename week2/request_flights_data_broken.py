import requests
from bs4 import BeautifulSoup

s = requests.Session()
r = s.get("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2")
soup = BeautifulSoup(r.text, 'lxml')
print soup
viewstate_element = soup.find(id="__VIEWSTATE")
print viewstate_element, type(viewstate_element)
viewstate = viewstate_element['value']
eventvalidation_element = soup.find(id="__EVENTVALIDATION")
eventvalidation = eventvalidation_element["value"]


r = s.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
                  data = { 'AirportList': "BOS",
                          'CarrierList' : 'VX',
                          'Submit' : 'Submit',
                          '__EVENTTARGET' : '',
                          '__EVENTARGUMENT' : '',
                          '__EVENTVALIDATION' : eventvalidation,
                          '__VIEWSTATE' : viewstate})

f = open("Data Elements.html", 'w')
f.write(r.text)