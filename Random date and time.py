import random

import time


def getRandomDate(starDate , EndDate):
    print("Printing random date between", starDate ,"and",EndDate)
    randomGenerator = random . random()
    dateFormat = '%m/%d/%Y'
    starttime = time . mktime(time.strptime(starDate ,dateFormat))
    endTime = time . mktime(time . strptime (EndDate , dateFormat))
    randomTime = starttime + randomGenerator * (endTime - starttime)
    
    randomDate = time . strftime(dateFormat , time . localtime(randomTime))
    return randomDate
    
print("Random Date =", getRandomDate ("1/1/2020", "12/12/2024"))