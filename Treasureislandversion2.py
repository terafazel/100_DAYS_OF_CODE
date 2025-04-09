print("🏝️ Welcome to Treasure Island 🏝️\nYour mission is to find the treasure! 💰\n")

Answerone = input("🚶 You are at a crossroad. Where do you want to go? \n👉 Type 'left' or 'right': ").lower()

if Answerone == "left":
    AnswerTwo = input("\n🌊 You've come to a lake. There is an island in the middle of the lake.\n⛵ Do you want to 'swim' or 'wait' for a boat? \n👉 Type 'swim' or 'wait': ").lower()
    if AnswerTwo == "wait":
        AnswerThree = input("\n🏠 You arrive at the island unharmed. You see three doors in front of you: one red 🚪, one blue 🚪, and one yellow 🚪.\nWhich door do you choose? \n👉 Type 'red', 'blue', or 'yellow': ").lower()
        if AnswerThree == "red":
            print("\n🔥 Burned by fire! \n💀 GAME OVER.")
        elif AnswerThree == "blue":
            print("\n🐻 You are eaten by beasts! \n💀 GAME OVER.")
        elif AnswerThree == "yellow":
            print("\n🎉 You found the treasure! You WIN! 🏆💰")
        else:
            print("\n🚫 Invalid choice. \n💀 GAME OVER.")
    else:
        print("\n🐟 You were attacked by a trout. \n💀 GAME OVER.")
else:
    print("\n🕳️ You fell into a hole. \n💀 GAME OVER.")
