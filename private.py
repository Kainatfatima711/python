class myClass:

    __privateVar = 27


    def __privMeth(self):
        print("I am inside myClass") # ENCAPSULATED OR PRIVATE / NO OBJECT CAN USE IT


    def hello(self):
        print("Private Variable value: " , myClass.__privateVar)

myobject = myClass()
myobject.hello()
myobject.__privateVar
