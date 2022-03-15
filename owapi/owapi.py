#!/usr/bin/python
import os
import requests
import json

# error's
class noPermission(Exception):
  pass

url = "";

# client
class Client:
  def __init__(self, key):
    self.key = key


  

class Assets:
  def __init__(self, password=None):
    self.password = password

    if self.password == None or self.password != os.getenv('password'):
      raise noPermission(f"'{self.password}' must be filled or is incorrect")

  def parse_json(tjson):
    return json.dumps(tjson, sort_keys=False, indent=2)

