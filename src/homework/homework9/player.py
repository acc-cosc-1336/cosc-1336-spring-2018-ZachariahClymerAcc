#write import statement for Die class
from src.homework.homework9.die import Die
'''
Create a Player class.

'''

class Player:

    def __init__(self):
        '''
        Constructor method creates two Die attributes die1 and die2
        '''

        self.dice1 = Die()
        self.dice2 = Die()


    def roll_doubles(self):
        '''
        The roll_doubles method that will roll die1 and die2 (attributes from constructor method),
        display rolled values,and continue iterating until a double is rolled.
        '''
        dice1 = 1
        dice2 = 2
        
        while dice1 != dice2:
            dice1 = self.die1.roll()
            dice2 = self.die2.roll()
            print('You Rolled: ', dice1, dice2)
            
        if dice1 == dice2:
            print('Ay! You got doubles!', dice1, dice2)
