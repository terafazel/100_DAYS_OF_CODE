print("welcome to the percentage calculator please type in your marks in the given order")
enligsh_marks=int(input("what is your marks in english"))
hindi_marks=int(input("what is your hindi marks"))
marathi_marks=int(input("what is your marathi marks"))
#now that you have entered the marks lets see if yoave have failed oer passed 
total_marks=enligsh_marks+hindi_marks+marathi_marks
if total_marks>90:
    print("you have passsed")
elif total_marks >80 and total_marks<90:
    print("you have been good")
elif total_marks>70 and total_marks <=80:
  print("you are average")
else :
   print("sorry babau you havent cleared the exams")
