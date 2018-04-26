#write import statement for ScoreEntry

from src.homework.homework10.score_entry import ScoreEntry

#from score_entry import ScoreEntry

#create a class named GameLog with a parameterless constructor-create an empty list of score_entries class attribute in
# constructor
#Create a class method add_score_entry with a score_entry parameter, in the method code append the score_entry parameter
#to the score_entries class attribute
#Create a display_log method with no parameters-in this method iterate through display_log and display each
#score entry to screen

class GameLog:

    def __init__(self):
        self.score_entries = []

    def add_score_entry (self, score_entry):
        self.score_entries.append(score_entry)

    def display_log (self):
        for line in self.score_entries:
            print(line.score_entry_id,': Roll1 =',line.die1_value,'Roll2 =', line.die2_value)
