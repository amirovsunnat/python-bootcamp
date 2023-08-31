import time


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to the Treasure Island!")
print("You wake up on a deserted island. The sun is shining, and a sense of adventure fills the air.")

choice = input("Do you want to explore the island? (yes/no): ")

if choice.lower() == "yes":
    print("\nYou start walking and soon find yourself at a fork in the path.")
    print("To your left, there's a dense forest, and to your right, there's a rocky trail.")
    
    choice = input("Do you want to go left or right? ")
    
    if choice.lower() == "left":
        print("\nYou enter the forest. The air is cool, and birds are chirping above.")
        print("As you wander deeper, you stumble upon an old, abandoned campsite.")
        
        choice = input("Do you want to search the campsite or continue exploring? (search/continue): ")
        
        if choice.lower() == "search":
            print("\nAmong the debris, you find a torn piece of a map!")
            print("It seems to indicate something near the cave to the south.")
        elif choice.lower() == "continue":
            print("\nYou decide to keep exploring the forest.")
        else:
            print("\nInvalid choice. Your hesitation has led to confusion, and you're unable to proceed.")
            print("Game over.")
    elif choice.lower() == "right":
        print("\nYou follow the rocky trail uphill. The view from the top is breathtaking.")
        print("In the distance, you spot a sparkling object near a cave entrance to the south.")
        
        choice = input("Do you want to investigate the object or continue on the trail? (investigate/continue): ")
        
        if choice.lower() == "investigate":
            print("\nYou approach the cave entrance and find a locked treasure chest!")
            print("If only you had a key...")
        elif choice.lower() == "continue":
            print("\nYou continue along the trail, curious about what lies ahead.")
        else:
            print("\nInvalid choice. You're overcome by uncertainty and are unable to proceed.")
            print("Game over.")
    else:
        print("\nInvalid choice. Indecision holds you back, and your adventure ends prematurely.")
        print("Game over.")
else:
    print("\nYou decide not to explore. The mystery remains unsolved.")
