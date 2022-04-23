row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map_ = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
x = input("Where do you want to put the treasure? ")

y = int(x[0])
x = int(x[1])
map_[x-1][y-1] = "X"

print(f"{row1}\n{row2}\n{row3}")