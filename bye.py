valid = False

while not valid:

 try :
    number =int(input("Enter a number: ")) # 4


    while number%2 == 0: # 4 / 2 = 0
        print("Bye")
        valid = True


 except ValueError:
    print("Invalid")
