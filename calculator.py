from tkinter import *
from tkinter.messagebox import *




root=Tk()
root.title("CALCULATOR")
topframe=Frame(root)
topframe.pack()
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)
operator=""
entertext=StringVar()



m=Menu(root)
root.config(menu=m)


sm=Menu(m)
m.add_cascade(label="SAVE",menu=sm)
sm.add_command(label="SAVE AS")


sm1=Menu(m)
m.add_cascade(label="HISTORY",menu=sm1)
sm1.add_command(label="EXIT",command=root.quit)



def key(event):
    #if event.char == event.keysym:
        global operator
        operator =operator +  event.char
        entertext.set(operator)
        entry.config(text=entertext)


def btnclick(number):
    global operator

    operator = operator + str(number)
    entertext.set(operator)
    #entry.config(operator)
    #operator=""
def equalbtn(event=None):
 try:

    global operator
    add=str(eval(operator))
    add=add+("\n")
    entertext.set(add)
    #temp=entertext.get()
    text.insert(END,add)
 except :
    entertext.set("error")

def clearText(event=None):
        global operator
        entry.delete(0,"end")
        operator=""



def cancel(event=None):
    global operator,result
    operator = entry.get()
    entry.delete(0, 65)
    entry.insert(0, operator[0: len(operator) - 1])
    operator = entry.get()
    #strStr = entry.get()
    #operator=entertext.set(strStr)
    #print(entry.get())




label1=Label(topframe,text="Enter number")
label1.pack()

entry=Entry(topframe,width=40,textvar=entertext)
entry.pack()

sc=Scrollbar(topframe)
text=Text(topframe,width=25,height=2,yscrollcommand=sc.set)
sc.config(command=text.yview)
sc.pack(side="right",fill="y")

text.pack()


#text.insert(END,result)


b7=Button(bottomframe,text="7",height=1, width=7,command=lambda : btnclick(7))
b7.grid(row=1)
b4=Button(bottomframe,text="4",height=1, width=7,command=lambda : btnclick(4))
b4.grid(row=2)
b1=Button(bottomframe,text="1",height=1, width=7,command=lambda : btnclick(1))
b1.grid(row=3)


b8=Button(bottomframe,text="8",height=1, width=7,command=lambda : btnclick(8))
b8.grid(row=1,column=1)
b5=Button(bottomframe,text="5",height=1, width=7,command=lambda : btnclick(5))
b5.grid(row=2,column=1)
b2=Button(bottomframe,text="2",height=1, width=7,command=lambda : btnclick(2))
b2.grid(row=3,column=1)

b9=Button(bottomframe,text="9",height=1, width=7,command=lambda : btnclick(9))
b9.grid(row=1,column=2)
b6=Button(bottomframe,text="6",height=1, width=7,command=lambda : btnclick(6))
b6.grid(row=2,column=2)
b3=Button(bottomframe,text="3",height=1, width=7,command=lambda : btnclick(3))
b3.grid(row=3,column=2)

badd=Button(bottomframe,text="+",height=1, width=7,command=lambda : btnclick("+"))
badd.grid(row=1,column=3)
bsub=Button(bottomframe,text="-",height=1, width=7,command=lambda : btnclick("-"))
bsub.grid(row=2,column=3)
bmul=Button(bottomframe,text="*",height=1, width=7,command=lambda : btnclick("*"))
bmul.grid(row=3,column=3)
bdiv=Button(bottomframe,text="/",height=1, width=7,command=lambda : btnclick("/"))
bdiv.grid(row=4,column=3)
bdot=Button(bottomframe,text=".",height=1, width=7,command=lambda : btnclick("."))
bdot.grid(row=4,column=2)

equal=Button(bottomframe,text="c",height=1, width=7,command=lambda : clearText())
equal.grid(row=4)

zero=Button(bottomframe,text="0",height=1, width=7,command=lambda : btnclick(0))
zero.grid(row=4,column=1)

bb1=Button(bottomframe,text="(",height=1, width=7,command=lambda : btnclick("("))
bb1.grid(row=5)
bb2=Button(bottomframe,text=")",height=1, width=7,command=lambda : btnclick(")"))
bb2.grid(row=5,column=1)
bb3=Button(bottomframe,text="del",height=1, width=7,command=lambda : cancel())
bb3.grid(row=5,column=2)
bb4=Button(bottomframe,text="%",height=1, width=7,command=lambda : btnclick("%"))
bb4.grid(row=5,column=3)

clear=Button(bottomframe,text="RESULT", command=lambda :equalbtn(),height=1, width=7)
#clear.bind('<Return>', equalbtn)
clear.grid(row=6,columnspan=4,sticky=N+S+E+W)






root.bind_all('<Key>', key)
root.bind_all('<Return>', equalbtn)
root.bind_all('<Delete>', clearText)
root.bind_all('<BackSpace>', cancel)





root.mainloop()
