print("Welcome to Deepracer a ride for all ages")
Height = int(input("Please enter your Height"))
if Height >=120 :
 print("you are allowed to enter the ride")
 Age=int(input("enter your age"))
 if Age>18:
    print("you costing is $12")
    Ticketprice=12
 elif Age <18 and Age>12 :
   print("you costing is $7")
   Ticketprice=7
 elif Age<12:
   print("the costing is $5")
   Ticketprice=5
 Photos=bool(input("Do you waant to take a photos, answer in true or false"))
 if Photos==True:
   print(f"you will be charged additional $3, your total cost is {Ticketprice+3}")
 else:
   print(f"your costing is : {Ticketprice}")
else:
 print("Apologies but you are not eliglble to enter the ride")
