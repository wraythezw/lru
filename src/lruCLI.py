#!/usr/bin/python
import sys
import os
from cmd import Cmd
from lruDB import db


class cli(Cmd):
    db = ""
    def __init__(self):
        db = db()
    def do_set(self, args):
        """Sets a configuration variable"""
        print("set")
    def do_show(self, args):
        """Shows the running config"""
        print("show")
    def do_login(self, args):
