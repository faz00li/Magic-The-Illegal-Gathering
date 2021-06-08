import binascii
import os
import shutil
import sys

from diagnostic import CREATE_DECK_DIAG
import interface

# Global variable. List representing the deck.
deck = []
deck_size = 0

# Get current and deck directories.
cur_dir = os.getcwd()
deck_dir = cur_dir + "/Deck"
hand_dir = cur_dir + "/Hand"

def sortHelper(card):
  return card["d_path"]

def isEmpty():
  deck_empty = False

  if deck_size == 0:
    deck_empty = True 
  
  return deck_empty

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

def printDeck(debug = False):
  global deck
  global deck_size

  print("\n////////// PRINTING DECK //////////")
  
  if deck_size == 0:
    print("Deck: empty")
    print("///////////////////////////////////", end = "\n\n")
    return

  print("Cards: ", deck_size, )
  print("///////////////////////////////////", end = "\n\n")

  for card in deck:
    print("Card: ", card["name"])

    if debug == True:
      print("Card:    ", card["name"])
      print("Library: ", card["o_path"])
      print("Deck:    ", card["d_path"])
      print("Hand:    ", card["h_path"], end = '\n\n')
  
  print()

def dumpCard():
  global deck
  global deck_size

  # Check for empty deck.
  if isEmpty():
    interface.write("Deck is exhausted.")
    return

  # Remove card from list.
  card = deck.pop(0)

  # Copy file to Hand directory.
  try:
    shutil.copyfile(card["o_path"], card["d_path"])
  except Exception as e:
    print(e)
    # TODO possible additional mitigation steps needed.

  # Decrement deck size by 1.
  deck_size = deck_size - 1

  interface.write("Dumped: " + card["name"])

def dumpDeck():
  while deck_size > 0:
    dumpCard()

def drawCard() -> bool:
  global deck
  global deck_size

  # Check for empty deck.
  if isEmpty():
    interface.write("Deck is exhausted.")
    return False
    
  # Remove card from list.
  card = deck.pop(0)

  # Copy file to Hand directory.
  try:
    shutil.copyfile(card["o_path"], card["h_path"])
  except Exception as e:
    print(e)
    # TODO possible additional mitigation steps needed.

  # Decrement deck size by 1.
  deck_size = deck_size - 1

  interface.write("You drew: " + card["name"])

  return True

def clearHand():
  global hand_dir

  print("Size of draw pile: ", len(os.listdir(hand_dir))) 
  if len(os.listdir(hand_dir)) == 0:
    interface.write("Draw pile is empty.")
    return
  else:
    for f in os.listdir(hand_dir):
      os.remove(os.path.join(hand_dir, f))

def drawHand():
  print("////////// DRAWING HAND //////////")
  for i in range(6):
    drawn = drawCard()
    if drawn == False:
      break
      
  interface.write("{} cards drawn.".format(i))
  

# def putCardOnTopOfLibrary(str: card_name):
#   return None

# def shuffleLibrary():
#   return None
    




