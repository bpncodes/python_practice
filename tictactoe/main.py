def printit():
    global board
    for i in range(1,12):
        for j in range(1,12):
            if i==2 and j==2:
                print(board[2][2],end='')
            elif i==2 and j==6:
                print(board[2][6],end='')
            elif i==2 and j==10:
                print(board[2][10],end='')
            elif i==6 and j==2:
                print(board[6][2],end='')
            elif i==6 and j==6:
                print(board[6][6],end='')
            elif i==6 and j==10:
                print(board[6][10],end='')
            elif i==10 and j==2:
                print(board[10][2],end='')
            elif i==10 and j==6:
                print(board[10][6],end='')
            elif i==10 and j==10:
                print(board[10][10],end='')
            elif (i%4==0) and (j%4==0):
                print(' ',end='')
            elif i%4==0 and j%4!=0:
                print('-',end='')
            elif i%4!=0 and j%4==0:
                print('|',end='')
            elif i%4!=0 and j%4!=0:
                print(' ',end='')
        print('\n')

def firstinitialise():
    global board
    board[2][2] = 'A'
    board[2][6] = 'B'
    board[2][10] = 'C'
    board[6][2] = 'D'
    board[6][6] = 'E'
    board[6][10] = 'F'
    board[10][2] = 'G'
    board[10][6] = 'H'
    board[10][10] = 'I'

def nineturns():
    ainuse=True
    binuse=True
    cinuse=True
    dinuse=True
    eincuse=True
    finuse=True
    ginuse=True
    hinuse=True
    iinuse=True
    global board
    turn=1
    gameplayed=0
    while(gameplayed<9):
        if turn==1:
            print('Player one turn : ')
            print('The available positions are : ')
            printit()
            pos=input('Enter the alphabet in which you want to insert : ')
            if pos=='A' and ainuse:
                board[2][2]='0'
                turn=2
                ainuse=False
                gameplayed += 1
            elif pos=='B' and binuse:
                board[2][6]='0'
                turn=2
                gameplayed += 1
                binuse=False
            elif pos=='C' and cinuse:
                board[2][10]='0'
                turn=2
                gameplayed += 1
                cinuse=False
            elif pos=='D' and dinuse:
                board[6][2]='0'
                turn=2
                dinuse==False
                gameplayed += 1
            elif pos=='E' and eincuse:
                board[6][6]='0'
                turn=2
                eincuse=False
                gameplayed += 1
            elif pos=='F' and finuse:
                board[6][10]='0'
                turn=2
                finuse==False
                gameplayed += 1
            elif pos=='G' and ginuse:
                board[10][2]='0'
                turn=2
                ginuse=False
                gameplayed += 1
            elif pos=='H' and hinuse:
                board[10][6]='0'
                turn=2
                hinuse=False
                gameplayed += 1
            elif pos=='I' and iinuse:
                board[10][10]='0'
                gameplayed += 1
                turn=2
                iinuse=False
            else:
                print('Incorrect input . Try again ')
        elif turn==2:
            print('Player two turn : ')
            print('The available positions are : ')
            printit()
            pos=input('Enter the alphabet in which you want to insert : ')
            if pos=='A' and ainuse:
                board[2][2]='1'
                turn=1
                ainuse=False
                gameplayed += 1
            elif pos=='B' and binuse:
                board[2][6]='1'
                turn=1
                binuse=False
                gameplayed += 1
            elif pos=='C' and cinuse:
                board[2][10]='1'
                turn=1
                cinuse=False
                gameplayed += 1
            elif pos=='D' and dinuse:
                board[6][2]='1'
                turn=1
                dinuse=False
                gameplayed += 1
            elif pos=='E' and eincuse:
                board[6][6]='1'
                turn=1
                eincuse=False
                gameplayed += 1
            elif pos=='F' and finuse:
                board[6][10]='1'
                turn=1
                finuse=False
                gameplayed += 1
            elif pos=='G' and ginuse:
                board[10][2]='1'
                turn=1
                ginuse=False
                gameplayed += 1
            elif pos=='H' and hinuse:
                board[10][6]='1'
                turn=1
                hinuse=False
                gameplayed += 1
            elif pos=='I' and iinuse:
                board[10][10]='1'
                turn=1
                iinuse=False
                gameplayed += 1
            else:
                print('No position available')
def start():
    print('--------------------Welcome to the game : --------------------')
    print('Then current board of tictactoe is : \n')
    firstinitialise()
    nineturns()

w, h = 12, 12;
board= [[0 for x in range(w)] for y in range(h)]
start()