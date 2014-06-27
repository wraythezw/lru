#!/usr/bin/python
import sys
import os
from cmd import Cmd
from lruDB import db
import subprocess


class cli(Cmd):
    def do_set(self, args):
        """Sets a configuration variable"""
        print("set")
    def do_show(self, args):
        """Shows the running config"""
        if len(args) != 0:
            # Get first command in args
            if args.split(' ',1)[0] == 'network':
             dbobj=db()
             if len(args.split(' ',1)) >= 2:
                 # identify second stage
                 dbobj.parseNetworkConfigInterface(args.split(' ',1)[1])
             else:
              dbobj=db()
              dbobj.parseNetworkConfig()        
        else:
            print "No args"
    def do_ping(self,args):
        """Pings a remote host
           usage
           ping host
        """
        ar=args.split(" ")
        if len(args) != 0:
         print "Sending 4 packets of 32 bytes to " + ar[0]
         p = subprocess.Popen(["ping","-c 4",ar[0]], stdout=subprocess.PIPE)
         out=p.communicate()
         print out
         
    def do_quit(self,args):
        raise SystemExit
    def do_login(self, args):
        print ""