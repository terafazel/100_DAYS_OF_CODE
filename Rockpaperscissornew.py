import random
print("Lets play the game rock paper scissor ")
user_choice=input("please input what is your choice \n rock paper or scissor" )
options_available=["rock","paper","scissor"]
computer_choice=random.choice(options_available)
if user_choice==computer_choice:
    print("its a tie")
elif user_choice=="rock" and computer_choice=="scissor":
    print("user wins")
elif user_choice=="rock" and computer_choice=="paper":
    print("computer wins")
elif user_choice=="paper" and computer_choice=="scissor":
    print("computer wins")
elif user_choice=="paper" and computer_choice=="rock":
    print("user wins")
elif user_choice=="scissor" and computer_choice=="paper":
    print("user wins")
elif user_choice=="scissor" and computer_choice=="rock":
    print("computer wins")

