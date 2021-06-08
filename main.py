import deck

def readInterface():
  deck.interface.seek(0)
  msg = deck.interface.readline()
  deck.interface.seek(0)
  deck.interface.truncate()
  return msg

deck.createDeck()
deck.printDeck()



# while True:
#   print(readInterface())
#   user_choice = int(
#     input("What would you like to do?\n \
#       \t1) Draw card\n \
#       \t2) Exit\n \
#       \t3) Clear Draw Pile\n\n")) 

#   # Draw card.
#   if user_choice == 1:
#     deck.drawCard()
#     deck.cls()
#     deck.interface.write("You drew a card.")
  
#   # Exit.
#   if user_choice == 2:
#     # TODO: close all open files.
#     exit(0)

#   # Clear draw pile.  
#   if user_choice == 3:
#     deck.clearDrawPile()
#     deck.cls()
#     deck.interface.write("You cleared the draw pile.")
  

