import json
import os
import requests
import time

def getNameUri(card_dict):
  global card_list
  global counter

  for card in card_dict:
    # print(counter, end=". ")
    name = card["name"]
    # print(name)
    img_uris = card["image_uris"]
    small_img_uri = img_uris["normal"]
    # print("URI: ", small_img_uri , end="\n\n")
    card_list.append({"name": name, "uri": small_img_uri})
    counter += 1

with open("/Users/Fazooli/Desktop/MTG_The_Bootlegging/MTG_ALPHA_1.json", "r") \
as f:
  data = json.load(f)

# List of all card name/uri objects.
card_list = []

# Get total number of cards from JSON.
total_cards = int(data["total_cards"])
print("Total Cards: ", total_cards)

# Track number of cards.
counter = 1

# Get card list from JSON. 
card_dict = data["data"]

getNameUri(card_dict)

f.close()

with open("/Users/Fazooli/Desktop/MTG_The_Bootlegging/MTG_ALPHA_2.json", "r") \
as f:
  data = json.load(f)

# Get card list from JSON. 
card_dict = data["data"]

getNameUri(card_dict)

f.close()

cwd = os.getcwd()
cwd = cwd + "/Library/"

for card in card_list:
  img_uri = card["uri"]

  name = card["name"]
  path = cwd + name + ".jpeg"
  with open(path, 'wb') as fd:
    response = requests.get(img_uri, stream=True)
    
    time.sleep(.05) # Not to overburden the scryfall server.

    if not response.ok:
        print(response)

    for block in response.iter_content(1024):
        if not block:
            break

        fd.write(block)

  fd.close()