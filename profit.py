costprice = int(input("Enter the cp: "))
sellingprice = int(input("Enter the sp: "))

if(sellingprice>costprice):
    print("There is Profit")
    profit = sellingprice - costprice
    print(profit)
else:
    print("No Profit")