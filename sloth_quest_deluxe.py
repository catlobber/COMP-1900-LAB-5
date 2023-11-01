import random
import math
print("Welcome to Sloth Quest!")
print("-----------------------")
print("")
print("You're currently at position (0,0) in the world.")
print("Available commands: ")
print("N - go north, S- go south, E - go east, W - go west, X - exit game")
#initialize game variable and statistics variables
game = 1
abandoned = 0
lost = 0
won = 0
avgwin = 0.0
maxwin = 0
minwin = 0
gamesplayed = 0
totalmovement = 0
#create stats function to display game stats
def stats():
  global maxwin
  global minwin
  global avgwin
  #For the first win, min and max are the same but after the first win check the max and minimum moves to win and change them
  if won == 1:
     maxwin = movement
     minwin = movement
  elif won > 1:
     if maxwin < movement:
         maxwin = movement
     if minwin > movement:
         minwin = movement
  avgwin = (totalmovement / won)
  print("Your Statistics So Far")
  print("----------------------")
  print(f"Games Won: {won}/{gamesplayed}")
  print(f"Games Lost: {lost}/{gamesplayed}")
  print(f"Games Abandoned: {abandoned}/{gamesplayed}")
  print(f"Average moves to win: {avgwin}")
  print(f"Minimum moves to win: {minwin}")
  print(f"Maximum moves to win: {maxwin}")

 
#create restartgame function to reset all game variables
def restartgame():
#Create goal and hazard coordinate
 global xHaz
 xHaz = (random.randint(-7,7))
 global yHaz
 yHaz = (random.randint(-7,7))
 global yGoal
 yGoal = (random.randint(-7,7))
 global xGoal
 xGoal = (random.randint(-7,7))
#check to see if either goal or hazard is at 0,0 or have same position
 if (xGoal == 0 and yGoal == 0):
  xGoal = (random.randint(-7,7))
  yGoal = (random.randint(-7,7))
 if (xHaz == 0 and yHaz == 0):
  xHaz = (random.randint(-7,7))
  yHaz = (random.randint(-7,7))
 if (xGoal == xHaz and yGoal == yHaz):
  xGoal = (random.randint(-7,7))
  yGoal = (random.randint(-7,7))
  xHaz = (random.randint(-7,7))
  yHaz = (random.randint(-7,7))
#initialize user's coordinates and movement counter
 global userX 
 userX = 0
 global userY 
 userY = 0
 global movement 
 movement = 0
restartgame()
print("Welcome to Sloth Quest!")
print("-----------------------")
print("")
print("You're currently at position (0,0) in the world.")
print("Available commands: ")
print("N - go north, S- go south, E - go east, W - go west, X - exit game")
#While Loop, checking for user inputs to see where they want to move and checking for if they reached the hazard/goal. If either is reached, the game ends and text is shown.
#Also, add a counter variable for moves and print them
while game == 1:
    direction = input("Enter command: ")
    if direction == "N":
     userY += 1
     movement += 1
     print(f"Moving north to {userX}, {userY} [moves taken: {movement}]")
    elif direction == "S":
     movement += 1
     userY -= 1
     print(f"Moving south to {userX}, {userY} [moves taken: {movement}]")
    elif direction == "E":
     movement += 1
     userX += 1
     print(f"Moving east to {userX}, {userY} [moves taken: {movement}]")
    elif direction == "W":
     movement += 1
     userX -= 1
     print(f"Moving west to {userX}, {userY} [moves taken: {movement}]")
    elif direction == "X":
      abandoned += 1
      gamesplayed += 1
      break
    else: 
       print("Learn to read.")
    #Check player distance to goal/hazard and print message
    if (math.sqrt((xGoal - userX)**2 + ((yGoal - userY)**2)) < 2):
       print("You  feel good about this.")
    if ((math.sqrt((xHaz - userX)**2 + ((yHaz - userY)**2)) < 2)):
       print("You don't feel too good.")
    #Print win/loss statements and display statistics
    if (userX == xGoal and userY == yGoal):
       print("You reached Slothtopia!")
       won += 1
       gamesplayed += 1
       totalmovement += movement
       stats()
       game = int(input("Play again? Type 1 for yes, 2 for no."))
       if game == 1:
         restartgame()
         print("You're currently at position (0,0) in the world.")
    if (userX == xHaz and userY == yHaz):
       print("You've been captured by anti-sloth protestors!.")
       lost += 1
       gamesplayed += 1
       stats()
       game = int(input("Play again? Type 1 for yes, 2 for no."))
       if game == 1:
         restartgame()
         print("You're currently at position (0,0) in the world.")
      

