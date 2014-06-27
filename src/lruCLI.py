#!/usr/bin/python
import sys
import os
from cmd import Cmd
from lruDB import db


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
             dbobj.parseNetworkConfig()        
        else:
            print "No args"
        
    def do_quit(self,args):
        raise SystemExit
    def do_login(self, args):
        print ""