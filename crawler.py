from Tkinter import *
import requests
from tkFont import Font
from bs4 import BeautifulSoup
import tkMessageBox

#Crawler

def callcrawler():
	info=z.get()
	flag=0
	if info=='':
		tkMessageBox.showinfo('ERROR','Please enter an address to crawl!!!')
	elif 'youtube.com' not in info:
		tkMessageBox.showinfo('ERROR','This crawler works only for youtube!!')
	else:
		
		try:

			f=open('links.txt','w')
			dat=requests.get(info)
			data=dat.text
			soup=BeautifulSoup(data)
			for link in soup.findAll('a',{'class':'playlist-video'}):
				# title=line.string
				addr=link.get('href')
				t=link.findAll('h4',{'class':'yt-ui-ellipsis'});
				if flag==0:
					l=link.findAll('span',{'class':'video-uploader-byline'})
					print('The series is uploaded by--\n'+l[0].getText())
					f.write('\n'+'The series is uploaded by--\n'+l[0].getText())
					T.insert(END,'\n'+'The series is uploaded by--\n'+l[0].getText(),"font")
					flag=1
				title=t[0].string
				print(title)
				f.write(title+'\n')
				T.insert(END,title+'\n',"font")
				print ('https://www.youtube.com'+addr)
				f.write('https://www.youtube.com'+addr+'\n')
				T.insert(END,'https://www.youtube.com'+addr+'\n\n')
			f.close()
		except requests.exceptions.RequestException as e:
			tkMessageBox.showinfo('ERROR','Network error, try again!!')


def cleartext():
	addr.delete(0,'end')
	T.delete(1.0,END)



#GUI


root = Tk().geometry("750x650")
v=StringVar()
z=StringVar()
tframe=Frame(root)
tframe.pack(side=TOP,pady=10,fill=X)

photo=PhotoImage(file='download.png')
photo_label=Label(tframe,image=photo)
photo_label.pack()

addrc=Label(tframe,text="Enter the Address of the Link..",font=('bold'))
addrc.pack(pady=10)
addr=Entry(tframe,textvariable=z)
addr.pack(fill=X,padx=30)
btn=Button(tframe,text="Get the links..",fg="red",bg="white",command=callcrawler)
btn.pack(pady=10,padx=30,side=LEFT)
cbtn=Button(tframe,text="Clear fields",fg="green",bg="white",command=cleartext)
cbtn.pack(pady=10,padx=20,side=LEFT)

frame=Frame(root)
frame.pack()
label=Label(frame,text="These are the links",font=('bold'))
label.pack(side=TOP,pady=20)
S = Scrollbar(frame)
T = Text(frame, height=20, width=95)
S.pack(side=RIGHT,fill=Y)
T.pack(side=LEFT)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)

f = Font(family="times", size=12, weight="bold")
T.tag_config("font", font=f)


mainloop()