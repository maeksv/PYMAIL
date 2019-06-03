import smtplib
import tkinter
import base64
from tkinter import *

gifBase='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'
"""
 id: cu.project1@gmail.com
 password:project@1

 """

def next():
    
    root1=Tk()
    root1.geometry("350x250+120+120")
    app1=Frame(root1)
    app1.grid()
    mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
    mailServer.starttls()
    label4=Label(app1,text="   WELCOME   "+ gmailaddress.get() +"    " )
    label4.grid(row=1,column=0)
    button2=Button(app1,text='SIGN OUT',command=root1.destroy).grid(row=1,column=2)
    label5=Label(app1,text="PYMAIL" ,fg="greenyellow",font="Times 20 bold ")
    label5.grid(row=2,column=0)
    button3=Button(app1,text='Compose mail ',command=create).grid(row=3 ,column=0)
    
def create():
    root2=Tk()
    root2.geometry("350x250+120+120")
    app2=Frame(root2)
    app2.grid()
    
    label6=Label(app2,text="TO :      ",font="Times 12 ")
    label6.grid(row=1)
    label7=Label(app2,text="MESSAGE :",font="Times 12 ")
    label7.grid(row=2)
    
    mailto =tkinter.StringVar()
    response=tkinter.StringVar()
    print(mailto)
    print(response)
    

    
    mailto1=Entry(app2 ,textvariable= mailto)
    mailto1.grid(row=1,column=2)
    msg1=Entry(app2 , textvariable= response )
    msg1.grid(row=2,column=2)
    msg1=repr(response)
    msg=encode(ascii)
    button4=Button(app2,text='SEND', command=sending).grid(row=7)
    
  
    
    
def sending():
    mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
    mailServer.starttls()
    mailServer.login(gmailaddress , gmailpassword)
    mailServer.sendmail(gmailaddress, mailto , msg)
    label1=Label(app,text="SENT SUCCESSFULLY")
    print(" \n Sent!")
    mailServer.quit()

root=Tk()
root.title=("PYMAIL")
root.geometry("350x250+120+120")
app=Frame(root)
app.grid()
"""
gif = tkinter.PhotoImage(data = gifBase)
displayGif = tkinter.Label(app, image = gif, borderwidth = 10).grid()

gif = Tkinter.PhotoImage(data = gifBase)
displayGif = Tkinter.Label(app, image = gif, borderwidth = 10, bg = bgColor).grid(row = 0, rowspan = 6, columnspan = 2)
        
""""""
canvas=Canvas(width=350,height=250)        
photo=PhotoImage(file="\\C:\\Users\\Hp\\Desktop\\project\\beach.jpg")
canvas.create_image(0,0,image=photo,achor=NW)"""

label=Label(app,text="WELCOME TO PYMAIL",fg="black",font="Broadway 20 bold ")
label.grid()
label1=Label(app,text="LOGIN",font="Broadway 14 bold")
label1.grid()
label2=Label(app,text="ENTER EMAIL",font="Jokerman 12 ")
label2.grid(row=3)
label3=Label(app,text="ENTER PASSWORD",font="Jokerman 12 ")
label3.grid(row=5)

gmailaddress =tkinter.StringVar()
gmailpassword =tkinter.StringVar()

address=Entry(app ,textvariable= gmailaddress)
address.grid(row=4)
password=Entry(app , textvariable= gmailpassword)
password.grid(row=6)
button1=Button(app,text='login',command=next).grid(row=7)
root.mainloop()






"""def encode(key,clear):
    enc=[]
    for i in range(len(clear)):
        key_c=key[i%len(len(key)]
        enc_c=chr((ord(clear[i])+ord{key_c))%256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode(" ".join(enc).encode()).decode()
    
print("\n")
gmailaddress = input("gmail address? \n ")
gmailpassword = input("password  \n  ")
mailto = input("what email address do you want to send your message to? \n ")
msg = input("What is your message? \n ")
mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
mailServer.starttls()
mailServer.login(gmailaddress , gmailpassword)
mailServer.sendmail(gmailaddress, mailto , msg)
print(" \n Sent!")
mailServer.quit()
"""
