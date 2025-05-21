import random
from designrps import rock,paper,scissors
game_images=[rock,paper,scissors]
user_choice=int(input("What do you choose? Type 0 for Rock ,1 for Paper or 2 for Scissors \n"))
if user_choice>=0 and user_choice<=2:
    print(game_images[user_choice])
computer_choice=random.randint(0,2)
print("computer choose:")
print(game_images[computer_choice])
if user_choice>=3 or user_choice<0:
    print("Enter a valid input")
elif user_choice==0 and computer_choice==2:
    print("You wins!")
elif user_choice==2 and computer_choice==0:
    print("You loose")
elif computer_choice>user_choice:
    print("You loose!")
elif user_choice==computer_choice:
    print("Draw")
elif user_choice>computer_choice:
    print("You wins!")