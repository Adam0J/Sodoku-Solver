# -*- coding: utf-8 -*-
"""
Sudoku Solver
"""
from copy import deepcopy

def NewGame():
    """
    Makes a simple dictdictoinary containing the inital Sodoku board.
    """
    game = {
            'board': [[0,0,0,0,0,0,0,9,0],
                     [8,0,0,9,5,7,0,0,4],
                     [6,0,7,0,0,4,5,0,0],
                     [0,0,4,0,0,0,0,6,2],
                     [0,0,6,0,0,0,7,0,0],
                     [9,2,0,0,0,0,4,0,0],
                     [0,0,8,3,0,0,9,0,5],
                     [4,0,0,2,9,1,0,0,8],
                     [0,3,0,0,0,0,0,0,0]]
            }
    return game

def PrintBoard(board):
    """
    Prints the sodoku board in a more appealing way than a list of list's.
    """
    horizontalborder = " -----------"
    for i in range(9):#counts rows while printing the row in question
        row = ' '
        for j in range(9):#loops through the lists values and turns the to strings adds them before printing them
            if j == 2 or j == 5:    
                row += str(board[i][j]) + '|'
            else:
                row += str(board[i][j])
        if i == 2 or i==5 :
            print(row)
            print(horizontalborder)
        else:
            print(row)
    return



def ZeroFinder(board):
    """
    Finds all entries on the board that are yet to be filled (all zero 
    elements). It then outputs the postion of all said elements as a list of 
    tuple's.
    """
    EmptyEntries = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                EmptyEntries.append((i,j))
    return EmptyEntries




def CheckSqs(i,j,board):
    
    """
    Finds possible entries that could be entered into a zero element based 
    soley on the 3x3 square it's within. Requires tuple input that refers to the 
    zero elements postion on the board.
    """
    Numbers=[1,2,3,4,5,6,7,8,9]

    
    if i < 3 and j <3:
        (n,m)=(3,3)
    if i < 3 and 3<=j<6:
        (n,m)=(3,6)
    if i < 3 and 6<=j<9:
        (n,m)=(3,9)
        
    if 3<=i<6 and j <3:
        (n,m)=(6,3)
    if 3<=i<6 and 3<=j<6:
        (n,m)=(6,6)
    if 3<=i<6 and 6<=j<9:
        (n,m)=(6,9)
        
    if 6<=i<9 and j <3:
        (n,m)=(9,3)
    if 6<=i<9 and 3<=j<6:
        (n,m)=(9,6)
    if 6<=i<9 and 6<=j<9:
        (n,m)=(9,9)
        
    L = []
    for s in range(n-3,n):
        for t in range(m-3,m):
            if board[s][t] != 0:
                L.append(board[s][t])
    Moves = list(set(Numbers)-set(L))
    
    return Moves


def CheckRCs(i,j,board):
    """
    Finds possible entries that could be entered into a zero element based 
    soley on the rows and columns it's on. Requires tuple input that refers 
    to the zero elements postion on the board.
    """
    Numbers=[1,2,3,4,5,6,7,8,9]
   
  
    LC=[]
    LR=[]
    for n in range(9):
        if n == j:
            continue
        elif board[i][n] == 0:
            continue
        else:
            LC.append(board[i][n])
    
    for m in range(9):
        if m == i:
            continue
        elif board[m][j] == 0:
            continue
        else:
            LR.append(board[m][j])
    
    Moves = list(set(Numbers)-set(LC)-set(LR))
    
    return Moves

                
def PossibleMoves(Sqs,RCs):
    """
    Function that finds the union of the two lists inputted.
    """
    Moves = list(set(Sqs)&set(RCs))
        
    return Moves

def UpdateBoard(i,j,Move,board):
    board[i][j] = Move
    
    return board
        
    

def Solver():
    board = NewGame()['board']
    PrintBoard(board)
    print('\n')
    print('\n')
    print("Press any button to start.")
    (str(input()))
    EmptyElements = ZeroFinder(board) #Make this faster later by running this once then removing from list when element entered.


    while EmptyElements != []: 
        
        L = []
        P = []
        for n in range(3,12,3):
            for m in range(3,12,3):
                for i in range(n-3,n):
                    for j in range(m-3,m):
                        if (i,j) in EmptyElements:
                            Sqs = CheckSqs(i,j,board)
                            RCs = CheckRCs(i,j,board)
                            Moves = PossibleMoves(Sqs,RCs)
                            L.append(Moves)
                            P.append((i,j))
        
        for t in range(len(L)):
            if len(L[t]) == 1:
                move = L[t][0]
                (i,j) = P[t]
                board = UpdateBoard(i,j,move,board)
                PrintBoard(board)
                print('\n')
                
        EmptyElements = ZeroFinder(board) # can make this faster
    return
Solver()
            

            
