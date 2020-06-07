# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 11:45:23 2019

@author: Kushagra Indurkhya
"""
from tkinter import *
import tkinter.messagebox

tk = Tk()
tk.configure(bg="firebrick3")
tk.title("Tic Tac Toe")
p = StringVar()
# board=[[" "*3]*3]
player_name = Entry(tk, textvariable=p, bd=7,width=35,bg="white")
player_name.grid(row=1, column=1, columnspan=8)
p=player_name.get()

#checking for empty tiles
def moves_left(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return True
    return False

WIN_SCORE = 10
LOOSE_SCORE = -10

#checking if maximizer(computer) or minimizer(player) == winning or draw
def evaluate(board):
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] == 'O': return LOOSE_SCORE
    if board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] == 'O': return LOOSE_SCORE
    if board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] == 'O': return LOOSE_SCORE
    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] == 'O': return LOOSE_SCORE
    if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] == 'O': return LOOSE_SCORE
    if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] == 'O': return LOOSE_SCORE
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == 'O': return LOOSE_SCORE
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] == 'O': return LOOSE_SCORE
    if board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][0] == 'X': return WIN_SCORE
    if board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][0] == 'X': return WIN_SCORE
    if board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][0] == 'X': return WIN_SCORE
    if board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[0][0] == 'X': return WIN_SCORE
    if board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[0][1] == 'X': return WIN_SCORE
    if board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[0][2] == 'X': return WIN_SCORE
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == 'X': return WIN_SCORE
    if board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] == 'X': return WIN_SCORE
    return 0

#minimax algorithm imp is bool variable to know if its maximiser's turn or not
def minimax(board , imp,alpha,beta):
    score=evaluate(board)
    if score ==  10:
        return score
    if score ==  -10:
        return score
    if moves_left(board) ==  False:
        return 0
    if imp  ==   True:
        best=-1000
        for i in range(3):
            for j in range(3):
                if board[i][j]==" ":
                    board[i][j]="X"
                    val=minimax(board,not imp,alpha,beta)
                    best=max(best,val)
                    alpha=max(best,alpha)
                    board[i][j]=" "
                    if alpha>=beta:
                    	return best                
    else:
        best= 1000
        for i in range(3):
            for j in range(3):
                if board[i][j]==" ":
                    board[i][j]="O"
                    val=minimax(board,not imp,alpha,beta)
                    best=min(best,val)
                    beta=min(best,beta)
                    board[i][j]=" "
                    if alpha>=beta:
                    	return best               
    
    return best
#finding best move for a given board position
def best_move(board):
    bestval = 1000
    moveval = None
    row=-1
    col=-1
    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':
                board[i][j]='O'
                moveval=minimax(board,True,-1000,1000)
                board[i][j]=' '
                if moveval < bestval:
                    row=i
                    col=j
                    bestval=moveval
   #converting coordinates to button no
    return((3*row)+(col+1))
#function to disable buttons after the game is over
def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


# function defining action when the user clicks a button this function also calls best_move() and moves computer's turn
def btnClick(buttons):
    global bclick,player_name, player,p,board,undo_p,undo_c

    if buttons["text"] == " ":
        buttons["text"] = "X"
        undo_p=buttons
        checkForWin()


        board=[[button1['text'],button2['text'],button3['text']],[button4['text'],button5['text'],button6['text']],[button7['text'],button8['text'],button9['text']]]
        mov= best_move(board)
        if mov == 1:
            button1["text"]="O"
            undo_c=button1
        if mov == 2:
            button2["text"]="O"
            undo_c=button2
        if mov == 3:
            button3["text"]="O"
            undo_c=button3
        if mov == 4:
            button4["text"]="O"
            undo_c=button4
        if mov == 5:
            button5["text"]="O"
            undo_c=button5
        if mov == 6:
            button6["text"]="O"
            undo_c=button6
        if mov == 7:
            button7["text"]="O"
            undo_c=button7
        if mov == 8:
            button8["text"]="O"
            undo_c=button8
        if mov == 9:
            button9["text"]="O"
            undo_c=button9
        checkForWin()

    else:
           tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")




# checks if in the given board position someone(either computer of human is winning or losing) or draw (no winner but and moves left)
def checkForWin():

    if (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo(player_name.get()+" VS Computer", "Computer Wins")
    elif(button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
          button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
          button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
          button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
          button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
          button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
          button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
          button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo(player_name.get()+" VS Computer",player_name.get()+" Wins")
    elif(moves_left([[button1['text'],button2['text'],button3['text']],[button4['text'],button5['text'],button6['text']],[button7['text'],button8['text'],button9['text']]])==False):
    	disableButton()
    	tkinter.messagebox.showinfo(player_name.get()+" VS Computer", "It's a draw")
# undo button's coomand
def reset(buttons,buttonc):
    buttons['text'] = ' '
    buttonc['text'] = ' '

# restting the board
def reset_All():
    button1['text'] = ' '
    button2['text'] = ' '
    button3['text'] = ' '
    button4['text'] = ' '
    button5['text'] = ' '
    button6['text'] = ' '
    button7['text'] = ' '
    button8['text'] = ' '
    button9['text'] = ' '
    button1.configure(state=NORMAL)
    button2.configure(state=NORMAL)
    button3.configure(state=NORMAL)
    button4.configure(state=NORMAL)
    button5.configure(state=NORMAL)
    button6.configure(state=NORMAL)
    button7.configure(state=NORMAL)
    button8.configure(state=NORMAL)
    button9.configure(state=NORMAL)




    
    

#defining all the buttons in tk
buttons = StringVar()
buttonc = StringVar()
label = Label( tk, text="Name:", font='Times 20 bold', bg='firebrick3', fg='black', height=1, width=8)
label.grid(row=1, column=0)

button1 = Button(tk, text=" ", font='Times 20 bold', bg='NavajoWhite3', fg='black', height=4, width=8, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg='NavajoWhite3', fg='black', height=4, width=8, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ',font='Times 20 bold', bg='NavajoWhite3', fg='black', height=4, width=8, command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg='NavajoWhite3', fg='black', height=4, width=8, command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg='NavajoWhite3', fg='black', height=4, width=8, command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg='NavajoWhite3', fg='black', height=4, width=8, command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg='NavajoWhite3', fg='black', height=4, width=8, command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg='NavajoWhite3', fg='black', height=4, width=8, command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg='NavajoWhite3', fg='black', height=4, width=8, command=lambda: btnClick(button9))
button9.grid(row=5, column=2)

button10=Button(tk, text="QUIT", bg="grey60",fg="black",command=tk.destroy,height=2,width=12)
button10.grid(row=6,column=0)

button12=Button(tk, text="UNDO", bg="grey60",fg="black",command=lambda:reset(undo_p,undo_c),height=2,width=12)
button12.grid(row=6,column=1)

button11=Button(tk, text="RESET", bg="grey60",fg="black",command=lambda:reset_All(),height=2,width=12)
button11.grid(row=6,column=2)

tk.mainloop()
