
###   Noughts and Crosses Game   ###

def DisplayBoard(board):
    print("\n+-----+-----+-----+","\n|     |     |     |",\
          "\n| ",board[0][0]," |","",board[0][1]," |","",board[0][2]," |"\
          "\n|     |     |     |","\n+-----+-----+-----+","\n|     |     |     |",\
          "\n| ",board[1][0]," |","",board[1][1]," |","",board[1][2]," |"\
          "\n|     |     |     |","\n+-----+-----+-----+","\n|     |     |     |",\
          "\n| ",board[2][0]," |","",board[2][1]," |","",board[2][2]," |"\
          "\n|     |     |     |","\n+-----+-----+-----+","\n")

def EnterMove(board,PlayerName):
    try:
        print(PlayerName,end="")
        move=int(input("'s turn, enter a number to make your move: "))
        if move in MakeListOfFreeFields(board):
            for i in board:
                for y in i:
                    if y==move and move<4:
                        i.insert(y,"O")
                        del i[(y-1)]
                        return board
                    elif y==move and move>3 and move<7:
                        i.insert(y-3,"O")
                        del i[(y-4)]
                        return board
                    elif y==move and move>6:
                        i.insert(y-6,"O")
                        del i[(y-7)]
                        return board
        print("\nInvalid Move!\n")
        EnterMove(board,PlayerName)
    except Exception:
        print("\nInvalid Move!\n")
        EnterMove(board,PlayerName)
    
def MakeListOfFreeFields(board):
    freespace=[]
    for i in board:
        for y in i:
            if y in range(1,10):
                freespace.append(y)       
    return freespace

def VictoryFor(board,sign):
    win=(sign,sign,sign)
    for x in range(3):
        if x!=1:
            diagcheck=board[0][x],board[1][1],board[2][(-x)+2]
        rowcheck=tuple(board[x][0:3])
        columncheck=board[0][x],board[1][x],board[2][x]
        if rowcheck==win or columncheck==win or diagcheck==win:
            return True

def DrawMove(board):
    from random import randrange
    move=randrange(1,10)
    if move in MakeListOfFreeFields(board):
        for i in board:
            for y in i:
                if y==move and move<4:
                    i.insert(y,"X")
                    del i[(y-1)]
                    return board
                elif y==move and move>3 and move<7:
                    i.insert(y-3,"X")
                    del i[(y-4)]
                    return board
                elif y==move and move>6:
                    i.insert(y-6,"X")
                    del i[(y-7)]
                    return board
    DrawMove(board)

def PlayerNameInput(scores):
    global PlayerName
    print("")
    PlayerName=str.capitalize(str.strip(input("Who's playing? ")))
    if PlayerName not in scores:
        scores[PlayerName]=0
        print("\nWelcome to Noughts and Crosses ",PlayerName,\
              ".\n\nThe Computer will be X and take the first turn:",sep="")
        time.sleep(3)
    return PlayerName,scores

def PlayGame(scores):
    board=[[1,2,3],[4,"X",6],[7,8,9]]
    PlayerNameInput(scores)
    DisplayBoard(board)
    for turns in range(4):
        EnterMove(board,PlayerName)
        DisplayBoard(board)
        if VictoryFor(board,"O"):
            print(PlayerName,"wins!","\n")
            score=scores[PlayerName]
            score+=1
            scores[PlayerName]=score
            again=input("Play again? Enter Y or N: ")
            if again.upper()=="Y":PlayGame(scores)
            return scores
        print("Computer's move:")
        time.sleep(1)
        DrawMove(board)
        DisplayBoard(board)
        if VictoryFor(board,"X"):
            print("Computer wins!","\n")
            score=scores["Computer"]
            score+=1
            scores["Computer"]=score
            again=input("Play again? Enter Y or N: ")
            if again.upper()=="Y":PlayGame(scores)
            return scores
    print("It's a Draw.","\n")
    again=input("Play again? Enter Y or N: ")
    if again=="Y":PlayGame(scores)
    return scores    

import time
loadingwidget="Loading Noughts and Crosses, Please wait..."
for i in loadingwidget:
    print(i,end="")
    time.sleep(0.1)
print("")
time.sleep(2)
scores={"Computer":0}
PlayGame(scores)
print("\nScores at the end of play:\n")
time.sleep(2)
overallwin=[0,0]
for player,points in scores.items():
    print(player.center(10,"~"),":",points)
    if points>overallwin[1]:
        overallwin=[player,points]
time.sleep(1)
if overallwin[1]==1:
    print("\nThe overall winner with ",overallwin[1]," point is ",overallwin[0],". Well Done!",sep="")
    print("\nGoodbye.")
else:
    print("\nThe overall winner with ",overallwin[1]," points is ",overallwin[0],". Well Done!",sep="")
    print("\nGoodbye.")
