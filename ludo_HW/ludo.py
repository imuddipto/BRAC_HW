winner=None
winFlag = 100

player1=0
player1_open=None
player2=0
player2_open=None

def checkWin(x):
    if (x>=winFlag):
        return True

def caseOFsix():
    global player1
    global player1_open
    global player2
    global player2_open
    if(i==0):
        temp1=int(input("You rolled a six, you get another chance: "))
        if(temp1==6):
            temp2=int(input("You already rolled two sixes in a row, be careful: "))
            if(temp2==6):
                print("You rolled 3 sixes in a row,the other player gets a chance now")
                return 0
            else:
                if ( player1_open is None):
                    player1_open = True
                return 6+temp1+temp2
        else:
            if (player1_open is None):
                player1_open = True
            return 6+temp1
    elif(i==1):
        player2_open=False
        temp3=int(input("You rolled a six, you get another chance: "))
        if(temp3==6):
            temp4=int(input("You already rolled two sixes in a row, be careful: "))
            if(temp4==6):
                print("You rolled 3 sixes in a row,the other player gets a chance now")
                return 0
            else:
                if(player2_open is None):
                    player2_open = True
                return 6+temp3+temp4
        else:
            if(player2_open is None):
                player2_open = True
            return 6+temp3

while(True):
    if(checkWin(player1) or checkWin(player2)):
        print("Winner is: ", winner)
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
            if(player1 > player2):
                winner = "Player 1"
            else:
                winner = "Player 2"
            print("Player_1 score:", player1)
        elif(i==1):
            y=int(input("Player_2, Enter the number you just rolled: "))
            if(y==6):
                player2 += caseOFsix()
            elif(player2_open == True):
                player2+=y
            else:
                print("You have to roll a six to start")
            if(player1 > player2):
                winner = "Player 1"
            else:
                winner = "Player 2"
            print("Player_2 score:", player2)
