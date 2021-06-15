import deck
import interface

end_game = False

def endGame():
  interface.interface.close()
  exit(0)

deck.createDeck()
deck.printDeck(True)
deck.printUniqueCards()

while True:
  messages = interface.read()

  for message in messages:
    print(message, end = "")
  print()

  if end_game == True:
    endGame()

  try:
    user_choice = int(
      input("What would you like to do?\n \
        \t1) Draw card\n \
        \t2) Exit\n \
        \t3) Clear Hand\n \
        \t4) Draw Hand\n \
        \t5) Print Deck\n \
        \t6) Dump Deck and Exit\n \
        \t7) Print Unique Cards\n \
        \t8) Put card on top of library\n \
        \n\n")) 
  except Exception as e:
    print(e)
    interface.cls()
    continue

  # Draw card.
  if user_choice == 1:
    interface.write("Drawing a card:")
    deck.drawCard()
    interface.cls()
  
  # Exit.
  if user_choice == 2:
    endGame()
    
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

  # Print Deck.
  if user_choice == 5:
    interface.cls()
    deck.printDeck(True)

  # Dump Deck.
  if user_choice == 6:
    interface.write("Dumping deck:\n")
    deck.dumpDeck()
    interface.cls()
    end_game = True

  # Print unique cards.
  if user_choice == 7:
    interface.cls()
    deck.printUniqueCards()

  # Print unique cards.
  if user_choice == 8:
    interface.write("Putting card on top of library:")
    deck.putCardOnTopOfLibrary()
    interface.cls()
  




  

