row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

column = int(position[0])
row = int(position[1])

if column > 3 or row > 3:
    print("That value is out of range")
    exit()
#Write your code below this row 👇
map[row - 1][column - 1] = "X"





#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")