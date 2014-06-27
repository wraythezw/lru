#!/usr/bin/python
import string
import sys
import os
import re
from cmd import Cmd

class db:
    configpath="/etc/lru/"
    netconfig="network.xml"
    def parseNetworkConfig(self):
        print "network{"
        # get interfaces from /etc/sysconfig/network-scripts/
        files = [f for f in os.listdir('/etc/sysconfig/network-scripts/') if re.match(r'ifcfg*', f)]
        for f in files:
            print f.split("-",1)[1] + "{"
            t=open("/etc/sysconfig/network-scripts/" + f)
            lines = t.read().split("\n")
            for i in lines:
                if "NAME" in i:
                 print " name = " + i.split("=",1)[1]
                if "BOOTPROTO" in i:
                  print " type = " + i.split("=",1)[1] 
                if "IPADDR" in i:
                  print " ipaddress = " + i.split("=",1)[1]
                if "NETMASK" in i:
                 print " mask = " + i.split("=",1)[1]
                if "ONBOOT" in i:
                 print " active = " + i.split("=",1)[1]     
                if "HWADDR" in i:
                 print " hwaddr = " + i.split("=",1)[1]                
#        print lines
            t.close()
        print " }"
        print "}"