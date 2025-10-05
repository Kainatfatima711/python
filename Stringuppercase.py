class IOString():


    def __init__(self): # def __init__ (self) THIS FUNCION BELONGS TO PYTHON
        self.str1 = ""


    def get_String(self): # def get_String (self) THIS FUNCTION IS CREATED BY ME METHOD
        self.str1 = input("Enter String: ")


    def prin_String(self):
        print("Result is: " , self.str1.upper())

# Object Creation
str1 = IOString()

#Call Functions
str1.get_String()
str1.prin_String()