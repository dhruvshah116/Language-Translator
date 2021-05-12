from tkinter import *
import tkinter as tk
from tkinter import ttk
#from PIL import ImageTk, Image
from googletrans import Translator
from tkinter import messagebox

def translate():
    language_1 = t1.get("1.0","end-1c")
    cl = choose_language.get() #get the language to be translated to from the user

    if language_1=='':
        messagebox.showerror("Language Translator","Please fill in the box.")

    else:
        t2.delete(1.0,"end")
        translator=Translator()
        output=translator.translate(language_1,dest=cl) #dest=cl: destination is c1 which is the language that user chooses
        t2.insert("end",output.text) #show the translated output on screen

def clear():
    t1.delete(1.0,"end")
    t2.delete(1.0,"end")

root=tk.Tk()
root.title("Language Translator")
root.geometry("530x330")
root.maxsize(530,330)
root.minsize(530,330)
a=tk.StringVar()
auto_detect = ttk.Combobox(root,width=20,textvariable=a,state='readonly',font=('verdana',10,'bold'))
auto_detect['values']=('Auto Detect',)
auto_detect.place(x=30,y=70)
auto_detect.current(0)


l=tk.StringVar()
choose_language=ttk.Combobox(root,width=20,textvariable=l,state='readonly',font=('verdana',10,'bold'))
choose_language['values']=('English','Hindi','Japanese','Chinese','Polish','German','French','Portugese',)
choose_language.place(x=290,y=70)
choose_language.current(0)

t1=Text(root,width=30,height=10,borderwidth=5,relief=RIDGE)
t1.place(x=10,y=100)

t2=Text(root,width=30,height=10,borderwidth=5,relief=RIDGE)
t2.place(x=260,y=100)

button=Button(root,text="Translate",relief=RIDGE,borderwidth=3,font=('verdana',12,'bold'),cursor='hand2',command=translate)
button.place(x=150,y=280)

clear=Button(root,text="Clear",relief=RIDGE,borderwidth=3,font=('Montserrat',12,'bold'),cursor='hand2',command=clear)
clear.place(x=280,y=280)

root.configure(bg="blue")
root.mainloop()
