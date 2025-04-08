print("Ticket Calculator")

age_of_the_person = int(input("Please enter your age: "))

if age_of_the_person < 12:
    print("The ticket price is $5")
    ticket_price = 5
elif age_of_the_person < 18:
    print("The ticket price is $7")
    ticket_price = 7
elif age_of_the_person < 25:
    print("The ticket price is $12")
    ticket_price = 12
else:
    print("The ticket price is $15")
    ticket_price = 15

popcorn = input("Do you want popcorn? (yes or no): ").lower()
if popcorn == "yes":
    ticket_price += 3
    print(f"Your final ticket price with popcorn is ${ticket_price}")
else:
    print(f"Your final ticket price is ${ticket_price}")
   