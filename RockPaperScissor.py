
from tkinter import *
import random

# Game Reset
def reset():
    button1["state"] = "active"
    button2["state"] = "active"
    button3["state"] = "active"
    label1.config(text = "Player")
    label2.config(text = "Computer")
    label3.config(text = "")
    
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
    label4.config(text = matchResult)
    label1.config(text = "Rock     ")
    label3.config(text = computerValue)
    disableButton()
    
def isPaper():
    computerValue = opponentValue[str(random.randint(0, 2))]
    if computerValue == "Paper":
        matchResult = "Draw"
    elif computerValue == "Scissor":
        matchResult = "Computer Wins"
    else:
        matchResult = "Player Wins"
    label4.config(text = matchResult)
    label1.config(text = "Paper     ")
    label3.config(text = computerValue)
    disableButton()
    
def isScissor():
    computerValue = opponentValue[str(random.randint(0, 2))]
    if computerValue == "Scissor":
        matchResult = "Draw"
    elif computerValue == "Rock":
        matchResult = "Computer Wins"
    else:
        matchResult = "Player Wins"
    label4.config(text = matchResult)
    label1.config(text = "Rock     ")
    label3.config(text = computerValue)
    disableButton()

# Create Tk Object and Set Window
root = Tk()
root.geometry("500x500")
root.title("Rock, Paper, Scissor Game")

# Set GUI
Label(root, text = "Rock, Paper, Scissor", 
      font = "normal 24", fg = "Gray").pack(pady = 25)

frame = Frame(root)
frame.pack()

label1 = Label(frame, text = "Player        ", font = 12)
label2 = Label(frame, text = "VS        ", font = 14)
label3 = Label(frame, text = "Computer", font = 12)

label1.pack(side = LEFT)
label2.pack(side = LEFT)
label3.pack()

label4 = Label(root, text = "", font = "normal 24", bg = "white",
               width = 15, borderwidth = 2, relief = "solid")
label4.pack(pady = 20)

frame1 = Frame(root)
frame1.pack()

button1 = Button(frame1, text = "Rock", font = 12, width = 7,
                 command = isRock)
button2 = Button(frame1, text = "Paper", font = 12, width = 7,
                 command = isPaper)
button3 = Button(frame1, text = "Scissor", font = 12, width = 7,
                 command = isScissor)

button1.pack(side = LEFT, padx = 10)
button2.pack(side = LEFT, padx = 10)
button3.pack(padx = 10)

Button(root, text = "Reset", font = 12, fg = "red", bg = "black",
       command = reset).pack(pady = 25)

# Set Opponent Values
opponentValue = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
    }

# Execute
root.mainloop()
