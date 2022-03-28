ahead=None
winFlag = 100
turns =0

player1=0
player1_open=None
player2=0
player2_open=None

def checkWin(x):
    if (x>=winFlag):
        return True

def caseOFsix():
    global turns
    global player1_open
    global player2_open

    if(i == 0):
        player1_open = True
    else:
        player2_open = True

    turns += 1
    temp = int(input("You rolled a six, you get to roll again: "))


    if (temp == 6):
        if(turns < 2):
            return caseOFsix()
        elif(turns == 2):
            if(temp==6):
                print("Alas! You have rolled 3 consecutive sixes")
                if player1_open is None:
                    player1_open == False
                elif player2_open is None:
                    player2_open == False
                turns = 0
                return 0
            else:
                results = turns*6+temp
                turns = 0
                return results
    else:
        results = turns*6 + temp
        turns = 0
        return results

while(True):
    if(player1 > player2):
            ahead = "Player 1"
    else:
            ahead = "Player 2"
    if(checkWin(player1) or checkWin(player2)):
        print("Winner is: ", ahead)
        break
    for i in [0,1]:
        if(checkWin(player1) or checkWin(player2)):
            break
        if(i==0):
            x=int(input("Player_1, Enter the number you just rolled: "))
            if(x==6):
                player1 += caseOFsix()
            elif(player1_open == True):
                player1+=x
            else:
                print("You have to roll a six to start")
            print("Player_1 score:", player1)
        elif(i==1):
            y=int(input("Player_2, Enter the number you just rolled: "))
            if(y==6):
                player2 += caseOFsix()
            elif(player2_open == True):
                player2+=y
            else:
                print("You have to roll a six to start")
            print("Player_2 score:", player2)
