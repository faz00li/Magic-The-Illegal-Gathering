# Download single card from Scryfall API.

import sys
import os
import requests

img_uri = sys.argv[1]
img_name = sys.argv[2]

path = os.getcwd()
path = path + "/new deck/" + img_name

print(path)

with open(path, 'wb') as fd:
  response = requests.get(img_uri, stream=True)

  if not response.ok:
      print(response)

  for block in response.iter_content(1024):
      if not block:
          break

      fd.write(block)

fd.close()






    