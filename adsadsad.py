
def determine_grade(score):
    if (90 <= score) and (score <= 100):
        print("A")
    elif (80 <= score) and (score <= 89):
        print("B")
    elif (70 <= score) and (score <= 79):
        print("C")
    elif (60 <= score) and (score <= 69):
        print("D")
    elif ( 60 > score):
        print("F")
    return score
def calc_average(n1,n2,n3,n4,n5):
    average = float(n1+n2+n3+n4+n5)/5
    determine_grade(n1)
    determine_grade(n2)
    determine_grade(n3)
    determine_grade(n4)
    determine_grade(n5)
    print(average)
    return average 
score1 = int(input("Enter your grade"))
score2 = int(input("Enter your grade"))
score3 = int(input("Enter your grade"))
score4 = int(input("Enter your grade"))
score5 = int(input("Enter your grade"))
calc_average(score1,score2,score3,score4,score5)
def stats():
 print("Your Statistics So Far")
 print("----------------------")
 print(f"Games Won: {won}/{gamesplayed}")
 print(f"Games Lost: {lost}/{gamesplayed}")
 print(f"Games Abandoned: {abandoned}/{gamesplayed}")
 if won == 1:
     maxwin = movement
     minwin = movement
 elif won > 1:
     if maxwin < movement:
         maxwin = movement
     if minwin > movement:
         minwin = movement
 
 avgwin += (movement / gamesplayed)
