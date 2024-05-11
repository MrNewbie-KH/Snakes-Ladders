import tkinter as tk
from PIL import ImageTk, Image
import random


# Function to quit the game
def quit_game():
    root.destroy()

# the main window
root = tk.Tk()
root.geometry("1200x800")
root.title("Snakes and Ladders")

# the frame holding the main window
frame1 = tk.Frame(root, width=1200, height=800, relief='raised')
frame1.place(x=0, y=0)

# the board where snakes and ladders are located
board_image = ImageTk.PhotoImage(Image.open("./images/board.webp"))
Lab = tk.Label(frame1, image=board_image)
Lab.place(x=0, y=0)

# until here we placed an image

# Player 1
player1_btn = tk.Button (root,text="Player 1",height=3,width=16,bg="red",fg="blue",font=("Cursive",16,"bold"),activebackground="white")
player1_btn.place(x=1000,y=0)
# Player 2
player2_btn = tk.Button (root,text="Player 2",height=3,width=16,bg="red",fg="blue",font=("Cursive",16,"bold"),activebackground="white")
player2_btn.place(x=1000,y=500)
# quit 
quit_btn = tk.Button (root,text="Quit",command=quit_game,height=3,width=16,bg="red",fg="black",font=("Cursive",16,"bold"),activebackground="white")
quit_btn.place(x=1000,y=600)
# dice
roll_image = Image.open("./images/0.png").resize((65, 65))
roll_image = ImageTk.PhotoImage(roll_image)
button_roll = tk.Button(root, image=roll_image, command="")
button_roll.image = roll_image  
button_roll.place(x=1050, y=100)  


root.mainloop()
