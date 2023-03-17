import os
import tkinter as t
import fnmatch
from pygame import mixer

cv=t.Tk()
cv.title("Isr Music")
cv.geometry("400x1200")
cv.config(bg='skyblue')

rootpath="F:\\Venkateswara songs"
pattern= "*.mp3"

mixer.init()

def select():
    lb.config(text= listb.get("anchor"))
    mixer.music.load(rootpath + "\\" + listb.get('anchor'))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listb.select_clear('active')

def next():
    nxs=listb.curselection()
    nxs=nxs[0]+1
    nxs_name=listb.get(nxs)
    lb.config(text=nxs_name)
    mixer.music.load(rootpath + "\\" + nxs_name)
    mixer.music.play()
    listb.select_clear(0,"end")
    listb.activate(nxs)
    listb.select_set(nxs)

def prev():
    pvs=listb.curselection()
    pvs=pvs[0]-1
    pvs_name=listb.get(pvs)
    lb.config(text=pvs_name)
    mixer.music.load(rootpath + "\\" + pvs_name)
    mixer.music.play()
    listb.select_clear(0,"end")
    listb.activate(pvs)
    listb.select_set(pvs)

def pause():
    if pause["text"]=="pause":
        mixer.music.pause()
        pause['text']="play"
    else:
        mixer.music.unpause()
        pause["text"]="pause"



listb=t.Listbox(cv,fg="black",bg="pink",width=200,font=("poopins",10))
listb.pack(padx=15,pady=15)

lb=t.Label(cv, text="",bg="skyblue",fg="purple",font=("poopins",10))
lb.pack(pady=10)

tp=t.Frame(cv,bg="skyblue")
tp.pack(padx=10,pady=7,anchor='center')

prev=t.Button(cv,text="prev",command=prev)
prev.pack(pady=15,in_=tp,side="left")

play=t.Button(cv,text="start",command=select)
play.pack(pady=15,in_=tp,side="left")

pause=t.Button(cv,text="pause",command=pause)
pause.pack(pady=15,in_=tp,side="left")

stop=t.Button(cv,text="stop",command=stop)
stop.pack(pady=15,in_=tp,side="left")

next=t.Button(cv,text="next",command=next)
next.pack(pady=15,in_=tp,side="left")


for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files,pattern):
        listb.insert('end',filename)

cv.mainloop()