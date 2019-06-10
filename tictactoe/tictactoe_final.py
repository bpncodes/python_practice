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
def checkforgame():
    global board
    global win
    if(( board[2][2] =='0' and board[2][6] == '0' and board[2][10] == '0')or( board[10][2] =='0' and board[10][6] == '0' and board[10][10] == '0')or( board[6][2] =='0' and board[6][6] == '0' and board[6][10] == '0')or( board[2][2] =='0' and board[6][2] == '0' and board[10][2] == '0')or( board[2][6] =='0' and board[6][6] == '0' and board[10][6] == '0')or( board[2][10] =='0' and board[2][10] == '0' and board[10][10] == '0')or( board[2][2] =='0' and board[6][6] == '0' and board[10][10] == '0')or( board[10][2] =='0' and board[6][6] == '0' and board[2][10] == '0')):
        printit()
        print("Player one won !!!")
        win=False
        return win
    elif(( board[2][2] =='1' and board[2][6] == '1' and board[2][10] == '1')or( board[10][2] =='1' and board[10][6] == '1' and board[10][10] == '1')or( board[6][2] =='1' and board[6][6] == '1' and board[6][10] == '1')or( board[2][2] =='1' and board[6][2] == '1' and board[10][2] == '1')or( board[2][6] =='1' and board[6][6] == '1' and board[10][6] == '1')or( board[2][10] =='1' and board[2][10] == '1' and board[10][10] == '1')or( board[2][2] =='1' and board[6][6] == '1' and board[10][10] == '1')or( board[10][2] =='1' and board[6][6] == '1' and board[2][10] == '1')):
        printit()
        print("Player two won !!!")
        win = False
        return win
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
    global win
    win=True
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
    print('Player one goes first')
    while(gameplayed<9 and win):
        if turn==1:
            print('** 1 is the marker for player for Player two **')
            print('Player one turn : ')
            print('The available positions are : ')
            printit()
            pos=input('Enter the alphabet in which you want to insert : ')
            if pos=='A' and ainuse:
                board[2][2]='0'
                turn=2
                ainuse=False
                gameplayed += 1
                checkforgame()
            elif pos=='B' and binuse:
                board[2][6]='0'
                turn=2
                gameplayed += 1
                binuse=False
                checkforgame()
            elif pos=='C' and cinuse:
                board[2][10]='0'
                turn=2
                gameplayed += 1
                cinuse=False
                checkforgame()
            elif pos=='D' and dinuse:
                board[6][2]='0'
                turn=2
                dinuse==False
                gameplayed += 1
                checkforgame()
            elif pos=='E' and eincuse:
                board[6][6]='0'
                turn=2
                eincuse=False
                checkforgame()
                gameplayed += 1
            elif pos=='F' and finuse:
                board[6][10]='0'
                turn=2
                checkforgame()
                finuse==False
                gameplayed += 1
            elif pos=='G' and ginuse:
                board[10][2]='0'
                turn=2
                checkforgame()
                ginuse=False
                gameplayed += 1
            elif pos=='H' and hinuse:
                board[10][6]='0'
                turn=2
                checkforgame()
                hinuse=False
                gameplayed += 1
            elif pos=='I' and iinuse:
                board[10][10]='0'
                gameplayed += 1
                turn=2
                checkforgame()
                iinuse=False
            elif win==False:
                print('Game over')
                return

            else:
                print('Incorrect input . Try again ')
        elif turn==2:
            print('** 0 is the markger for Player one **')
            print('Player two turn : ')
            print('The available positions are : ')
            printit()
            pos=input('Enter the alphabet in which you want to insert : ')
            if pos=='A' and ainuse:
                board[2][2]='1'
                turn=1
                checkforgame()
                ainuse=False
                gameplayed += 1
            elif pos=='B' and binuse:
                board[2][6]='1'
                turn=1
                checkforgame()
                binuse=False
                gameplayed += 1
            elif pos=='C' and cinuse:
                board[2][10]='1'
                turn=1
                checkforgame()
                cinuse=False
                gameplayed += 1
            elif pos=='D' and dinuse:
                board[6][2]='1'
                turn=1
                checkforgame()
                dinuse=False
                gameplayed += 1
            elif pos=='E' and eincuse:
                board[6][6]='1'
                turn=1
                checkforgame()
                eincuse=False
                gameplayed += 1
            elif pos=='F' and finuse:
                board[6][10]='1'
                turn=1
                checkforgame()
                finuse=False
                gameplayed += 1
            elif pos=='G' and ginuse:
                board[10][2]='1'
                turn=1
                checkforgame()
                ginuse=False
                gameplayed += 1
            elif pos=='H' and hinuse:
                board[10][6]='1'
                turn=1
                checkforgame()
                hinuse=False
                gameplayed += 1
            elif pos=='I' and iinuse:
                board[10][10]='1'
                turn=1
                checkforgame()
                iinuse=False
                gameplayed += 1
            else:
                print('No position available')
    if win:
        printit()
        print('Game Over')

def start():
    print('--------------------Welcome to the game : --------------------')
    print('Then current board of tictactoe is : \n')
    firstinitialise()
    nineturns()
win=True
w, h = 12, 12;
board= [[0 for x in range(w)] for y in range(h)]
start()