from src.homework.homework10.player import Player
from src.homework.homework10.game_log import GameLog
#write import statement for GameLog class

#from player import Player
#from game_log import GameLog

#Create a game log instance
gamelog1 = GameLog()

#SEnd the game_log instance to Player class as an argument
Player(gamelog1).roll_doubles()


#call the game log display method below

GameLog.display_log(gamelog1)
