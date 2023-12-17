import pygame
import time
pygame.init
a = int(input("Nhap lua chon: 1.Minimax vs Alphabets 2.AlphaBeta vs Minimax: "))
pygame.display.set_caption('Cờ Caro (3x3)')
screen = pygame.display.set_mode((610,580))
running = True
background = pygame.image.load(r'B.png')
background = pygame.transform.scale2x(background)
iconx = pygame.image.load(r'X.png')
icono = pygame.image.load(r'O.png')
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
computer = computer2 = ' '
x = []
def printBoard(board):
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-+-+-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-+-+-")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("\n")

def spaceIsFree(position):
    if board[position] == ' ':
        return True 
    return False 

def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter 
        x=0
        y=0
        if position == 1 or position == 2 or position == 3:
            y= 50
        elif position == 6 or position == 5 or position == 4:
            y = 240
        else:
            y = 400
        if position == 1 or position == 4 or position == 7:
            x = 75
        elif position == 2 or position == 5 or position == 8:
            x = 260
        else:
            x = 430
        printBoard(board)
        if letter == 'X':
            screen.blit(iconx,(x,y))
            pygame.display.update()
        else:
            screen.blit(icono,(x,y))
            pygame.display.update()
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
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
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
            score = anphabeta(board,9,mark1,mark2,False,a,b)
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
            score = minimax_2(board,9,mark1,mark2,False)
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
        bestScore = -1
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
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark) or ((board[1] == board[2] or board[2] == ' ') and (board[1] == board[3] or board[3] == ' ') and board[1] == mark) or ((board[1] == board[2] or board[1] == ' ') and (board[2] == board[3] or board[3] == ' ') and board[2] == mark) or  ((board[1] == board[3] or board[1] == ' ') and (board[2] == board[3] or board[2] == ' ') and board[3] == mark) or (board[1] == board[2] and board[1] == board[3] and board[1] == ' '):
        dem += 1
    if (board[1] == board[4] and board[1] == board[7] and board[1] == mark) or ((board[1] == board[4] or board[4] == ' ') and (board[1] == board[7] or board[7] == ' ') and board[1] == mark) or ((board[1] == board[4] or board[1] == ' ') and (board[4] == board[7] or board[7] == ' ') and board[4] == mark ) or ((board[1] == board[7] or board[1] == ' ') and (board[4] == board[7] or board[4] == ' ') and board[7] == mark) or (board[1] == board[4] and board[1] == board[7] and board[1] == ' '):
        dem += 1
    if (board[1] == board[9] and board[1] == board[5] and board[1] == mark) or ((board[1] == board[5] or board[5] == ' ') and (board[1] == board[9] or board[9] == ' ') and board[1] == mark) or ((board[1] == board[5] or board[1] == ' ') and (board[5] == board[9] or board[9] == ' ') and board[5] == mark) or ((board[1] == board[9] or board[1] == ' ') and (board[5] == board[9] or board[5] == ' ') and board[9] == mark) or (board[1] == board[5] and board[1] == board[9] and board[1] == ' '):
        dem += 1
    if (board[5] == board[2] and board[2] == board[8] and board[2] == mark) or ((board[2] == board[5] or board[5] == ' ') and (board[2] == board[8] or board[8] == ' ') and board[2] == mark) or ((board[2] == board[5] or board[2] == ' ') and (board[8] == board[5] or board[8] == ' ') and board[5] == mark) or ((board[2] == board[8] or board[2] == ' ') and (board[5] == board[8] or board[5] == ' ') and board[8] == mark) or (board[2] == board[5] and board[2] == board[8] and board[2] == ' '):
        dem += 1
    if (board[3] == board[6] and board[3] == board[9] and board[3] == mark) or ((board[3] == board[6] or board[6] == ' ') and (board[9] == board[3] or board[9] == ' ') and board[3] == mark) or ((board[3] == board[6] or board[3] == ' ') and (board[6] == board[9] or board[9] == ' ') and board[6] == mark) or ((board[3] == board[9] or board[3] == ' ') and (board[6] == board[9] or board[6] == ' ') and board[9] == mark) or (board[3] == board[6] and board[3] == board[9] and board[3] == ' '):
        dem += 1
    if (board[7] == board[3] and board[5] == board[3] and board[3] == mark) or ((board[3] == board[5] or board[5] == ' ') and (board[3] == board[7] or board[7] == ' ') and board[3] == mark) or ((board[7] == board[5] or board[7] == ' ') and (board[3] == board[5] or board[3] == ' ') and board[5] == mark) or ((board[7] == board[5] or board[5] == ' ') and (board[7] == board[3] or board[3] == ' ') and board[7] == mark) or (board[7] == board[5] and board[7] == board[3] and board[7] == ' '):
        dem += 1
    if (board[4] == board[5] and board[4] == board[6] and board[4] == mark) or ((board[4] == board[5] or board[5] == ' ') and (board[4] == board[6] or board[6] == ' ') and board[4] == mark) or ((board[4] == board[5] or board[4] == ' ') and (board[5] == board[6] or board[6] == ' ') and board[5] == mark) or ((board[4] == board[6] or board[4] == ' ') and (board[5] == board[6] or board[5] == ' ') and board[6] == mark) or (board[4] == board[5] and board[4] == board[6] and board[4] == ' '):
        dem += 1
    if (board[9] == board[7] and board[8] == board[7] and board[7] == mark) or ((board[7] == board[8] or board[8] == ' ') and (board[7] == board[9] or board[9] == ' ') and board[7] == mark) or ((board[7] == board[8] or board[7] == ' ') and (board[8] == board[9] or board[9] == ' ') and board[8] == mark) or ((board[7] == board[9] or board[7] == ' ') and (board[8] == board[9] or board[8] == ' ') and board[9] == mark) or (board[7] == board[8] and board[7] == board[9] and board[7] == ' '):
        dem += 1
    return dem 
def valueE(mark1,mark2):
    dem1 = Value2(mark1)
    dem2 = Value2(mark2)
    return dem1 - dem2
pygame.init
pygame.display.set_caption('Cờ Caro (3x3)')
running = True
background = pygame.image.load(r'B.png')
background = pygame.transform.scale2x(background)
iconx = pygame.image.load(r'X.png')
screen = pygame.display.set_mode((610,580))
if a == 1:
    while running == True:
        screen.blit(background,(0,0))
        computer = 'X'
        computer2 = 'O'
        while not checkWin():
            compMoveCC(computer,computer2)
            pygame.time.delay(1000)
            compMove(computer2,computer)
            pygame.time.delay(1000)
else:
    while running == True:
        screen.blit(background,(0,0))
        computer = 'X'
        computer2 = 'O'
        while not checkWin():
            compMove(computer,computer2)
            pygame.time.delay(1000)
            compMoveCC(computer2,computer)
            pygame.time.delay(1000)




