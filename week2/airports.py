# -*- coding: utf-8 -*-
# All your changes should be in the 'extract_airports' function
# It should return a list of airport codes, excluding any combinations like "All"

from bs4 import BeautifulSoup
html_page = "Data ElementsPS.html"


def extract_airports(page):
    data = []
    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "lxml")
        airportList = soup.find(id='AirportList')
        for option in airportList.find_all('option'):
            # print option
            if 'All' not in option['value']:
                 data.append(option['value'])

        print len(data)

    return data
print extract_airports(html_page)

# def test():
#     data = extract_airports(html_page)
#     assert len(data) == 15
#     assert "ATL" in data
#     assert "ABR" in data
#
# test()