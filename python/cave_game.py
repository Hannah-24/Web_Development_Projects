import random

print("===== The Cave Adventure =====")
print("You're trapped in a cave. Find the exit and escape!")
print("Type 'left', 'right', or 'quit' to play. \n")

health = 100
treasure = 0

while health > 0:
     print(f"\nHealth: {health} | Treasure: {treasure}")
     choice = input("You see 2 paths. Go left, right, or quit? ").lower()

     if choice == "quit":
          print("You quit. Game over.")
          break
     elif choice == "left":
          event = random.choice(["trap", "treasure", "empty"])
          if event == "trap":
               damage = random.randint(10, 30)
               health -= damage
               print(f"Ouch! A trap! You lose {damage} health.")
          elif event == "treasure":
               gold = random.randint(5, 20)
               treasure += gold
               print(f"You found {gold} gold coins!")
          else:
               print(f"It's just an empty tunnel. Nothing happens.")

     elif choice == "right":
          event = random.choice(["monster","treasure", "exit"])
          if event == "monster":
               damage = random.randint(20, 40)
               health -= damage
               print(f"A goblin attacks! You lose {damage} health.")
          elif event == "treasure":
               gold = random.randint(10, 30)
               treasure += gold
               print(f"Wow! You found {gold} gold coins!")
          elif event == "exit":
               print(f"\nYou found the exit! You escape with {treasure} gold.")
               print("You win.")
               break
     else:
          print("Invalid choice. Type 'left', 'right', or 'quit'.")

     if health <= 0:
          print(f"\nYou died in the cave. Game over.")

print(f"\nFinal Score: {treasure} gold ")