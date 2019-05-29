from tkinter import*
a=Tk()
a.title('con ga')

b=IntVar()

rad1=Radiobutton(a,text='first',value=1,variable=b)
rad2=Radiobutton(a,text='second',value=2,variable=b)
rad3=Radiobutton(a,text='ba',value=3,variable=b)
def Click():
    print(b.get())
bnt=Button(a,text='click me',command=Click)

rad1.grid(column=0,row=0)
rad2.grid(column=1,row=0)
rad3.grid(column=2,row=0)
bnt.grid(column=3,row=0)
a.mainloop()