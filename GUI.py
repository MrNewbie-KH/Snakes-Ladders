import tkinter as tk
from PIL import ImageTk, Image
import random
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
# GLOBALS
Dice = []
Index={} # store x and y of each number
Snakes={32:10,36:6,48:26,62:18,88:24,95:56,97:78}
Ladders={1:38,4:14,8:30,28:76,21:42,50:67,71:92,80:99}
position1=None
position2=None

def check_ladder(turn):
    global position1,position2,Ladders
    flag=0
    if turn==1:
        if position1 in Ladders:
            position1=Ladders[position1]
            flag=1
    else:
        if position2 in Ladders:
            position2=Ladders[position2]
            flag=1
    return flag
def check_snake(turn):
    global position1,position2,Snakes
    flag=0
    if turn==1:
        if position1 in Snakes:
            position1=Snakes[position1]
            flag=1
    else:
        if position2 in Snakes:
            position2=Snakes[position2]
            flag=1
    return flag
def roll_dice():
    global Dice, turn ,position1,position2
    r = random.randint(1, 6)
    if turn == 1 :
        if (position1+r)<=100:
            position1=position1+r
        ladder=check_ladder(turn)
        check_snake(turn)
        move_coin(turn, position1)
        if r!=6 and ladder!=1:
            turn=2
    else:
        if (position2+r)<=100:
            position2=position2+r
        ladder=check_ladder(turn)
        check_snake(turn)
        move_coin(turn, position2)
        if r!=6 and ladder!=1:
            turn=1
    is_winner()


        
    b2 = tk.Button(root,image=Dice[r-1],height=80,width=80)
    # b2.place(x=1250,y=200)
    b2.image = Dice[r-1]
    b2.place(x=1050, y=100)  
    # print(Dice[r-1])
    print(r,turn)
player1_btn = tk.Button (root,text="Player 1",height=3,width=16,bg="red",fg="blue",font=("Cursive",16,"bold"),activebackground="white",command=roll_dice)
# player2_btn = tk.Button (root,text="Player 2",height=3,width=16,bg="red",fg="blue",font=("Cursive",16,"bold"),activebackground="white",command=roll_dice)
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

# Function to simulate dice roll

def move_coin(turn,r):
    global player1_coin,player2_coin, Index
    if turn==1:
        player1_coin.place(x=Index[r][0],y=Index[r][1])
    else:
        player2_coin.place(x=Index[r][0],y=Index[r][1])

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
    global im ,player1_btn,player2_btn
    # Player 1
    player1_btn = tk.Button (root,text="Player 1",height=3,width=16,bg="red",fg="blue",font=("Cursive",16,"bold"),activebackground="white",command=roll_dice)
    player1_btn.place(x=1000,y=0)
    # Player 2
    # player2_btn = tk.Button (root,text="Player 2",height=3,width=16,bg="red",fg="blue",font=("Cursive",16,"bold"),activebackground="white",command=roll_dice)
    # player2_btn.place(x=1000,y=500)
    # quit 
    quit_btn = tk.Button (root,text="Quit",command=quit_game,height=3,width=16,bg="red",fg="black",font=("Cursive",16,"bold"),activebackground="white")
    quit_btn.place(x=1000,y=600)
    # dice
    im = Image.open("./images/0.png").resize((65, 65))
    im = ImageTk.PhotoImage(im)
    b2 = tk.Button(root, image=im)
    b2.image = im  
    b2.place(x=1050, y=100)  

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
turn = 1
# ================================================
reset_coins()
load_images()
get_index()
start_game()

root.mainloop()
