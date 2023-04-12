import requests

_URL = "http://localhost:5000/{}"

def get_status():
  url = _URL.format("get_status")
  data = {'elevator': 1, 'all_elevators': False, 'all_attrs': False}
  print(requests.get(url, json=data).json())

def call_elevator():
  url = _URL.format("call_elevator")
  data = {'floor': 1}
  print(requests.post(url, json=data).json())

get_status()
call_elevator()