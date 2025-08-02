number = int(input("Enter the whole number: "))

sum = 0

#Iterate from 1 to n(inclusive)
for i in range(1, number + 1):
    sum = sum + i

#Print the result
print("\nsum =", sum)