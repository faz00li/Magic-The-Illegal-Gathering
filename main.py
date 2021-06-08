import deck

def readInterface():
  deck.interface.seek(0)
  msg = deck.interface.readlines()
  deck.interface.seek(0)
  deck.interface.truncate()
  return msg

deck.createDeck()
deck.printDeck()

while True:
  messages = readInterface()
  for message in messages:
    print(message)

  user_choice = int(
    input("What would you like to do?\n \
      \t1) Draw card\n \
      \t2) Exit\n \
      \t3) Clear Hand\n \
      \t4) Draw Hand\n\n")) 

  # Draw card.
  if user_choice == 1:
    deck.interface.write("Drawing a card:")
    deck.drawCard()
    deck.cls()
  
  # Exit.
  if user_choice == 2:
    # TODO: close all open files.
    deck.printDeck()
    exit(0)

  # Clear draw pile.  
  if user_choice == 3:
    deck.interface.write("You cleared your hand.")
    deck.clearHand()
    deck.cls()

  # Draw hand.
  if user_choice == 4:
    deck.interface.write("Drawing hand:")
    deck.drawHand()
    deck.cls()



  

