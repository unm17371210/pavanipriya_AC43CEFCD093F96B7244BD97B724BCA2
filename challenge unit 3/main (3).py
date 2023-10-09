# Define the base class player

class player:
  def play(self):
    print("The player is playing cricket.")

# Define the derived class Batsman

class Batsman(player):
 def play(self):
    print("The batsman is batting.")

# Definr the derived class Bowler

class Bowler(player):
  def play(self):
    print("The bowler is bowling.")

# Creating objects of batsman and bowler classes

batsman = Batsman() 
bowler = Bowler() 

# Call the play() method for each object

batsman. play() 
bowler. play() 