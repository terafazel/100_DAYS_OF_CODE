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
new_list = random_letters + random_numbers + random_symbols  # ✅ flat list
random.shuffle(new_list)
new_password = ''.join(new_list)  # join characters into one string
print(new_password)
