#!/usr/bin/python
import string
from xml.dom import minidom

class db:
    configpath="/etc/lru/"
    netconfig="network.xml"
    def __init__(self):
        print("test")
    def parseNetworkConfig(self):
        xmldoc = minidom.parse(self.netconfig)
        itemlist = xmldoc.getElementsByTagName('interface') 
        print len(itemlist)
        print itemlist[0].attributes['name'].value
        for s in itemlist :
            print s.attributes['name'].value