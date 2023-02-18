#this code is for any game that uses a square board. For the purposes of the session, we'll assume it's noughts
#and crosses, so the boardsize is 3 (as 3 x 3 is the board we need)

def get_input(boardsize):
    myinput = input("Please input a number from 1 to " + str(boardsize * boardsize) + ": ")
    return myinput

print(get_input(3))
