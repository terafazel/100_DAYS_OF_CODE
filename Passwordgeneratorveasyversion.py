import random 
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['!', '@', '#', '$', '%', '^', '&', '*']
length_of_letters = int(input("Please input the number of letters you want in your password : "))
lenght_of_numbers=int(input("Please enter  the number of numerical numbers  that you would like in your password : "))
lenght_of_symbols=int(input("please enter the number of symbols that you want in your password : "))
random_letters=random.choices(letters, k=length_of_letters)
random_numbers=random.choices(numbers,k=lenght_of_numbers)
random_symbols=random.choices(symbols, k=lenght_of_symbols)
password_numbers=""
password_letters=""
password_symbols=""
for selected_password_letters in random_letters:
    password_letters += selected_password_letters
#print(password_letters)
for selected_password_numbers in random_numbers:
    password_numbers += selected_password_numbers
#print(password_numbers)
for selected_password_symbols in random_symbols:
    password_symbols += selected_password_symbols
#print(password_symbols)
print(f"your generated password that you can is {password_letters}{password_numbers}{password_symbols} ")