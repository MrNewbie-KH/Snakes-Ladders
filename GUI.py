import tkinter as tk
from PIL import ImageTk, Image
import random
from socket import *
from threading import Thread

s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 8000))
# GLOBALS
Dice = []
Index={} 
Snakes={32:10,36:6,48:26,62:18,88:24,95:56,97:78}
Ladders={1:38,4:14,8:30,28:76,21:42,50:67,71:92,80:99}
position1=0
position2=0
turn =0
lol = s.recv(1024).decode()
if lol =="first":
    turn = 1
else:
    turn =4
def move_coin(r):
    global player1_coin,player2_coin, Index,turn
    if turn==1:
        player1_coin.place(x=Index[r][0],y=Index[r][1])
        player1_btn.configure(state="disabled")
        turn = 3
    elif turn==2:
        player2_coin.place(x=Index[r][0],y=Index[r][1])
        player1_btn.configure(state="disabled")
        turn = 4
    elif turn ==3:
        player2_coin.place(x=Index[r][0],y=Index[r][1])
        player1_btn.configure(state="normal")
        turn = 1 
    elif turn == 4 :
        player1_coin.place(x=Index[r][0],y=Index[r][1])
        player1_btn.configure(state="normal")
        turn = 2



def receive_message():
    global turn
    while True:
        p = s.recv(1024).decode()
        move_coin(int(p))
        print(f"position {p} of user {turn}")


def send_number(r):
    s.send(str(r).encode('utf-8'))

print(turn)

receive = Thread(target=receive_message)
receive.start()

#    ==============================================================
root = tk.Tk()
root.geometry("800x600")
root.title("Snakes and Ladders")
# the frame holding the main window
frame1 = tk.Frame(root, width=800, height=600, relief='raised')
frame1.place(x=0, y=0)



# the board where snakes and ladders are located
board_image = ImageTk.PhotoImage(Image.open("./images/board.webp"))
Lab = tk.Label(frame1, image=board_image)
Lab.place(x=0, y=0)


def check_ladder():
    global turn 
    global position1,position2,Ladders
    if   turn==1:
        if position1 in Ladders:
             position1=Ladders[position1]
             return position1
        else:
            return position1
    elif turn==2:
        if position2 in Ladders:
             position2=Ladders[position2]
             return position2
        else:
            return position2
def check_snake():
    global turn
    global position1,position2,Snakes
    if turn==1:
        if position1 in Snakes:
            position1=Snakes[position1]
            return position1
        else:
            return position1
    elif  turn==2:
        if position2 in Snakes:
            position2=Snakes[position2]
            return position2
        else:
            return position2
def roll_dice(): 
    global Dice, turn ,position1,position2,player1_btn
    r = random.randint(1, 6)
    # send_number(r)
    if turn==1: 
        if (position1+r)<=100:
            position1=position1+r
        position1=check_ladder()
        position1=check_snake()
        move_coin( int(position1))
        send_number(int(position1))
    
    elif  turn==2:
        if (position2+r)<=100:
            position2=position2+r
        position2=check_ladder()
        position2=check_snake()
        move_coin( int(position2))
        send_number(int(position2))
    is_winner()

    print(r,turn)

        
    b2 = tk.Button(root,image=Dice[r-1],height=80,width=80)
    # b2.place(x=1250,y=200)
    b2.image = Dice[r-1]
    b2.place(x=550, y=300)  
    # print(Dice[r-1])
player1_btn = tk.Button (root,text="Play",height=3,width=16,bg="red",fg="blue",font=("Cursive",16,"bold"),activebackground="white",command=roll_dice)
def is_winner():
    global position1,position2
    if position1==100:
        message="Player 1 is the winner"
        Lab=tk.Label(root,text=message,height=2,width=20,bg="red",font=("bold"))
        Lab.place(x=500,y=500)
        reset_coins()
    elif position2==100 :
        message="Player 2 is the winner"
        Lab=tk.Label(root,text=message,height=2,width=20,bg="red",font=("bold"))
        Lab.place(x=500,y=500)
        reset_coins()
        
def load_images():
    global Dice
    names=["1.png","2.png","3.jpeg","4.png","5.png","6.png"]
    for name in names:
         # dice
        im = Image.open("./images/"+name).resize((65, 65))
        im = ImageTk.PhotoImage(im)
        Dice.append(im)
        # 



def get_index():
    global player1_coin,player2_coin
    Nums=[100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # generating x and y for every one
    row=25
    i=0
    for x in range (1,11):
        col=30
        for y in range(1,11):
            Index[Nums[i]]=(col,row)
            col = col +45
            i = i +1
        row = row + 45
    # print(Index)


def quit_game():
    root.destroy()
def start_game():

    global im ,player1_btn,turn
    # Player 1
    # player1_btn = tk.Button (root,text="Play",height=3,width=16,bg="red",fg="blue",font=("Cursive",16,"bold"),activebackground="white",command=roll_dice)
    player1_btn.place(x=550,y=100)
    if turn==1 or turn ==2:
        player1_btn.configure(state="normal")
    else:
        player1_btn.configure(state="disabled")
    # quit 
    quit_btn = tk.Button (root,text="Quit",command=quit_game,height=3,width=16,bg="red",fg="black",font=("Cursive",16,"bold"),activebackground="white")
    quit_btn.place(x=550,y=200)
    # dice
    im = Image.open("./images/0.png").resize((65, 65))
    im = ImageTk.PhotoImage(im)
    b2 = tk.Button(root, image=im)
    b2.image = im  
    b2.place(x=550, y=300)  

def reset_coins():
    global player1_coin,player2_coin ,position1,position2
    player2_coin.place(x=30, y=500)
    player1_coin.place(x=0, y=500)
    position2=0
    position1=0


# Player 1 coin (green)
player1_coin = tk.Canvas(root, width=30, height=30)
player1_coin.create_oval(5, 5, 30, 30, fill='blue')

# Player 2 coin (blue)
player2_coin = tk.Canvas(root, width=30, height=30)
player2_coin.create_oval(5, 5, 30, 30, fill='green')
# ================================================

reset_coins()
load_images()
get_index()
start_game()

root.mainloop()
