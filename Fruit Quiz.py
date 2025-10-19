import random

class FruitQuiz:
    def __init__(self):


# Create a dictionary of fruits as keys and color as value
        self.fruits = {
            'apple' : 'red',
             'orange':'orange',
             'watermelon':'green',
            }
        
    def quiz(self):

        while(True):

            fruit , color = list(self.fruits.items())
            print("What is the color of {}".format(fruit))
            user_answer = input()
            if(user_answer.lower() == color):
                print("Correct Answer")
            else:
                print("Wrong Answer")

            option = int(input("Enter 0 ,  if you want to play otherwise enter 1"))
            if(option):
             break

print("Welcome to the fruit quiz")
fq = FruitQuiz()
fq.quiz()