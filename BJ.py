#coding:utf-8
import random
import tkinter as tk
import tkinter.messagebox as mb

remain=list(range(52))
card_list=[[0,0]]
counter=0
card_place=[30,-180]
RESULT=[0,0,0]

def deck():#[スート,数値]
    numbers=["1","2","3","4","5","6","7","8","9","10","J","Q","K"]
    soots=["S","H","D","C"]
    for i in range(4):
        for j in range(13):
            remain[i*13+j]=[soots[i],numbers[j]]
    return remain

remain=deck()

def trans(list1):
    
    if list1[1]=="J":
        a=10
    elif list1[1]=="Q":
        a=10
    elif list1[1]=="K":
        a=10
    else:
        a=int(list1[1])
    return [list1[0],a]

def choice():#remain中の要素をランダムに一つ選びそれを返り値とし、remainから削除
    global remain
    
    
    place=random.randint(0,len(remain)-1)
    for_return=remain[place]
    remain[place:place+1]=[]
    return for_return

def put_card(card_place,card,card_area):#カードを設置
    global counter
    if counter==12:
        return 0
    if counter%6==0:
        card_place[1]+=200
        card_place[0]=20
    card_area.create_rectangle(card_place[0],card_place[1],card_place[0]+140,\
                        card_place[1]+180)
    card_area.create_text(card_place[0]+70,card_place[1]+50,text=card[0],font=("helvetica",40))
    card_area.create_text(card_place[0]+70,card_place[1]+120,text=card[1],font=("helvetica",40))
    card_place[0]+=160
    counter+=1

def add_list(card,card_list):
    card_list[-1:len(card_list)]=[card,[0,0]]


def jud (list1):#リスト化された手札から、結果を判定
    global RESULT
    total=0
    total1=0
    A=False
    for i in list1:
        if trans(i)[1]==1:
            A=True
            break
    for i in list1:
        total+=trans(i)[1]

    if total>=22:
        return "burst"
    elif A :
        if total+10>=22:
            return total
        else:
            if total+10==21 and len(list1)==3:
                return "BJ"
            else:
                return total+10
    else:
        return total
    
        

def HIT():
    global card_list
    a=choice()
    put_card(card_place,a,card_area)
    add_list(a,card_list)

def STAND():
    global card_list
    mb.showinfo("RESULT",jud(card_list))
    global remain
    remain=list(range(52))
    remain=deck()
    card_list=[[0,0]]
    global card_area
    card_area.create_rectangle(0,0,1000,550,fill="white")
    global counter
    counter=0
    global card_place
    card_place=[30,-180]
    
    


BJ=tk.Tk()

BJ.geometry("1000x800")
BJ.title("BJ")

card_area=tk.Canvas(BJ,width=1000,height=500,bg="white")
card_area.place(x=0,y=0)

hit_button=tk.Button(BJ,text="HIT",font=("Helvetica",40),command=HIT)
hit_button.place(x=100,y=550)

stand_button=tk.Button(BJ,text="STAND",font=("Helvetica",40),command=STAND)
stand_button.place(x=600,y=550)


BJ.mainloop
        
    

