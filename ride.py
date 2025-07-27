print("Select you ride : ")
print("1.Bike")
print("2.Car ")

Choice = int(input("Enter your choice : "))

if(Choice == 1):
    print("What type of Bike ? ")
    print("1.Scooty")
    print("2.Scooter") 

    choicebike  = int(input("Enter your choice of bike : "))

    if choicebike == 1:
     print("You hace selected Scooty")
    else:
     print("You have selected Scooter") 




elif choice == 2 :
   print("What type of car ? ")
   print("1.Sedan")
   print("2.XUV")
   choicecar=int(input("Enter your choice of the car : "))
   if choicecar == 1:
     print("You have selected Sedan")
   else:
     print("You have selected XUV")
      

else:
  print("Invalid Choice!")