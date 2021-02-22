#!/usr/bin/env python3

import os
from PIL import Image

def change_image(directory):
  """Reads through all the images in a directory and resizes them to 600x400,
    then converts them to RGB format jpegs, with matching file extensions
    """
  new_extension = '.jpeg'

  for file in os.listdir(directory):      # Loop through the files in the dir
    if '.tiff' in file:
      img = Image.open(directory +'/'+ file)
      name, _ = file.split('.')
      file = name + new_extension
      img.resize((600, 400)).convert('RGB').save(directory + file, 'JPEG')

change_image('/home/student-00-4dd743e70e3f/supplier-data/images/')