def cube(number):
    return number * number * number



def by_three(number):
    if number % 3 == 0:
        return cube (number)
    else:
        return"Cube not possible ,not dividible by 3"
    

print(by_three(9))
print(by_three(4))