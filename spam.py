from tkinter import *
import string
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


def removePunc(doc):
	pc=string.punctuation
	clean_doc=re.sub(f'[{pc}]','',doc)
	return clean_doc

df=pd.read_csv('sms.txt',delimiter='\t')
df.columns=['type','msg']
df['msg']=df.msg.apply(removePunc)
cv=TfidfVectorizer(stop_words='english')
X=cv.fit_transform(df.msg).todense()
gnb=MultinomialNB()
gnb.fit(X,df.type)	

def mypredict():
	new_rvw=e.get()
	X_test=cv.transform([new_rvw]).todense()
	p=gnb.predict(X_test)
	if(p[0]=='ham'):
		l3.configure(text='Ham',fg='green')
	else:
		l3.configure(text='Spam',fg='red')

root=Tk()
root.state('zoomed')
root.resizable(width=False,height=False)
root.configure(background='yellow')
l=Label(root,text='Spam Detection',bg='yellow',font=('',40,'bold'))
l.pack()

l2=Label(root,text='Enter Msg:',bg='yellow',font=('',20,'bold'))
l2.place(x=100,y=200)

l3=Label(root,text='',bg='yellow',font=('',20,'bold'))
l3.pack(padx=300,pady=50)

e=Entry(root,font=('',20,'bold'))
e.place(x=300,y=200)

b=Button(root,command=mypredict,text='Predict',font=('',20,'bold'))
b.place(x=300,y=300)

root.mainloop()
