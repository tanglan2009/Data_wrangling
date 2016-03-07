#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Let's assume that you combined the code from the previous 2 exercises
# with code from the lesson on how to build requests, and downloaded all the data locally.
# The files are in a directory "data", named after the carrier and airport:
# "{}-{}.html".format(carrier, airport), for example "FL-ATL.html".
# The table with flight info has a table class="dataTDRight".
# There are couple of helper functions to deal with the data files.
# Please do not change them for grading purposes.
# All your changes should be in the 'process_file' function
# This is example of the datastructure you should return
# Each item in the list should be a dictionary containing all the relevant data
# Note - year, month, and the flight data should be integers
# You should skip the rows that contain the TOTAL data for a year
# data = [{"courier": "FL",
#         "airport": "ATL",
#         "year": 2012,
#         "month": 12,
#         "flights": {"domestic": 100,
#                     "international": 100}
#         },
#         {"courier": "..."}
# ]


import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile
import os
import numpy as np

s = requests.Session()
r = s.get("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2")
soup = BeautifulSoup(r.text, 'lxml')
carrierList = soup.find(id="CarrierList")
airportList = soup.find(id="AirportList")

table = soup.find(id="DataGrid1")
print table
for option in carrierList.find_all('option'):
    if 'All' not in option["value"]:
        courier = option["value"]
        # print courier

for option in airportList.find_all("option"):
    if 'All' not in option["value"]:
        airport = option["value"]
        # print airport
temList = []
for row in table.find_all('td'):
    # print row.text, type(row.text)

    temList.append(row.text)
npTemList = np.array(temList).reshape([len(temList)/5, 5])
print npTemList[1:]
for ele in npTemList[1:]:
    print ele
    if 'TOTAL' not in ele:
        year = int(ele[0])
        print year, type(year)
        month = int(ele[1])
        print month, type(month)
        domestic = int(ele[2].replace(',',''))
        print domestic, type(domestic)
        international = int(ele[3].replace(',', ''))
        print international, type(international)
#
#
#
#
# r = s.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
#                   data = { 'courier': courier,
#                           'airport' : airport,
#                           'year' : year,
#                           'month': month,
#          "flights": {"domestic": domestic,
#                      "international": international}
#
#                           })
#
# f = open("Data ElementsPS.html", 'w')
#
# f.write(r.text)

# datadir = "data"
#
#
# def open_zip(datadir):
#     with ZipFile('{0}.zip'.format(datadir), 'r') as myzip:
#         myzip.extractall()
#
#
# def process_all(datadir):
#     files = os.listdir(datadir)
#     return files
#
#
# def process_file(f):
#     """This is example of the data structure you should return.
#     Each item in the list should be a dictionary containing all the relevant data
#     from each row in each file. Note - year, month, and the flight data should be
#     integers. You should skip the rows that contain the TOTAL data for a year
#     data = [{"courier": "FL",
#             "airport": "ATL",
#             "year": 2012,
#             "month": 12,
#             "flights": {"domestic": 100,
#                         "international": 100}
#             },
#             {"courier": "..."}
#     ]
#     """
# #
# #
#     data = []
#     info = {}
#     info["courier"], info["airport"] = f[:6].split("-")
#     # Note: create a new dictionary for each entry in the output data list.
#     # If you use the info dictionary defined here each element in the list
#     # will be a reference to the same info dictionary.
#     with open("{}/{}".format(datadir, f), "r") as html:
#
#         soup = BeautifulSoup(html)
#         table = soup.find(id="DataGrid1")
#         temList = []
#         for row in table.find_all("td"):
#             temList.append(row.text)
#         npTemList = np.array(temList).reshape([len(temList)/5, 5])
#         for ele in npTemList[1:]:
#             if "TOTAL" not in ele:
#                 year =int(ele[0])
#                 month = int(ele[1])
#                 domestic = int(ele[2])
#                 international = int(ele[3])
#                 elementInData = {'courier' : info['courier'],
#                                  'airport' : info['airport'],
#                                  'year' : year,
#                                  'month' : month,
#                                  'flight' : {'domestic' : domestic,
#                                              'international' : international}
#                                 }
#                 data.append(elementInData)
#
#     return data
# # open_zip(datadir)
# files = process_all(datadir)
# print process_file(files)
# def test():
#     print "Running a simple test..."
#     open_zip(datadir)
#     files = process_all(datadir)
#     data = []
#     for f in files:
#         data += process_file(f)
#
#     assert len(data) == 399  # Total number of rows
#     for entry in data[:3]:
#         assert type(entry["year"]) == int
#         assert type(entry["month"]) == int
#         assert type(entry["flights"]["domestic"]) == int
#         assert len(entry["airport"]) == 3
#         assert len(entry["courier"]) == 2
#     assert data[0]["courier"] == 'FL'
#     assert data[0]["month"] == 10
#     assert data[-1]["airport"] == "ATL"
#     assert data[-1]["flights"] == {'international': 108289, 'domestic': 701425}
#
#     print "... success!"
#
# if __name__ == "__main__":
#     test()