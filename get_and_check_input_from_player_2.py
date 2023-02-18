def get_input(boardsize):
    myinput = input("Please input a number from 1 to " + str(boardsize * boardsize) + ": ")
    if int(myinput) < 1 or int(myinput) > int(boardsize * boardsize):
        print("sorry, out of range. ")
        get_input(boardsize)
    else:
        return myinput

#print(get_input(3))

def get_input1(boardsize):
    incheck = False;
    while incheck == False:   
        myinput = input("Please input a number from 1 to " + str(boardsize * boardsize) + ": ")
        if int(myinput) < 1 or int(myinput) > int(boardsize * boardsize):
            print("sorry, out of range. ")
        else:
            incheck = True;
    return myinput

#print(get_input1(3))



##THIS ONLY CHECKS IF THE NUMBER IS IN RANGE. But this is not enough. We also need to check the input
##is of the right type, for example not a word or random string.
##Here is the solution


def get_input2(boardsize):
    while True:
        try:
            myinput = int(input("Please input a number between 1 and " + str(boardsize * boardsize) + ": "))
        except ValueError:
            print("Sorry, not a number.",end=" ")
            continue                                    #this means, continue around the while loop
        if (myinput < 1 or myinput > boardsize * boardsize):
            print("Sorry, number is out of range.",end=" ")
            continue                 
        else:
            print("You input number " + str(myinput));
            break
    return myinput
        

#get_input2(3)

def get_input3(boardsize, takenlist):
    while True:
        try:
            myinput = int(input("Please input a number between 1 and " + str(boardsize * boardsize) + ": "))
        except ValueError:
            print("Sorry, not a number.",end=" ")
            continue                                    #this means, continue around the while loop
        if (myinput < 1 or myinput > boardsize * boardsize):
            print("Sorry, number is out of range.",end=" ")
            continue
        elif (myinput in takenlist):
            #complete code here
            continue   
        else:
            print("You input number " + str(myinput));
            break
    return myinput

#this is numbers taken in the noughts and crosses game that the code represents.
#takenlist = [1,5,9]
#get_input3(3,takenlist)