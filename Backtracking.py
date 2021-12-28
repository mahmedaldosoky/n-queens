import turtle
import time
import tkinter as tk
from tkinter import simpledialog

t = turtle.Turtle()
global N
board = []
boardList=[]


def getNQueens(N):
    def isSafe(board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        for i, j in zip(range(row, N, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True
    def solveNQueens(board, col):
        if col >= N:
            return True

        for i in range(N):
            if isSafe(board, i, col):
                board[i][col] = 1
                if solveNQueens(board, col + 1) == True:
                    return True
                
                board[i][col] = 0

        return False




    if N < 1:
      print("The Number N Should be 1 or larger ^_^")
    else: 
        
        for i in range(N):
            row = []
            for j in range(N):
                row.append(0)
            board.append(row)


        if solveNQueens(board, 0) == False:
            print("Solution does not exist :(")
        else:
            print("Solution:")
            for i in range(N):
                for j in range(N):
                    print(board[i][j], end=" ")
                print()
def box(ln):
    
    #print(boxNum)
    for i in range(4):
        t.forward(ln)
        #print(boxNum)
        if i==0:
            t.back(10)
            t.color('Black' if count % 2 != 0 else 'White')
            if boardList[boxNum+1]==1:
                t.write('Q')
            t.color('black')

            if count % 2 == 0:
               t.fillcolor("Black")
            else:
                t.fillcolor("White")
            t.forward(10)

        t.left(90)



ROOT = tk.Tk()
ROOT.withdraw()
# the input dialog
N = simpledialog.askinteger(title="plz only Even",prompt="Enter The N:")
getNQueens(N)

for i in range(N):
    for j in range(N):
        #print(board[3][1])
        print(board[i][N-1-j], end=" ")
        boardList.append(board[N-1-i][j])


t.speed(0)
x=0
y=0
count = 2
boxNum=-1
while True:
    t.goto(x,y)
    t.pendown()
    x += 20
    t.begin_fill()
    if count % 2 == 0:
        t.fillcolor("Black")
    else:
        t.fillcolor("White")

    
    count += 1
    box(20)
    boxNum+=1
    
    t.end_fill()
    if x >= 20*N:
        x=0
        y += 20
        t.penup()
        count += 1
    if y >= 20 * N:
        break
t.hideturtle()

turtle.done()