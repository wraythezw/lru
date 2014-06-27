#!/usr/bin/python
import sys
import os
from cmd import Cmd



class cli(Cmd):
 def do_set(self,args):
  """Sets a configuration variable"""
  print("set")
 def do_show(self,args):
  """Shows the running config"""
  print("show")