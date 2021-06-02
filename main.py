import deck

mdeck = deck.createDeck()

for card in mdeck:
  print(card["name"])

def readFromInterface():
  global msg
  deck.interface.seek(0,0)
  msg = deck.interface.readline()
  deck.interface.truncate()
  deck.interface.seek(0,0)

while True:
  readFromInterface()
  print(msg)
  user_choice = int(
    input("What would you like to do?\n \
      \t1) Draw card\n \
      \t2) Exit\n \
      \t3) Clear Draw Pile\n\n")) 

  # Draw card.
  if user_choice == 1:
    deck.drawCard()
    deck.cls()
    deck.interface.truncate()
    deck.interface.write("You drew a card.")
  
  # Exit.
  if user_choice == 2:
    # TODO: close all open files.
    exit(0)

  # Clear draw pile.  
  if user_choice == 3:
    deck.clearDrawPile()
    deck.cls()
    deck.interface.truncate()
    deck.interface.write("You cleared the draw pile.")
  

