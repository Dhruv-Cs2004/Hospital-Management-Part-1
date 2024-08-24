from tkinter import *
from tkinter import messagebox
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from PIL import ImageTk,Image
import mysql.connector
import os

  

def temp_text(e):
   user_inut.delete(0,"end")

def temp_text1(e):
   pass_inut.delete(0,"end") 

def temp_text2(e):
   name_input.delete(0,"end") 

def temp_text3(e):
   name_input1.delete(0,"end")   

def temp_text4(e):
   name_user.delete(0,"end") 

def temp_text5(e):
   phone_input.delete(0,"end")    

def temp_text6(e):
   pass_input.delete(0,"end")  

 

def chek():
   state=var1.get()
   if state==1:
         mysqldb=mysql.connector.connect(
         host="127.0.0.1",
         user="root",
         password="Sonia1978",
         database="hospital"
      )
         mycursor=mysqldb.cursor()
         email=user_inut.get()
         password=pass_inut.get()

         sql="select * from login where email = %s and password = %s"
         mycursor.execute(sql,[(email),(password)])
         result=mycursor.fetchall()
         if result:
            os.system(f'python {'mainpage.py'}')
            
         else:
            messagebox.showinfo("information","incorrect user and password")
   else:
      messagebox.showinfo("information","click the check box")      



def DateEntry():
   if(var2.get()==1):
         try:
            first=name_input.get()
            last=name_input1.get()
            user=name_user.get()
            phone=phone_input.get()
            birth=birth_input.entry.get()
            Password=pass_input.get()
            mysqldb=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Sonia1978",
            database="hospital")
            mycursor=mysqldb.cursor()
            ind="INSERT INTO login (user, last, email, password, dates, PHno) VALUES(%s,%s,%s,%s,%s,%s)"
            t=(first,last,user,Password,birth,phone)
            mycursor.execute(ind,t)
            mysqldb.commit(); 
            root1.destroy()
            messagebox.showinfo("informattion","Welcome new user")
             
         except:
            messagebox.showinfo("informattion","Fill all the information correctly")

   else:
      messagebox.showinfo("information","PLZ agree the rerms and condition")

def close():
   
   root1.destroy()



root=tb.Window(themename='darkly')
root.geometry('900x600')
root.resizable(0,0)
root.title('Hospita Login Page')

var1=IntVar()
var2=IntVar()

my_image=Image.open('logo and images/medical-stethoscope-isolated-with-black-background-medical-concept-stethoscope-black-background-with-space-text-health-concept-medical-conceptual.jpg')
resize_image=my_image.resize((900,600))

img = ImageTk.PhotoImage((resize_image))
img_label=Label(root,image=img)
img_label.place(x=1,y=1,relwidth=1,relheight=1)


frame =Frame(root, highlightthickness=0,width=300, height=400)  
frame.grid(pady=(75,5),padx=(60,5))  

sinin_lab=tb.Label(text='Login',font=('verdina',25,'italic','bold'))
sinin_lab.grid(row=0,column=0,pady=(15,250),padx=(80,45))

user_inut=Entry(root,bg="white",width=25, borderwidth=10)
user_inut.insert(0,'Email')
user_inut.grid(row=0,column=0,pady=(15,120),padx=(90,45))
user_inut.bind("<FocusIn>", temp_text)

pass_inut=Entry(root,bg="white",width=25, borderwidth=10)
pass_inut.insert(1,'Password')
pass_inut.grid(row=0,column=0,pady=(30,10),padx=(90,45))
pass_inut.bind("<FocusIn>", temp_text1)

my_style=tb.Style()
my_style.configure('info.outline-toolbutton.TButton',font=('vardina',15,'bold'))

sign_button=tb.Button(text='SignIn',style='warming.outline-toolbutton.TButton',command=lambda:chek())
sign_button.grid(row=0,column=0,pady=(160,10),padx=(0,55))

check_but=tb.Checkbutton(root,text='I agree all terms..',bootstyle="warning",variable=var1,onvalue=1,offvalue=0)
check_but.grid(row=0,column=0,pady=(240,10),padx=(80,45))

my_style=tb.Style()
my_style.configure('info.outline-toolbutton.TButton',font=('vardina',15,'bold'))

creat_new=tb.Button(text='SignUp',style='warming.outline-toolbutton.TButton',command=lambda:new_tab())
creat_new.grid(row=0,column=0,pady=(160,10),padx=(200,45))

def new_tab():
   global name_input,name_input1,name_user,phone_input,pass_input,birth_input,root1
   root1=Toplevel()
   root1.geometry('900x600')
   root1.title('creat new Account')
   root1.resizable(0,0)

   img_label=Label(root1,image=img)
   img_label.place(x=1,y=1,relwidth=1,relheight=1)

   frame1=Frame(root1, highlightthickness=0,width=450, height=500)  
   frame1.grid(pady=(75,5),padx=(60,5)) 

   user_new=tb.Label(root1, text='Creat New Account',font=('verdina',25,'italic','bold'))
   user_new.grid(row=0,column=0,pady=(20,350),padx=(60,10))

   name_input=Entry(root1,bg="white",width=15, borderwidth=10)
   name_input.insert(0,'Enter first name')
   name_input.grid(row=0,column=0,pady=(15,165),padx=(85,215))
   name_input.bind("<FocusIn>", temp_text2)

   name_input1=Entry(root1,bg="white",width=15, borderwidth=10)
   name_input1.insert(0,'Enter last name')
   name_input1.grid(row=0,column=0,pady=(15,165),padx=(470,215))
   name_input1.bind("<FocusIn>", temp_text3)

   name_user=Entry(root1,bg="white",width=15, borderwidth=10)
   name_user.insert(0,'Enter EmailId')
   name_user.grid(row=0,column=0,pady=(15,40),padx=(85,215))
   name_user.bind("<FocusIn>", temp_text4)

   phone_input=Entry(root1,bg="white",width=15, borderwidth=10)
   phone_input.insert(0,'Enter your Phone.No')
   phone_input.grid(row=0,column=0,pady=(125,40),padx=(470,215))
   phone_input.bind("<FocusIn>", temp_text5)

   birth_input=tb.DateEntry(root1,width=13, borderwidth=10,dateformat='%d/%m/%Y')
   birth_input.grid(row=0,column=0,pady=(125,40),padx=(85,215))


   pass_input=Entry(root1,bg="white",width=15, borderwidth=10)
   pass_input.insert(0,'Enter New Password')
   pass_input.grid(row=0,column=0,pady=(15,40),padx=(470,215))
   pass_input.bind("<FocusIn>", temp_text6)

   check_but1=tb.Checkbutton(root1,text='I agree all terms & Conditions..',bootstyle="warning",variable=var2,onvalue=1,offvalue=0)
   check_but1.grid(row=0,column=0,pady=(240,10),padx=(80,45))

   my_style1=tb.Style()
   my_style1.configure('outline-toolbutton.TButton',font=('vardina',30))

   creat_acc=tb.Button(root1,text='creat',style='outline.TButton',width=20,command=DateEntry)
   creat_acc.grid(row=0,column=0,pady=(340,10),padx=(130,95))

root.mainloop()