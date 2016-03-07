from bs4 import BeautifulSoup
#
# def options(soup, id):
#     option_values = []
#     carrier_list = soup.find(id=id)
#     for option in carrier_list.find_all('option'):
#         option_values.append(option['value'])
#     return option_values
# #
# # def print_list(label, codes):
# #     print "\n%s:" %label
# #     for c in codes:
# #         print c
# #
# soup = BeautifulSoup(open("Data Elements.html"))
# codes =  options(soup, 'CarrierList')
# print codes

#print_list('carriers', codes)
#
# codes2 = options(soup, 'AirportList')
# print_list('Airports', codes2)

# def main():
#     soup = BeautifulSoup(open("virgin_and_logan_airport.html"))
#
#     codes = options(soup, 'CarrierList')
#     print("carriers", codes)
#
#     codes = options(soup, 'AirportList')
#     print_list("Airports", codes)


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Please note that the function 'make_request' is provided for your reference only.
# You will not be able to to actually use it from within the Udacity web UI.
# Your task is to process the HTML using BeautifulSoup, extract the hidden
# form field values for "__EVENTVALIDATION" and "__VIEWSTATE" and set the appropriate
# values in the data dictionary.
# All your changes should be in the 'extract_data' function
# from bs4 import BeautifulSoup
import requests
import json

html_page = "Data Elements.html"


def extract_data(page):
    data = {"eventvalidation": "",
            "viewstate": ""}

    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(open(page), 'lxml', )
        #hiddenElement = soup.find_all('input')

        # print hiddenElement['value']
        input1 = soup.find(id="__VIEWSTATE")
        # print input1
        # print input1['value']
        data['viewstate'] = input1['value']
        # print data['viewstate']

        input2 = soup.find(id="__EVENTVALIDATION")
        # print input2
        # print type(input2)
        data['eventvalidation'] = input2['value']
        # print data['eventvalidation']



    return data

print extract_data(html_page)
#
# def make_request(data):
#     eventvalidation = data["eventvalidation"]
#     viewstate = data["viewstate"]
#
#     r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
#                     data={'AirportList': "BOS",
#                           'CarrierList': "VX",
#                           'Submit': 'Submit',
#                           "__EVENTTARGET": "",
#                           "__EVENTARGUMENT": "",
#                           "__EVENTVALIDATION": eventvalidation,
#                           "__VIEWSTATE": viewstate
#                     })
#
#     return r.text
#
#
# def test():
#     data = extract_data(html_page)
#     assert data["eventvalidation"] != ""
#     assert data["eventvalidation"].startswith("/wEWjAkCoIj1ng0")
#     assert data["viewstate"].startswith("/wEPDwUKLTI")
#
#
#test()