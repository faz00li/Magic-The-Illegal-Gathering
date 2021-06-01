import binascii
import os
import random
import shutil
import sys

def createDeck():
  # Get current directory.
  cur_dir = os.getcwd()

  deck_dir = cur_dir + "/Deck"

  try:
    # Remove old deck.
    shutil.rmtree(deck_dir)
  except Exception as e:
    print(e)
  
  # Create new deck directory.
  os.mkdir(deck_dir)

  # Get path to new deck list.
  deck_file_name = sys.argv[1]
  deck_name = deck_file_name.capitalize().rstrip(".txt")
  deck_path = cur_dir + "/Deck Lists/" + deck_file_name

  print("Creating deck named {}\nFrom file: {} \n".format(deck_name, deck_path))

  f = open(deck_path, "rt")
  card_list = f.readlines()
  f.close()

  # Iterate through deck list.
  for line in card_list:
    # Get card name and number of instances in deck.
    line = line.rstrip('\n')
    name_num = line.split(":") 
    card_name = name_num[0]
    num_cards = int(name_num[1]) 

    # Get original card file path.
    org_card_path = cur_dir + "/Library/" + card_name + ".jpeg"
    
    print("Num Cards: ", num_cards)
    print("Original Card Path: ", org_card_path)

    for i in range(num_cards):
      # Get cryptographically random sequence of 16 chars.
      rand_name = binascii.hexlify(os.urandom(16)).decode()

      # Create path for duplicate card.
      dup_card_path = cur_dir + "/Deck/" + rand_name + ".jpeg"
      print("Duplicate Card Path: ", dup_card_path)

      # Copy file. 
      # TODO: move copy file functionaliyt to draw card
      shutil.copyfile(org_card_path, dup_card_path)
    
    print()

  
  # open file for reading
  # open file for writing
  # open file with current name
  # make copy of file
  # name file with hex string
  

'''
# Params: text file
# Returns: dictionary
#
* parse deck list by line -> list
* parse line -> name, num
* dict.append("name": num)
*
''' 

createDeck()
