try :
    num = int(input("Enter your Number: "))
    print(num)


except ValueError as ex:
    print("Exception:", ex)


print("I am outside the try block")