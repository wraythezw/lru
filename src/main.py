#!/usr/bin/python
import string
import socket
from lruCLI import cli

prompt = cli()
prompt.prompt = '> '

prompt.cmdloop('***   LRU System prompt init ***')

print "end"