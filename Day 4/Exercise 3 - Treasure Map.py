map_list = [['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']]

for i in range (3):
    for j in range (3):
        print(f"{map_list[i][j]}", end = '')
    print("\n")

location = input("Where do you want to put the treasure? ");
map_list[int(location[1]) - 1][int(location[0]) - 1] = "x "

for i in range (3):
    for j in range (3):
        print(f"{map_list[i][j]}", end = '')
    print("\n")
