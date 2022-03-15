#!/usr/bin/python
import os
import requests
import json

class noPermission(Exception):
  pass

class Client:
  def __init__(self, key):
    self.key = key

class Assets:
  def __init__(self, password=None):
    self.password = password

    if self.password == None:
      raise noPermission(f"'{self.password}' must be filled")

  def parse_json(tjson):
    return json.dumps(tjson, sort_keys=False, indent=2)