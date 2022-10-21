print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
a = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n").lower()
if (a == "left"):
  b = input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across\n").lower()
  if (b == "swim"):
    print("Game Over.")
  elif (b == "wait"):
    c = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. which colour do you choose?\n").lower()
    if (c == "red") or (c == "blue"):
      print("Game Over.")
    elif (c == "yellow"):
      print("You Win!")
elif (a == "right"):
    print("Game Over.")