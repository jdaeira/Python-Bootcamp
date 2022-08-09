def turn_right():
    turn_left()
    turn_left()
    turn_left()

while at_goal() == False:
    if wall_in_front() == True and wall_on_right() == True:
        turn_left()
    elif right_is_clear() == True:
        turn_right()
        move()
    elif front_is_clear() == True:
         move()
    else: 
         right_is_clear() == True and wall_in_front() == True
         turn_right()



def turn_right():
    turn_left()
    turn_left()
    turn_left()

while at_goal() == False:
    if right_is_clear() == True:
       turn_right()
       if wall_in_front() == True and wall_on_right() == True:
          turn_left()
       else:
          move()
    elif front_is_clear() == True:
         move()
    else: 
        wall_in_front() == True and wall_on_right() == True
        turn_left() 