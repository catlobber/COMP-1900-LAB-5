import random

#intialize variables
dicetoroll = 999
sidesperdie = 999
dicerolled = 1
total = 0
rolledvalue = 0
#While loop, looping to ask for input, print dice rolling, and then print total while reinitializing it to 0
while dicetoroll > 0 and sidesperdie > 0:
 dicetoroll = int(input("Number of dice to roll (any non-positive value to exit:) "))
 if (dicetoroll <= 0):
   break
 sidesperdie = int(input("Number of sides per die (any non-positive value to exit:) "))
 if (sidesperdie <= 0):
  break
 
 print(f"Rolling {dicetoroll}d{sidesperdie}")
 #Nested While loop, looping to roll the dice, print the value, and to add the total
 while dicerolled <= dicetoroll:
  rolledvalue = random.randint(1,sidesperdie)
  print(f"Die {dicerolled}: {rolledvalue}")
  total = total + rolledvalue
  dicerolled += 1
 print(f"Total: {total}")
 total = 0
   


