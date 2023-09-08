
from tkinter import *
import tkinter as tk
import random

# Game Reset
def reset():
    button1["state"] = "active"
    button2["state"] = "active"
    button3["state"] = "active"
    label1.config(text = "Player VS Computer")
    label2.config(text = "Match Result")
    
# Disable Buttons
def disableButton():
    button1["state"] = "disable"
    button2["state"] = "disable"
    button3["state"] = "disable"
    
# Game Logic
def isRock():
    computerValue = opponentValue[str(random.randint(0, 2))]
    if computerValue == "Rock":
        matchResult = "Draw"
    elif computerValue == "Scissor":
        matchResult = "Player Wins"
    else:
        matchResult = "Computer Wins"
    label2.config(text = matchResult)
    label1.config(text = "Rock VS " + computerValue)
    disableButton()
    
def isPaper():
    computerValue = opponentValue[str(random.randint(0, 2))]
    if computerValue == "Paper":
        matchResult = "Draw"
    elif computerValue == "Scissor":
        matchResult = "Computer Wins"
    else:
        matchResult = "Player Wins"
    label2.config(text = matchResult)
    label1.config(text = "Paper VS " + computerValue)
    disableButton()
    
def isScissor():
    computerValue = opponentValue[str(random.randint(0, 2))]
    if computerValue == "Scissor":
        matchResult = "Draw"
    elif computerValue == "Rock":
        matchResult = "Computer Wins"
    else:
        matchResult = "Player Wins"
    label2.config(text = matchResult)
    label1.config(text = "Scissor VS " + computerValue)
    disableButton()

# Create Tk Object and Set Window
root = Tk()
root.geometry("500x500")
root.title("Rock, Paper, Scissor Game")

# Set GUI
label0 = tk.Label(root)
label0["text"] = "Rock, Paper, Scissor"
label0["font"] = "normal 28"
label0["fg"] = "#EEEEEE"
label0["bg"] = "#3066A3"
label0["justify"] = "center"
label0.place(x=0,y=0,width=500,height=50)

label1 = tk.Label(root)
label1["text"] = "Player VS Computer"
label1["font"] = "normal 22"
label1["fg"] = "#EEEEEE"
label1["bg"] = "#5EA9EA"
label1["justify"] = "center"
label1.place(x=0,y=50,width=500,height=100)

label2 = tk.Label(root)
label2["text"] = "Match Result"
label2["font"] = "normal 34"
label2["fg"] = "#333333"
label2["bg"] = "#D0D0D0"
label2["justify"] = "center"
label2.place(x=0,y=150,width=500,height=75)

button1 = tk.Button(root)
button1["text"] = "Rock"
button1["font"] = "normal 12"
button1["fg"] = "#EEEEEE"
button1["bg"] = "#3066A3"
button1["justify"] = "center"
button1["command"] = isRock
button1.place(x=66,y=270,width=100,height=40)

button2 = tk.Button(root)
button2["text"] = "Paper"
button2["font"] = "normal 12"
button2["fg"] = "#EEEEEE"
button2["bg"] = "#3066A3"
button2["justify"] = "center"
button2["command"] = isPaper
button2.place(x=200,y=270,width=100,height=40)

button3 = tk.Button(root)
button3["text"] = "Scissor"
button3["font"] = "normal 12"
button3["fg"] = "#EEEEEE"
button3["bg"] = "#3066A3"
button3["justify"] = "center"
button3["command"] = isScissor
button3.place(x=333,y=270,width=100,height=40)

resetButton = tk.Button(root)
resetButton["text"] = "Reset"
resetButton["font"] = "normal 12"
resetButton["fg"] = "#EEEEEE"
resetButton["bg"] = "#5EA9EA"
resetButton["justify"] = "center"
resetButton["command"] = reset
resetButton.place(x=200,y=350,width=100,height=40)

# Set Opponent Values
opponentValue = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
    }

# Execute
root.mainloop()
