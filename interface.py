import os

from io import StringIO

interface = StringIO("Welcome to Magic the Illegal Gathering")

def cls():
  os.system('cls' if os.name=='nt' else 'clear')

def read():
  interface.seek(0)
  msg = interface.readlines()
  interface.seek(0)
  interface.truncate()

  return msg

def write(msg, padding = "\n"):
  interface.write(msg + padding)


