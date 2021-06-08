import deck
import interface

deck.createDeck()
deck.printDeck()

while True:
  messages = interface.read()

  for message in messages:
    print(message, end = "")
  print()

  user_choice = int(
    input("What would you like to do?\n \
      \t1) Draw card\n \
      \t2) Exit\n \
      \t3) Clear Hand\n \
      \t4) Draw Hand\n\n")) 

  # Draw card.
  if user_choice == 1:
    interface.write("Drawing a card:")
    deck.drawCard()
    interface.cls()
  
  # Exit.
  if user_choice == 2:
    # TODO: close all open files.
    interface.interface.close()
    exit(0)

  # Clear draw pile.  
  if user_choice == 3:
    interface.write("You cleared your hand.")
    deck.clearHand()
    interface.cls()

  # Draw hand.
  if user_choice == 4:
    interface.write("Drawing hand:")
    deck.drawHand()
    interface.cls()



  

