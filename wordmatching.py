l1 =[3 , 7 , 1 , 8 , 9 , 2 , 4 , 5 , ]

l1.sort()
print(l1)

sum = 0
for i in l1:
    sum = sum+i
print("sum=",sum)

avg=sum/len(l1)
print("avg=",avg)

maxi=max(l1)
print("max=",maxi)

mini=min(l1)
print("min=",mini)
