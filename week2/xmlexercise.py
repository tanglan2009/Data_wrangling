import xml.etree.ElementTree as ET
import numpy as np
import pprint

# tree = ET.parse('exampleResearchArticle.xml')
# root = tree.getroot()
#
#
# print '\nChildren of root:'
# for child in root:
#     print child.tag


article_file = "exampleResearchArticle.xml"

def get_root(fname):
    tree = ET.parse(fname)
    print tree
    return tree.getroot()


def get_authors(root):
    authors = []
    for author in root.findall('./fm/bibl/aug/au'):
        data = {}
        fnm = author.find('fnm').text
        snm = author.find('snm').text
        email = author.find('email').text
        data['fnm'] = fnm
        data['snm'] = snm
        data['email'] = email
        data['insr'] =[]
        insr = author.findall('insr')
        for i in insr:
            data['insr'].append(i.attrib['iid'])




        #if fnm is not None and snm is not None and email is not None:

        authors.append(data)
        authorsArray = np.array(authors)

    return authorsArray

root = get_root(article_file)
print root
print get_authors(root)

