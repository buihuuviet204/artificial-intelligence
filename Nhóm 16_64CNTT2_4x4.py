import pygame
import time
pygame.init
a = int(input("Nhap lua chon: 1.Anphabeta vs minimax 2.Minimax vs anphabeta: "))
board = {1: ' ', 2: ' ', 3: ' ',4: ' ',
        5: ' ', 6: ' ', 7: ' ', 8: ' ',
        9: ' ',10: ' ',11: ' ', 12: ' ',
        13: ' ',14: ' ',15: ' ', 16: ' '}
computer = computer2 = ' '
x = []
def printBoard(board):
    print(board[1] + "|" + board[2] + "|" + board[3] + "|" + board[4])
    print("-+-+-+-")
    print(board[5] + "|" + board[6] + "|" + board[7] + "|" + board[8])
    print("-+-+-+-")
    print(board[9] + "|" + board[10] + "|" + board[11] + "|" + board[12])
    print("-+-+-+-")
    print(board[13] + "|" + board[14] + "|" + board[15] + "|" + board[16])
    print("\n")

def spaceIsFree(position):
    if board[position] == ' ':
        return True 
    return False 

def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter 
        printBoard(board)
        if checkWin():
            if letter == computer:
                print("Computer1 wins!")
                exit()
            else:
                print("Computer2 wins")
                exit()
        if checkDraw():
            print("Draw!")
            exit()
def checkWin():
    for i in range (4):
        if board[i*4 + 4] == board[i*4+1] == board[i*4+2] == board[i*4+3] and board[i*4+1] != ' ' :
            return True
        if board[0*4 + i +1] == board[2*4+i+1] == board[3*4+i+1] == board[1*4+i+1] and board[0*4+i+1] != ' ' :
            return True
    if board [1] == board [6] == board[11] == board[16] and board[1] != ' ':
        return True
    if board [4] == board [7] == board[10] == board[13] and board[4] != ' ':
        return True
    return False
def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False 
    return True 
def compMove(mark1,mark2):
    bestScore = -200
    bestMove = 0
    a = -100
    b = 100
    start = time.time()
    for key in board.keys():
        if board[key] == ' ':
            x.append(1)
            board[key] = mark1
            score = anphabeta(board,5,mark1,mark2,False,a,b)
            board[key] = ' '
            if score > bestScore:
                bestScore = score 
                bestMove = key
    end = time.time()
    print("Diem cua nuoc di: ",bestScore)
    print("Thoi gian chay: ",end-start)
    print("So nut duyet: ",len(x))
    x.clear()
    insertLetter(mark1, bestMove)
def compMoveCC(mark1,mark2):
    bestScore = -1000
    bestMove = 0
    start = time.time()
    for key in board.keys(): 
        if board[key] == ' ':
            x.append(1)
            board[key] = mark1
            score = minimax_2(board,5,mark1,mark2,False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score 
                bestMove = key
    end = time.time()
    print("Diem cua nuoc di: ",bestScore)
    print("Thoi gian chay: ",end-start)
    print("So nut duyet: ",len(x))
    x.clear()
    insertLetter(mark1, bestMove)
def minimax_2(board,d,mark1,mark2,isMaximizing):
    if d==0 or checkDraw() or checkWin():
        return valueE(mark1,mark2)    
    if isMaximizing:
        bestScore = -100
        for key in board.keys():
            if board[key] == ' ':
                x.append(1)
                board[key] = mark1 
                score = minimax_2(board,d-1,mark1,mark2, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore 
    else:
        bestScore = 10
        for key in board.keys():
            if board[key] == ' ':
                x.append(1)
                board[key] = mark2
                score = minimax_2(board,d-1,mark1,mark2, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore
def anphabeta(board,d,mark1,mark2,isMaximizing,a,b):
  
    if d==0 or checkDraw() or checkWin():
        return valueE(mark1,mark2)    
    if isMaximizing:
        for key in board.keys():
            if board[key] == ' ':
                x.append(1)
                board[key] = mark1 
                score = anphabeta(board,d-1,mark1,mark2, False,a,b)
                board[key] = ' '
                if score > a:
                    a = score
                if a >= b:
                    break
        return a 
    else:
        for key in board.keys():
            if board[key] == ' ':
                x.append(1)
                board[key] = mark2
                score = anphabeta(board,d-1,mark1,mark2, True,a,b)
                board[key] = ' '
                if score < b:
                    b = score
                if a >= b:
                    break
        return b
def Value2(mark):
    dem = 0
    for i in range (4):
        if board[i*4 + 4] != mark and board[i*4+1] != mark and board[i*4+2] != mark and board[i*4+3] != mark :
            dem += 1
        if board[0*4 + i+1] != mark and board[2*4+i+1] != mark and board[3*4+i+1] != mark and board[3*4+i+1] != mark :
            dem += 1
    if board [1] != mark and board [6] != mark and board[11] != mark and board[16] != mark:
        dem += 1
    if board [4] != mark and board [7] != mark and board[10] != mark and board[13] != mark:
        dem += 1
    return dem 
def valueE(mark1,mark2):
    dem1 = Value2(mark2)
    dem2 = Value2(mark1)
    return dem1 - dem2
if a == 1:
        computer = 'X'
        computer2 = 'O'
        while not checkWin():
            compMoveCC(computer,computer2)
            compMove(computer2,computer)
else:
        computer = 'X'
        computer2 = 'O'
        while not checkWin():
            compMove(computer,computer2)
            compMoveCC(computer2,computer)




