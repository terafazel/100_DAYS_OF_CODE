print("Hi welcome to pizza palace")
Size=input("what size of pizza do you want small medium or large").lower()
if Size =="small":
    print("thank you for choosing small pizza your total cost is $15")
    pizzaprice=15
elif Size=="medium":
    print("thank you for choosing medium pizza the total cost is $20")
    pizzaprice=20
elif Size=="large":
    print("thank you for choosing large pizza the total cost is $25")
    pizzaprice=25
else: 
    print("please enter a valid input")
Topping=input("Do you want Topping answer in yes or no")
if Topping=="yes":
 Pepporni=input("Do you want pepporani answer in yes or no")
 if Pepporni=="yes":
    totalpriceonetpping=pizzaprice+2
    print(f"thank you for choosing the top up , the total cost {totalpriceonetpping}")
 else :
    print("Thank you")
 Cheese=input("Do you want cheese as a topping")
 if Cheese=="yes":
     totalpriceonetppingcheese=totalpriceonetpping+1
     print(f"thank you for choosing the top up , the total cost {totalpriceonetppingcheese}")
else:
    print("home")




