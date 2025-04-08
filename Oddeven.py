print("ENTER THE ODD EVEN NUMBER")
enter_the_number=int(input("enter the number that you want to check if odd or even"))
if(enter_the_number==1):
    print("the number is nor odd nor even")
elif (enter_the_number%2==0):
    print("the given number is an even number")
elif(enter_the_number%2!=0):
    print("the given number is an odd number")
else :
    print("please enter a valid number")
