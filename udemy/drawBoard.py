# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
#    --- --- ---
#   |   |   |   |
#    --- --- ---
#   |   |   |   |
#    --- --- ---
#   |   |   |   |
#    --- --- ---


rows = int(input("Enter the number of Rows in Board: "))
cols = int(input("Enter the number of Columns in Board: "))

print("So you want a board of size " + str(rows) + "x" + str(cols) + "! Great ! Here it is :")

for i in range(rows):
    for j in range(cols):
        print("|--", end="")

    print("|")



# Better answer

def board_draw(height, width):
    for x in range(height):
        print(" --- " * width)
        print("|   |" * width)
    print(" --- " * width)

heightinp= int(input("Enter the height of the board: "))
widthinp= int(input("Enter the width of the board: "))

board_draw(heightinp,widthinp)


