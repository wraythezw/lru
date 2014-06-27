#!/usr/bin/python
import string
import socket
from lruCLI import cli

prompt = cli()
prompt.prompt = socket.gethostname() + '> '
prompt.cmdloop('Starting prompt...')