#Tic Tac Tok
checkplaces = [i for i in range(1,11)]
player1 = True
winner = -1
countplay = 0
player1sign = 'X'
player2sign = 'O'
def checkselection(selection,checkplace):
    if(i in range(1, 11)):
        return type(checkplace[selection-1]) == int
    else:
        return False


def checkwinner(signs, checkplace):
    options = {'1sthor': [i for i in range(0, 3)],
               '2ndhor': [ i for i in range(3, 6)],
               '3ndhor': [i for i in range(6, 9)],
               '1stvert': [i for i in range(0, 9,3)],
               '2ndvert': [i+1 for i in range(0, 9, 3)],
               '3ndvert': [i+2 for i in range(0, 9, 3)],
               'line1': [0,4,8],
               'line2': [2, 4, 6]}
    for option in options.values():
        checkoptions = []
        for item in option:
            checkoptions.append(checkplace[item])
        alloption = set(checkoptions)
        neededoption = set(signs)
        if(neededoption == alloption):
            return True



while winner < 0 :
    print("-------------------")
    print("|     |     |     |")
    print("|  {}  |  {}  |  {}  |".format(checkplaces[0], checkplaces[1], checkplaces[2]))
    print("-------------------")
    print("|     |     |     |")
    print("|  {}  |  {}  |  {}  |".format(checkplaces[3], checkplaces[4], checkplaces[5]))
    print("-------------------")
    print("|     |     |     |")
    print("|  {}  |  {}  |  {}  |".format(
        checkplaces[6], checkplaces[7], checkplaces[8]))
    print("-------------------")
    if(player1):
        selection= input('Player1 ,Please Select number: ')
        if not checkselection(selection, checkplaces):
            print("This Selection was done before")
            continue
        checkplaces[selection-1] = player1sign
        if checkwinner(player1sign, checkplaces):
            print("Player 1 Wins!")
            break
    else:
        selection = input('Player2 ,Please Select number: ')
        if not checkselection(selection, checkplaces):
             print("This Selection was done before")
             continue
        checkplaces[selection-1] = player2sign
        checkselection(selection, checkplaces)
        if checkwinner(player2sign, checkplaces):
            print("Player 2 Wins!")
            break

    player1 = not player1
    if(countplay > 7):
        print("No Winner Draw!")
        break
    countplay+=1
