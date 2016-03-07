"""
Your task is to process the supplied file and use the csv module to extract data from it.
The data comes from NREL (National Renewable Energy Laboratory) website. Each file
contains information from one meteorological station, in particular - about amount of
solar and wind energy for each hour of day.

Note that the first line of the datafile is neither data entry, nor header. It is a line
describing the data source. You should extract the name of the station from it.

The data should be returned as a list of lists (not dictionaries).
You can use the csv modules "reader" method to get data in such format.
Another useful method is next() - to get the next line from the iterator.
You should only change the parse_file function.
"""
import csv
import os
import numpy as np

DATADIR = ""
DATAFILE = "745090.csv"


# def parse_file(datafile):
#     name = ""
#     data = []
#     with open(datafile,'rb') as f:
#
#         reader = csv.reader(f)
#         line1 = f.readline().split(',')
#         name = name + line1[1].replace('\"', '')
#
#         header = next(reader)
#         # print header
#         # print len(header)
#         # for i, val in enumerate(header):
#         #     print i, val, type(val)
#        # all(next(reader) for i in range(2))   # skip the first two lines
#         for row in reader:
#             # print row
#             data.append(row)
#
#     # Do not change the line below
#     return (name, data)
#
# print parse_file(DATAFILE)

# print data[0][1]
# print data[2][0]
# print data[2][5]

# #answer version:
def parse_file(datafile):
    name = ""
    data = []
    with open(datafile, 'rb') as f:
        r = csv.reader(f)
        name = r.next()[1]
        print name
        header = r.next()
        data = [row for row in r]

    return (name, data)

print parse_file(DATAFILE)


def test():
    datafile = os.path.join(DATADIR, DATAFILE)
    name, data = parse_file(datafile)

    assert name == "MOUNTAIN VIEW MOFFETT FLD NAS"
    assert data[0][1] == "01:00"
    assert data[2][0] == "01/01/2005"
    assert data[2][5] == "2"


if __name__ == "__main__":
    test()

