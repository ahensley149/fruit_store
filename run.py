#!/usr/bin/env python3

import os
import requests

def upload_fruit(directory):
    
    for files in os.listdir(directory):
      name, ext = files.split('.')
      img = name + '.jpeg'
      with open(directory+name+'.'+ext) as file:
        data = file.read().split('\n')
        weight, _ = data[1].split(' ')
        fruit = {'name': data[0], 'weight': int(weight), 'description': data[2], 'image_name': img}
        response = requests.post("http://localhost/fruits/", json=fruit)
        print(response)
upload_fruit('/home/student-00-4dd743e70e3f/supplier-data/descriptions/')

