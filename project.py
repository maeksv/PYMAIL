import smtplib
import base64
"""
 id: cu.project1@gmail.com
 password:project@1

 """
def relogin():
    a=input()
    if a=='y':
       login()
    else:
        print("wrong selection")
        print("TRY AGAIN")
        relogin()
def signout():
    print("print any key to signout ")
    relogin()
    
def att():
    filename=input("Enter Path")
    fo=open(filename,"rb")
    filecontent = fo.read()
    encodedcontent = base64.b64encode(filecontent)
    msg=msg1+encodedcontent
                  
def login():    #prog starts here!
    try:
        gmailaddress = input(" gmail address? \n ")
        gmailpassword = input("password : \n  ")
        mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
        mailServer.starttls()
        mailServer.login(gmailaddress , gmailpassword)
        print("WELCOME " + gmailaddress)
        print("  MENU  ")
        print(" 1. compose \n ")
        print(" 2. retrieve ")
        ch=int(input("enter your selection"))
        if (ch==1):
            mailto = input("TO: \n ")
            msg = input("MESSAGE : \n ")
            b=input("attachment? (y/n)")
            if (b=='y'):
                print("upload ") #att() will be call .we need to add attachment
                att()
            else:
                print("...")
            try:
                mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
                mailServer.starttls()
                mailServer.login(gmailaddress , gmailpassword)
                mailServer.sendmail(gmailaddress, mailto , msg)
                print(" \n Sent!")
                mailServer.quit()
                signout()
            except SMTPException:
                print ("Error: unable to send email")
        else:
            print("service unavailable")
    except:
        print("LOGIN FAILED")
        print("Press 'y' to RELOGIN")
        relogin()
    


login()






