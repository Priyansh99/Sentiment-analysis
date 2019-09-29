from tkinter import *

def spam():
	root.destroy()
	import spam

def review():
	root.destroy()
	import review
root=Tk()
root.state('zoomed')
root.resizable(width=False,height=False)
root.configure(background='yellow')
l=Label(root,text='Sentiment Analysis',bg='yellow',font=('',40,'bold'))
l.pack()

b1=Button(root,command=spam,text='Spam Detection',font=('',20,'bold'))
b1.place(x=300,y=100)

b2=Button(root,command=review,text='Review Analysis',font=('',20,'bold'))
b2.place(x=300,y=200)

root.mainloop()
