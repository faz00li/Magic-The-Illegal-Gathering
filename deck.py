from io import StringIO

import binascii
import os
import shutil
import sys

from diagnostic import CREATE_DECK_DIAG

# Global variable. List representing the deck.
deck = []
deck_size = 0
msg_padding = " "

# Get current and deck directories.
cur_dir = os.getcwd()
deck_dir = cur_dir + "/Deck"
hand_dir = cur_dir + "/Hand"

interface = StringIO("Welcome to Magic the Illegal Gathering")

def sortHelper(card):
  return card["d_path"]

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def writeInterface(msg):
  interface.write(msg + msg_padding)

def createDeck():

  global deck
  global deck_size

  # Remove old deck.
  try:
    shutil.rmtree(deck_dir)
  except Exception as e:
    print(e)
  
  # Remove old hand.
  try:
    shutil.rmtree(hand_dir)
  except Exception as e:
    print(e)

  # Create new deck directory.
  os.mkdir(deck_dir)
  os.mkdir(hand_dir)

  # Get path to new deck list.
  deck_file_name = sys.argv[1]
  deck_name = deck_file_name.capitalize().rstrip(".txt")
  deck_path = cur_dir + "/Deck Lists/" + deck_file_name

  if CREATE_DECK_DIAG:
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

    if CREATE_DECK_DIAG:
      print("{}: {}".format(num_cards, card_name))

    for i in range(num_cards):
      # Get cryptographically random sequence of 16 chars.
      rand_name = binascii.hexlify(os.urandom(16)).decode()

      # Create path for duplicate card.
      deck_card_path = cur_dir + "/Deck/" + rand_name + ".jpeg"
      hand_card_path = cur_dir + "/Hand/" + rand_name + ".jpeg"

      if CREATE_DECK_DIAG:
        print("Duplicate Card Path: ", deck_card_path)

      deck.append({"name": card_name, "o_path": org_card_path, "d_path": deck_card_path, "h_path": hand_card_path})
      deck_size = deck_size + 1

  deck.sort(key = sortHelper)

def printDeck():
  global deck
  global deck_size

  print("\n////////// PRINTING DECK //////////")
  
  if deck_size == 0:
    print("Deck is empty")
    return

  print("Cards in deck: ", deck_size, end = "\n\n")

  for card in deck:
    print("Card:    ", card["name"])
    print("Library: ", card["o_path"])
    print("Deck:    ", card["d_path"])
    print("Hand:    ", card["h_path"], end = '\n\n')

def drawCard():
  if len(deck) == 0:
    writeInterface("Deck is exhausted.")
    return 
  else:
    card = deck.pop(0)
    shutil.copyfile(card["o_path"], card["d_path"])

def clearDrawPile():
  global deck_dir

  print("Size of draw pile: ", len(os.listdir(deck_dir))) 
  if len(os.listdir(deck_dir)) == 0:
    writeInterface("Draw pile is empty.")
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
    




