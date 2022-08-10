# This is the solution to Maze in the dropdown menu
# https://bit.ly/3JFR6Dr

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear() == True:
    move()
turn_left()
    
while at_goal() == False:
    if right_is_clear() == True:
       turn_right()
       move()
    elif front_is_clear() == True:
         move()
    else: 
         turn_left() 