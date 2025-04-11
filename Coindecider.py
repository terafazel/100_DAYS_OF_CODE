import random
print("welcome to toss , please choose heads or tails")
player_1=input("what is it that you want heads or tails")
if player_1=="heads":
   player_2="tails"
elif player_1=="tails":
     player_2="heads"
choice_list=["heads","tails"]
reuslt=random.choice(choice_list)
if reuslt=="heads" and player_1=="heads":
    print("player 1 wins")
elif reuslt=='heads' and player_2=="heads":
    print("player 2 wins")
elif reuslt=="tails" and player_1=="tails":
    print("player 2 wins")
elif reuslt=="tails" and player_2=="tails":
    print("player 2 wins")