from tkinter import *

def login():
	u=e1.get()
	p=e2.get()
	if(u=='admin' and p=='admin'):
		root.destroy()
		import welcome
	else:
		l4.configure(text='Invalid Username/Password',fg='red')
root=Tk()
root.state('zoomed')
root.resizable(width=False,height=False)
photo1=PhotoImage(file="C:\\Users\\Priyansh Mishra\\Pictures\\Saved Pictures\\neal_everson001005.gif")
root.configure(root,image=photo1,background='yellow')

l=Label(root,image=photo1,text='Sentiment Analysis',bg='yellow',font=('',40,'bold'))
l.pack()

l2=Label(root,text='Username:',bg='yellow',font=('',20,'bold'))
l2.place(x=120,y=200)

l3=Label(root,text='Password:',bg='yellow',font=('',20,'bold'))
l3.place(x=120,y=300)

l4=Label(root,text='',bg='yellow',font=('',20,'bold'))
l4.place(x=120,y=100)

e1=Entry(root,font=('',20,'bold'))
e1.place(x=300,y=200)

e2=Entry(root,font=('',20,'bold'))
e2.place(x=300,y=300)

b=Button(root,command=login,text='Login',font=('',20,'bold'))
b.place(x=300,y=400)

root.mainloop()
