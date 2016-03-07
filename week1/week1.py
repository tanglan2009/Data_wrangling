import os
import csv
import xlrd

# DATAFILE = "beatles-diskography.csv"
#
#
# def parse_file(datafile):
#     data = []
#     with open(datafile, 'r') as f:
#         header = f.readline().split(',')
#         print header1
#         for line in f:
#             d = {}
#             line = line.strip().split(',')
#             print line
#             i = 0
#             for value in line:
#                 d[header[i]] = value
#             print d
#             data.append(d)
#             i += 1
#     return data
#
# print parse_file(DATAFILE)
#
# def test():
#    # a simple test of your implemetation
#     datafile = os.path.join(DATADIR, DATAFILE)
#     d = parse_file(datafile)
#     firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
#     tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}
#
#     assert d[0] == firstline
#     assert d[9] == tenthline


# from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data.xls"


# def open_zip(datafile):
#     with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
#         myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    ### example on how you can get the data
    # data = [[sheet.cell_value(r, col)
    #             for col in range(sheet.ncols)]\
    #                 for r in range(sheet.nrows)]

    # print "\nList Comprehension"
    # print "data [3][2]:",
    # print data[3][2]
    #
    # print "\nCells in a nested loop:"
    # for row in range(sheet.nrows):
    #     for col in range(sheet.ncols):
    #         if row == 50:
    #             print sheet.cell_value(row, col),





    ## other useful methods:
    # print "\nROWS, COLUMNS, and CELLS:"
    # print "Number of rows in the sheet:",
    # print sheet.nrows
    # print "Type of data in cell (row 3, col 2):",
    # print sheet.cell_type(3, 2)
    # print sheet.cell_value(5392, 1)
    # print sheet.cell_value(5391, 1)
    # print "Value in cell (row 3, col 2):",
    # print sheet.cell_value(3, 2)
    # print "Get a slice of values in column 3, from rows 1-3:"
    #print sheet.col_values(3, start_rowx=1, end_rowx=4)
    #
    # print "\nDATES:"
    # print "Type of data in cell (row 1, col 0):",
    # print sheet.cell_type(1, 0)
    # exceltime = sheet.cell_value(1, 0)
    # print "Time in Excel format:",
    # print exceltime
    # print "Convert time to a Python datetime tuple, from the Excel float:",
    # print xlrd.xldate_as_tuple(exceltime, 0)

    coast_data = sheet.col_values(1, start_rowx = 1)
    # print "Length of coast_data: ", len((coast_data))
    # print "maxvalue is", max(coast_data)
    # print "minvalue is", min(coast_data)
    # print "avgcoast is", sum(coast_data)/len(coast_data)

    rowOfmaxVal = coast_data.index(max(coast_data)) + 1
    # print "maxtime index is", rowOfmaxVal
    rowOfminVal = coast_data.index(min(coast_data)) + 1

    maxexceltime = sheet.cell_value(rowOfmaxVal, 0)
    minexceltime = sheet.cell_value(rowOfminVal, 0)
    maxtime = xlrd.xldate_as_tuple(maxexceltime, 0)
    mintime = xlrd.xldate_as_tuple(minexceltime, 0)
    # print maxtime
    # print mintime


    data = {
            'maxtime': maxtime,
            'maxvalue': max(coast_data),
            'mintime': mintime,
            'minvalue': min(coast_data),
            'avgcoast': sum(coast_data)/len(coast_data)
    }
    return data

print parse_file(datafile)

def test():
    # open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18770.166858114047, 10)


test()
# #
# #
#

# import json
# import requests
#
# BASE_URL = "http://musicbrainz.org/ws/2/"
# ARTIST_URL = BASE_URL + "artist/"
#
# # query parameters are given to the requests.get function as a dictionary; this
# # variable contains some starter parameters.
# query_type = {  "simple": {},
#                 "atr": {"inc": "aliases+tags+ratings"},
#                 "aliases": {"inc": "aliases"},
#                 "releases": {"inc": "releases"}}
#
#
# def query_site(url, params, uid="", fmt="json"):
#     # This is the main function for making queries to the musicbrainz API.
#     # A json document should be returned by the query.
#     params["fmt"] = fmt
#     r = requests.get(url + uid, params=params)
#     print "requesting", r.url
#
#     if r.status_code == requests.codes.ok:
#         return r.json()
#     else:
#         r.raise_for_status()
#
#
# def query_by_name(url, params, name):
#     # This adds an artist name to the query parameters before making
#     # an API call to the function above.
#     params["query"] = "artist:" + name
#     return query_site(url, params)
#
#
# def pretty_print(data, indent=4):
#     # After we get our output, we can format it to be more readable
#     # by using this function.
#     if type(data) == dict:
#         print json.dumps(data, indent=indent, sort_keys=True)
#     else:
#         print data
#
#
# def main():
#     '''
#     Modify the function calls and indexing below to answer the questions on
#     the next quiz. HINT: Note how the output we get from the site is a
#     multi-level JSON document, so try making print statements to step through
#     the structure one level at a time or copy the output to a separate output
#     file.
#     '''
#     results = query_by_name(ARTIST_URL, query_type["simple"], "FIRST AID KIT")
#     # pretty_print(results['artists'][1]['area']['name'])
#     # pretty_print(results)
#     count = 0
#     for ele in results['artists']:
#         if ele['name'] == 'First Aid Kit':
#             #print ele['name']
#             count += 1
#     print 'number of band named"First Aid Kit" is: ', count
#
#
#     results1= query_by_name(ARTIST_URL, query_type["simple"], "Queen")
#     # pretty_print(results1)
#     pretty_print(results1['artists'][0]['begin-area'])
#
#     for ele in results1['artists']:
#         if ele['name'] == 'Queen' and 'begin-area' in ele:
#
#            begin_area_name_for_Queen = ele['begin-area']['name']
#     print 'begin-area name for Queen is:', begin_area_name_for_Queen
#
#
#
#     results2 = query_by_name(ARTIST_URL, query_type["aliases"], "BEATLES")
#     # pretty_print(results2)
#     #pretty_print(results2['artists'][0])
#     for ele in results2['artists']:
#         if 'aliases' in ele:
#             for elem in ele['aliases']:
#                 if elem['locale'] == 'es':
#                     print 'Spanish Alias for Beatles is:',elem['name']
# #     #
# # #
#     results3 = query_by_name(ARTIST_URL, query_type["simple"], "NIRVANA")
#     # pretty_print(results3['artists'])
#     for ele in results3['artists']:
#         if  ele['name'] == 'Nirvana' and ele['country'] == 'US':
#             print 'Nirvana disambiguation is:', ele['disambiguation']
#
#
#
#
#     results4= query_by_name(ARTIST_URL, query_type["simple"], "One Direction")
#     # pretty_print(results4)
#     for ele in results4['artists']:
#         if ele['name'] == 'One Direction':
#             print ele['life-span']
#
#     # artist_id = results["artists"][1]["id"]
#     # print "\nARTIST:"
#     # pretty_print(results["artists"][1])
#
#
#     # artist_id = results['artists'][2]
#     # artist_data = query_site(ARTIST_URL, query_type["releases"], artist_id)
#     # releases = artist_data["releases"]
#     # print "\nONE RELEASE:"
#     # pretty_print(releases[0], indent=2)
#     # release_titles = [r["title"] for r in releases]
#     #
#     # print "\nALL TITLES:"
#     # for t in release_titles:
#     #     print t
#
#
# if __name__ == '__main__':
#     main()