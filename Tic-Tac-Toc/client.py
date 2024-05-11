from tkinter import *
from tkinter import messagebox
from socket import *
from threading import Thread

player = 0 #which player
turn = 1 #check turn (game finished or not)

def win(player):
    messagebox.showinfo(title = "Congratulation",message = 'winner is ' + player )
    wind.destroy()

def reset_game():
    global player, turn
    for button in button_list:
        button['text'] = " "
    player = 1
    turn = 1



def check():
    global turn
    turn +=1
        
    b1=bt1['text']
    b2=bt2['text']
    b3=bt3['text']
    b4=bt4['text']    
    b5=bt5['text']    
    b6=bt6['text']
    b7=bt7['text']
    b8=bt8['text']
    b9=bt9['text']
    
    if (b1==b2 and b2==b3 and b1 =='O') or (b1==b2 and b2==b3 and b1 =='X'):
        win(b1)
    if (b4==b5 and b5==b6 and b4 =='O') or (b4==b5 and b5==b6 and b4 =='X'):
        win(b4)
    if (b7==b8 and b8==b9 and b7 =='O') or (b7==b8 and b8==b9 and b7 =='X'):
        win(b7)
    if (b1==b4 and b4==b7 and b1 =='O') or (b1==b4 and b4==b7 and b1 =='X'):
        win(b1)
    if (b2==b5 and b5==b8 and b2 =='O') or (b2==b5 and b5==b8 and b2 =='X'):
        win(b2)
    if (b3==b6 and b6==b9 and b3 =='O') or (b3==b6 and b6==b9 and b3 =='X'):
        win(b3)
    if (b1==b5 and b5==b9 and b1 =='O') or (b1==b5 and b5==b9 and b1 =='X'):
        win(b1)
    if (b3==b5 and b5==b7 and b3 =='O') or (b3==b5 and b5==b7 and b3 =='X'):
        win(b3)
        
def clicked1():
    global player
    if bt1['text']==" ":
        if player == 1:
            player=2
            bt1['text']='X'
            send_play(1)
        check()

def clicked2():
    global player
    if bt2['text']==" ":
        if player == 1:
            player=2
            bt2['text']='X'
            send_play(2)
        check()
        
def clicked3():
    global player
    if bt3['text']==" ":
        if player == 1:
            player=2
            bt3['text']='X'
            send_play(3)
        check()
        
def clicked4():
    global player
    if bt4['text']==" ":
        if player == 1:
            player=2
            bt4['text']='X'
            send_play(4)
        check()
        
def clicked5():
    global player
    if bt5['text']==" ":
        if player == 1:
            player=2
            bt5['text']='X'
            send_play(5)
        check()
        
def clicked6():
    global player
    if bt6['text']==" ":
        if player == 1:
            player=2
            bt6['text']='X'
            send_play(6)
        check()
        
def clicked7():
    global player
    if bt7['text']==" ":
        if player == 1:
            player=2
            bt7['text']='X'
            send_play(7)
        check()
        
def clicked8():
    global player
    if bt8['text']==" ":
        if player == 1:
            player=2
            bt8['text']='X'
            send_play(8)
        check()
        
def clicked9():
    global player
    if bt9['text']==" ":
        if player == 1:
            player=2
            bt9['text']='X'
            send_play(9)
        check()
        
def send_play(n):
    n = str(n)
    n = n.encode()
    s.send(n)
    
def handle_play(n):
    global player
    n = n-1
    button_list [n]["text"] = "O"
    player = 1

def apply_play(p):
    p = p.decode()
    p = int(p)
    handle_play(p)

wind = Tk()

wind.title('Client: tic tac toe')
wind.geometry('260x130')

lb1 = Label(wind, text='player1: X', font=('Helvetica','15'))
lb1.grid(row=0, column=0)

button_list = list()

bt1=Button(wind, text=" ",bg="blue4",fg="orange",width = 3, height = 1,font=('Helvetica','15'),command = clicked1)
bt1.grid(row = 0, column=1)

bt2=Button(wind, text=" ",bg="blue4",fg="orange",width = 3, height = 1,font=('Helvetica','15'),command = clicked2)
bt2.grid(row = 0, column=2)

bt3=Button(wind, text=" ",bg="blue4",fg="orange",width = 3, height = 1,font=('Helvetica','15'),command = clicked3)
bt3.grid(row = 0, column=3)

bt4=Button(wind, text=" ",bg="blue4",fg="orange",width = 3, height = 1,font=('Helvetica','15'),command = clicked4)
bt4.grid(row = 1, column=1)

bt5=Button(wind, text=" ",bg="blue4",fg="orange",width = 3, height = 1,font=('Helvetica','15'),command = clicked5)
bt5.grid(row = 1, column=2)

bt6=Button(wind, text=" ",bg="blue4",fg="orange",width = 3, height = 1,font=('Helvetica','15'),command = clicked6)
bt6.grid(row = 1, column=3)

bt7=Button(wind, text=" ",bg="blue4",fg="orange",width = 3, height = 1,font=('Helvetica','15'),command = clicked7)
bt7.grid(row = 2, column=1)

bt8=Button(wind, text=" ",bg="blue4",fg="orange",width = 3, height = 1,font=('Helvetica','15'),command = clicked8)
bt8.grid(row = 2, column=2)

bt9=Button(wind, text=" ",bg="blue4",fg="orange",width = 3, height = 1,font=('Helvetica','15'),command = clicked9)
bt9.grid(row = 2, column=3)

button_list.append(bt1)
button_list.append(bt2)
button_list.append(bt3)
button_list.append(bt4)
button_list.append(bt5)
button_list.append(bt6)
button_list.append(bt7)
button_list.append(bt8)
button_list.append(bt9)


    
s = socket(AF_INET, SOCK_STREAM)

s.connect(('127.0.0.1', 7228))

def receive_message():
    while True:
        p = s.recv(10)
        apply_play(p)
        

receive =Thread(target = receive_message)
receive.start()
reset_button = Button(wind, text="Reset", command=reset_game)
reset_button.grid(row=3, column=2)
wind.mainloop()