from tkinter import *
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(True)
from tkinter import messagebox

color=("#FFFFFF","#E0E0E0","#000000")

root=Tk()
root.config(bg="#FFFFFF")
root.title("calculator")
root.resizable(False,False)
def tk_root(event):
    global Vtext1
    a="0123456789+-*/Pp.c="
    if event.keysym=="BackSpace":
        show.back_space()
    elif event.keysym=="Return":
        calculator.click()
    elif a.find(event.char)!=-1:
        if event.char=="c":
            show.cler()
        elif event.char=="=":
            calculator.click()
        else:
            show.add_text(event.char.replace("+","➕").replace("-","➖").replace("*","✖").replace("/","➗").replace("p","P"))
root.bind('<Key>',tk_root)
Vtext1=StringVar()
Vlabel1=StringVar()
Etext1=""
Vbutton=[]
class calculator:
    def click():
        global Etext1,Vlabel1,Vtext1
        text=calculator.break_text("+"+Vtext1.get())
        text=calculator.equation(text)
        Vlabel1.set(Vtext1.get()+"="+str(text))
        Vtext1.set(text)
        if Vtext1.get()=="ZeroDivisionError" or Vtext1.get()=="error" or Vtext1.get()=="Result too large":Vtext1.set("")

    def break_text(text):
        for i in range (0,len(text)):
            text=text.replace("P","P+")
            text=text.replace("✖","*")
            text=text.replace("*","*+")
            text=text.replace("/","/+")
            text=text.replace("➗","/")
            text=text.replace("➖","-")
            text=text.replace("➕","+")
            text=text.replace("++","+")
            text=text.replace('--','+')
            text=text.replace("-+","-")
            text=text.replace("+-","-")
        Rtext=[]
        for i in range (0,len(text)):
            num=""
            if not(text[i].isnumeric()) and text[i]!=".":
                for j in range (i+1,len(text)):
                    if not(text[j].isnumeric()) and text[j]!="." :break
                    num+=str(text[j])
                Rtext.append(text[i]+num)
        return Rtext
    def equation(text):
        Sum=0
        i=0
        try:
            while i<len(text):
                try:
                    Sum+=float(text[i])
                except:
                    if text[i]=="*":
                        Sum*=float(text[i+1])
                        i+=1
                    if text[i]=="/":
                        try:
                            Sum/=float(text[i+1])
                            i+=1
                        except ZeroDivisionError:Sum="ZeroDivisionError";break
                    if text[i]=="P":
                        Sum**=float(text[i+1])
                        i+=1
                i+=1
        except ValueError:messagebox.showerror("error","The equation is written incorrectly");Sum="error"
        except OverflowError:messagebox.showerror("error","The Result too large");Sum="Result too large"
        return Sum
class show:
    global Vtext1,root,Etext1,Vbutton,Vlabel1
    Label(root,textvariable=Vlabel1,font=("Helvetica", 8),bg="#FFFFFF").grid(row=0,column=0,columnspan=4)
    Etext1=Label(root,textvariable=Vtext1,font=("Helvetica", 15),width=26)
    Etext1.grid(row=1,column=0,columnspan=4)
    def add_text(T):
        global Etext1,Vtext1
        if T==".":
            test=calculator.break_text("+"+Vtext1.get())
            if len(test)==0 or str(test[len(test)-1])=="+":
                T="0."
            else:T="."
        Vtext1.set(Vtext1.get()+T)
    def back_space():
        global Etext1,Vtext1
        Vtext1.set(Vtext1.get()[:len(Vtext1.get())-1])
    def cler():
        global Vtext1,Vlabel1
        Vtext1.set("")
        Vlabel1.set("")
    Vbutton.append(Button(root,fg=color[2],text="1",font=18,width=8,height=3,bg=color[0],command=lambda:show.add_text("1")));Vbutton[0].grid(row=2,column=0)
    Vbutton.append(Button(root,fg=color[2],text="2",font=18,width=8,height=3,bg=color[0],command=lambda:show.add_text("2")));Vbutton[1].grid(row=2,column=1)
    Vbutton.append(Button(root,fg=color[2],text="3",font=18,width=8,height=3,bg=color[0],command=lambda:show.add_text("3")));Vbutton[2].grid(row=2,column=2)
    Vbutton.append(Button(root,fg=color[2],text="4",font=18,width=8,height=3,bg=color[0],command=lambda:show.add_text("4")));Vbutton[3].grid(row=3,column=0)
    Vbutton.append(Button(root,fg=color[2],text="5",font=18,width=8,height=3,bg=color[0],command=lambda:show.add_text("5")));Vbutton[4].grid(row=3,column=1)
    Vbutton.append(Button(root,fg=color[2],text="6",font=18,width=8,height=3,bg=color[0],command=lambda:show.add_text("6")));Vbutton[5].grid(row=3,column=2)
    Vbutton.append(Button(root,fg=color[2],text="7",font=18,width=8,height=3,bg=color[0],command=lambda:show.add_text("7")));Vbutton[6].grid(row=4,column=0)
    Vbutton.append(Button(root,fg=color[2],text="8",font=18,width=8,height=3,bg=color[0],command=lambda:show.add_text("8")));Vbutton[7].grid(row=4,column=1)
    Vbutton.append(Button(root,fg=color[2],text="9",font=18,width=8,height=3,bg=color[0],command=lambda:show.add_text("9")));Vbutton[8].grid(row=4,column=2)
    Vbutton.append(Button(root,fg=color[2],text="0",font=18,width=8,height=3,bg=color[0],command=lambda:show.add_text("0")));Vbutton[9].grid(row=5,column=1)
    Vbutton.append(Button(root,fg=color[2],text="000",font=18,width=8,height=3,bg=color[0],command=lambda:show.add_text("000")));Vbutton[10].grid(row=5,column=0)
    Vbutton.append(Button(root,fg=color[2],text="●",font=18,width=8,height=3,bg=color[0],command=lambda:show.add_text(".")));Vbutton[11].grid(row=5,column=2)
    Vbutton.append(Button(root,fg=color[2],text="➕",font=18,width=8,height=3,bg=color[1],command=lambda:show.add_text("➕")));Vbutton[12].grid(row=2,column=3)
    Vbutton.append(Button(root,fg=color[2],text="➖",font=18,width=8,height=3,bg=color[1],command=lambda:show.add_text("➖")));Vbutton[13].grid(row=3,column=3)
    Vbutton.append(Button(root,fg=color[2],text="✖",font=18,width=8,height=3,bg=color[1],command=lambda:show.add_text("✖")));Vbutton[14].grid(row=4,column=3)
    Vbutton.append(Button(root,fg=color[2],text="➗",font=18,width=8,height=3,bg=color[1],command=lambda:show.add_text("➗")));Vbutton[15].grid(row=5,column=3)
    Vbutton.append(Button(root,fg=color[2],text="P",font=18,width=8,height=3,bg=color[1],command=lambda:show.add_text("P")));Vbutton[16].grid(row=6,column=3)
    Vbutton.append(Button(root,fg=color[2],text="C",font=18,width=8,height=3,bg=color[1],command=lambda:show.cler()));Vbutton[17].grid(row=6,column=0)
    Vbutton.append(Button(root,fg=color[2],text="＝",font=18,width=8,height=3,bg=color[1],command=lambda:calculator.click()));Vbutton[18].grid(row=6,column=2)
    Vbutton.append(Button(root,fg=color[2],text="BS",font=18,width=8,height=3,bg=color[1],command=lambda:show.back_space()));Vbutton[19].grid(row=6,column=1)

show()




root.mainloop()
