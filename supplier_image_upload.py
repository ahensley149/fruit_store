#!/usr/bin/env python3

import requests
import os

url = "http://localhost/upload/"

def upload_images(directory):
  for file in os.listdir(directory):
    with open(directory + file, 'rb') as opened:
      result = requests.post(url, files={'file': opened})

upload_images('/home/student-00-4dd743e70e3f/supplier-data/images/')