import random
import math
print("Welcome to Sloth Quest!")
print("-----------------------")
print("")
print("You're currently at position (0,0) in the world.")
print("Available commands: ")
print("N - go north, S- go south, E - go east, W - go west, X - exit game")
#initialize game variable
game = 1
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
      break
    else: 
       print("Learn to read.")
    #Check player distance to goal/hazard and print message
    if (math.sqrt((xGoal - userX)**2 + ((yGoal - userY)**2)) < 2):
       print("You  feel good about this.")
    if ((math.sqrt((xHaz - userX)**2 + ((yHaz - userY)**2)) < 2)):
       print("You don't feel too good.")
    if (userX == xGoal and userY == yGoal):
       print("You reached Slothtopia!")
       game = int(input("Play again? Type 1 for yes, 2 for no."))
       if game == 1:
         restartgame()
         print("You're currently at position (0,0) in the world.")
    if (userX == xHaz and userY == yHaz):
       print("You've been captured by anti-sloth protestors!.")
       game = int(input("Play again? Type 1 for yes, 2 for no."))
       if game == 1:
         restartgame()
         print("You're currently at position (0,0) in the world.")
      

