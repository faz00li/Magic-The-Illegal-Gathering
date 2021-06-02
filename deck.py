from io import StringIO

import binascii
import os
import shutil
import sys


# Global variable. List representing the deck.
deck = []

# Get current and deck directories.
cur_dir = os.getcwd()
deck_dir = cur_dir + "/Deck"
interface = open(cur_dir + "/interface.txt", "w+t")
interface.write("Welcome to Magic the Illegal Gathering")

def sortHelper(card):
  return card["d_path"]

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def toGUI(msg):
  global msg
  msg_size = interface.write(msg)
  interface.seek(interface.tell()/msg)

def createDeck() -> list:

  global deck

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
    print("{}: {}".format(num_cards, card_name))

    for i in range(num_cards):
      # Get cryptographically random sequence of 16 chars.
      rand_name = binascii.hexlify(os.urandom(16)).decode()

      # Create path for duplicate card.
      dup_card_path = cur_dir + "/Deck/" + rand_name + ".jpeg"
      print("Duplicate Card Path: ", dup_card_path)
      deck.append({"name": card_name, "o_path": org_card_path, "d_path": dup_card_path})

  deck.sort(key = sortHelper)

  return deck

def drawCard():
  if len(deck) == 0:
    toGUI("Deck is exhausted.")
    return 
  else:
    card = deck.pop(0)
    shutil.copyfile(card["o_path"], card["d_path"])

def clearDrawPile():
  global deck_dir

  print("Size of draw pile: ", len(os.listdir(deck_dir))) 
  if len(os.listdir(deck_dir)) == 0:
    toGUI("Draw pile is empty.")
    return
  else:
    for f in os.listdir(deck_dir):
      os.remove(os.path.join(deck_dir, f))

# def drawHand():
#   return None

# def putCardOnTopOfLibrary(str: card_name):
#   return None

# def shuffleLibrary():
#   return None
    




