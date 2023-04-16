print("enter the no of queens:")
N=int(input())

board=[[0]*N for _ in range(N)]
#function for checking if the queen is being attacked or not
def is_attack(row,col):
    #checking for row and column
    for k in range(0,N):

        if board[row][k]==1 or board[k][col]==1:
            return True
    #checking for diagonals
    for k in range(0,N):
        for l in range(0,N):
            if(k+l==row+col) or (k-l==row-col):
                if board[k][l]==1:
                    return True
    return False

#function for placing the queen
def N_queen(n):
    #all queens are placed on the board
    if n==0:
        return True
        '''checking if we can place a queen here or not
            queen will not be placed if the place is being attacked
            or already occupied'''
    for i in range(0,N):
        for j in range(0,N):
            if(not(is_attack(i,j))) and (board[i][j]!=1):
                board[i][j]=1
    #recursion
    #wether we can put the next queen with this arrangment or not
                if N_queen(n-1)==True:
                    return True

                board[i][j]=0
    return False                

N_queen(N)
for i in board:
    print (i)
