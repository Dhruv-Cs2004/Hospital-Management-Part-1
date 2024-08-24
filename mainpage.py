from tkinter import *
from tkinter import messagebox
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame
import ttkbootstrap as tb
from PIL import ImageTk,Image
import random
import mysql.connector




root2=tb.Window(themename='darkly')
root2.geometry('900x600')
root2.resizable(0,0)
root2.title('Hospital Main')

def Homepage():
    def temp_text(e):
        email_inut.delete(0,"end")

    def temp_text1(e):
        phno_inut.delete(0,"end")

    def temp_text2(e):
        text_inut.delete(1.0,"end")  



    def submit():
        try:
            mysqldb=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Sonia1978",
            database="hospital")
            
            mail=email_inut.get()
            number=phno_inut.get()
            rew=text_inut.get("1.0",END)


            mycursor=mysqldb.cursor()
            ind="INSERT INTO feedback (email,phoneno,revew) VALUES(%s,%s,%s)"
            t=(mail,number,rew)
            mycursor.execute(ind,t)
            mysqldb.commit();    
            messagebox.showinfo("information","Review Submit sucessfully")
        except mysql.connector.errors.IntegrityError:
            messagebox.showinfo("information","fill the information correctly\nor\ndont use same email again and again")


    mysqldb=mysql.connector.connect(
         host="127.0.0.1",
         user="root",
         password="Sonia1978",
         database="hospital")
    mycursor=mysqldb.cursor()
    sql="SELECT COUNT(ward) FROM patient WHERE ward = 'ICU'"
    mycursor.execute(sql)
    result=mycursor.fetchone()
    out=result[0]

    sql="SELECT COUNT(ward) FROM patient WHERE ward = 'Deluxe'"
    mycursor.execute(sql)
    result=mycursor.fetchone()
    out1=result[0]

    sql="SELECT COUNT(ward) FROM patient WHERE ward = 'General'"
    mycursor.execute(sql)
    result=mycursor.fetchone()
    out2=result[0]

    sql="SELECT COUNT(ward) FROM patient WHERE ward = 'Children'"
    mycursor.execute(sql)
    result=mycursor.fetchone()
    out3=result[0]

    home_frame=Frame(root2,width=900,height=900)
    home_frame.place(x=140,y=0)
    home_frame1=Frame(root2,width=900,height=900)
    home_frame1.place(x=140,y=180)

    my_meter1=tb.Meter(master=home_frame,
                       bootstyle="info",
                       amountused=out,
                       amounttotal=20,
                       stripethickness=10,
                       metertype="semi",
                       textright="/20",
                       subtext="Bed's in ICU",
                       textfont=("Helvetica", 16, "bold"),
                       subtextstyle="info",
                       meterthickness=20
                    #  arcrange=150,
                    )
    my_meter1.grid(row=0, column=0,padx=20,pady=20)

    my_meter2=tb.Meter(master=home_frame,
                       bootstyle="info",
                       amountused=out1,
                       stripethickness=10,
                       metertype="semi",
                       textright="/70",
                       amounttotal=70,
                       subtext="Delux Room",
                       textfont=("Helvetica", 16, "bold"),
                       subtextstyle="info",
                       meterthickness=20
                    )
    my_meter2.grid(row=0, column=1,padx=20,pady=20)

    my_meter3=tb.Meter(master=home_frame,
                       bootstyle="info",
                       amountused=out2,
                       stripethickness=10,
                       metertype="semi",
                       textright="/100",
                       amounttotal=100,
                       subtext="Gernal Ward",
                       textfont=("Helvetica", 16, "bold"),
                       subtextstyle="info",
                       meterthickness=20
                    )
    my_meter3.grid(row=0, column=2,padx=20,pady=20)

    my_meter3=tb.Meter(master=home_frame,
                       bootstyle="info",
                       amountused=out3,
                       stripethickness=10,
                       metertype="semi",
                       textright="/80",
                       amounttotal=80,
                       subtext="Children ward",
                       textfont=("Helvetica", 16, "bold"),
                       subtextstyle="info",
                       meterthickness=20
                    )
    my_meter3.grid(row=0, column=3,padx=20,pady=20)


    feedback_lab=Label(root2,text='Feedback',font=('verdina',25,'italic','bold'))
    feedback_lab.place(y=200,x=250)

    global images
    feed = Image.open('logo and images/review_9123411.png')
    resize_feed1=feed.resize((35,35))
    images=ImageTk.PhotoImage((resize_feed1))
    image_label=Label(root2,image=images)
    image_label.place(y=200,x=200)

    

    email_inut=Entry(root2,width=25, borderwidth=10)
    email_inut.insert(0,'Email')
    email_inut.grid(row=0,column=0,pady=(15,460),padx=(0,325))
    email_inut.bind("<FocusIn>",temp_text)

    phno_inut=Entry(root2,width=25, borderwidth=10)
    phno_inut.insert(0,'PhoneNo')
    phno_inut.grid(row=0,column=0,pady=(15,360),padx=(0,325))
    phno_inut.bind("<FocusIn>",temp_text1)

    text_inut=Text(root2,width=27, height=5)
    text_inut.insert(1.0,'write your views')
    text_inut.grid(row=0,column=0,pady=(15,180),padx=(0,318))
    text_inut.bind("<FocusIn>",temp_text2)

    submit_button=tb.Button(root2,text='Submit',width=10,style='warning.outline-toolbutton.TButton',command=lambda:submit())
    submit_button.grid(row=0,column=0,pady=(25,0),padx=(0,460))

    contactus_lab=tb.Label(root2,text='Contact Us',font=('verdina',25,'italic','bold'))
    contactus_lab.grid(row=0,column=0,pady=(15,170),padx=(400,0))

    global images1,images2,images3
    contac = Image.open('logo and images/globe_1042096.png')
    resize_feed2=contac.resize((35,35))
    images1=ImageTk.PhotoImage((resize_feed2))
    image_contact=Label(root2,image=images1)
    image_contact.place(y=400,x=580)

    contact_lab=tb.Label(root2,text='1800-2800-20',font=('verdina',20,'italic','bold'))
    contact_lab.grid(row=0,column=0,pady=(15,83),padx=(420,0))
     
    phone = Image.open('logo and images/telephone_14875580.png')
    resize_phone=phone.resize((25,25))
    images2=ImageTk.PhotoImage((resize_phone))
    image_phone=Label(root2,image=images2)
    image_phone.place(y=450,x=590)

    link_lab=tb.Label(root2,text='https://www.aiims.edu',font=('verdina',20,'italic','bold'))
    link_lab.grid(row=0,column=0,pady=(22,0),padx=(505,0))

    link = Image.open('logo and images/link_1017466.png')
    resize_link=link.resize((25,25))
    images3=ImageTk.PhotoImage((resize_link))
    image_link=Label(root2,image=images3)
    image_link.place(y=500,x=590)


def Doctor():
    mysqldb=mysql.connector.connect(
         host="127.0.0.1",
         user="root",
         password="Sonia1978",
         database="hospital")
    
    mycursor=mysqldb.cursor()
    sql2="SELECT COUNT(doctorno) FROM doctor"
    mycursor.execute(sql2)
    result2=mycursor.fetchone()
    
    mycursor=mysqldb.cursor()
    sql1="SELECT COUNT(staffno) FROM staff"
    mycursor.execute(sql1)
    result1=mycursor.fetchone()

    mycursor=mysqldb.cursor()
    sql="SELECT COUNT(patisno) FROM patient"
    mycursor.execute(sql)
    result=mycursor.fetchone()


    doctor_frame=Frame(master=root2,width=900,height=900,)
    doctor_frame.place(x=140,y=0)

    global imagedock
    doctorinfo_frame=Frame(doctor_frame,width=200,height=100)
    doctorinfo_frame.config(bg='orange1')
    doctorinfo_frame.place(x=40,y=60)

    dockinfo = Image.open('logo and images/medical-assistance.png')
    resize_dockinfo=dockinfo.resize((45,45))
    imagedock=ImageTk.PhotoImage((resize_dockinfo))
    dockimage_label=tb.Label(doctorinfo_frame,image=imagedock,background='orange1')
    dockimage_label.place(y=25,x=130)

    total_dock=tb.Label(doctorinfo_frame,text=result2,font=('verdina',25,'bold'))
    total_dock.config(background="orange1", foreground="black")
    total_dock.place(y=25,x=50)

    total1_dock=tb.Label(doctorinfo_frame,text="Total Doctors",font=('verdina',15,'bold'))
    total1_dock.config(background="orange1", foreground="black")
    total1_dock.place(y=60,x=20)

    global imagestaf
    stafinfo_frame=Frame(doctor_frame,width=200,height=100)
    stafinfo_frame.config(bg='deep sky blue')
    stafinfo_frame.place(x=270,y=60)

    stafinfo = Image.open('logo and images/doctors.png')
    resize_satafinfo=stafinfo.resize((45,45))
    imagestaf=ImageTk.PhotoImage((resize_satafinfo))
    dockstaf_label=tb.Label(stafinfo_frame,image=imagestaf,background='deep sky blue')
    dockstaf_label.place(y=25,x=130)

    total_staf=tb.Label(stafinfo_frame,text=result1,font=('verdina',25,'bold'))
    total_staf.config(background="deep sky blue", foreground="black")
    total_staf.place(y=25,x=50)

    total_staf1=tb.Label(stafinfo_frame,text="Total Staff",font=('verdina',15,'bold'))
    total_staf1.config(background="deep sky blue", foreground="black")
    total_staf1.place(y=60,x=25)


    global imagepatient
    patientinfo_frame=Frame(doctor_frame,width=200,height=100)
    patientinfo_frame.config(bg='red')
    patientinfo_frame.place(x=500,y=60)

    patientinfo = Image.open('logo and images/hospital.png')
    resize_patientinfo=patientinfo.resize((45,45))
    imagepatient=ImageTk.PhotoImage((resize_patientinfo))
    patientimage_label=tb.Label(patientinfo_frame,image=imagepatient,background='red')
    patientimage_label.place(y=25,x=130)

    total_patient=tb.Label(patientinfo_frame,text=result,font=('verdina',25,'bold'))
    total_patient.config(background="red", foreground="black")
    total_patient.place(y=25,x=50)

    total_patient1=tb.Label(patientinfo_frame,text="Total Patient",font=('verdina',15,'bold'))
    total_patient1.config(background="red", foreground="black")
    total_patient1.place(y=60,x=25)


    def find():
        mysqldb=mysql.connector.connect(
         host="127.0.0.1",
         user="root",
         password="Sonia1978",
         database="hospital")
        dock_detail=combobox.get()
        mycursor=mysqldb.cursor()
        sql="SELECT * from doctor where specialization=%s"
        t=(dock_detail)
        mycursor.execute(sql,(t,))
        result = mycursor.fetchall() 
        for item in result:
            tree.insert("", "end", values=item)

    find_dock=tb.Label(doctor_frame,text="Find the Doctor",font=('Arial',30,'bold'))
    find_dock.place(y=200,x=240)

    options=['Cardiologist','Neurologist','Orthopedic Surgeon','Pediatrician','Dermatologist','Gastroenterologist','General Practitioner','Oncologist','Endocrinologist','Ophthalmologist']
    combobox = tb.Combobox(doctor_frame,state='readonly',value=options)
    combobox.set("Select The Problem")
    combobox.place(x=130,y=260)
        

    find_button=tb.Button(doctor_frame,text='Find Doctor',width=10,style='warning.outline-toolbutton.TButton',command=lambda:find())
    find_button.place(y=260,x=440)
    
    info_frame=Frame(doctor_frame,width=720,height=270)
    info_frame.config(bg='orange1')
    info_frame.grid(row=0,column=0,padx=80,pady=330)


    tree = tb.Treeview(info_frame, columns=("DoctorNo", "Name", "Age", "Specialization", "PHoneNO"), show="headings")

    tree.heading("DoctorNo", text="DoctorNo")
    tree.heading("Name", text="Name")
    tree.heading("Age", text="Age")
    tree.heading("Specialization", text="Specialization")
    tree.heading("PHoneNO", text="PHoneNO")
    
    tree.column("DoctorNo", width=90,anchor="center")
    tree.column("Name", width=137,anchor="center")
    tree.column("Age", width=50,anchor="center")
    tree.column("Specialization", width=137,anchor="center")
    tree.column("PHoneNO", width=137,anchor="center")

    tree.grid(padx=9,pady=9,sticky="nsew")

        
    


def Patient():
    def bk_text(e):
        fname1_inut.delete(0,"end") 
    def bk1_text(e):
        age1_inut.delete(0,"end") 
    def bk2_text(e):
        number1_inut.delete(0,"end") 
    def bk3_text(e):
        problem1_inut.delete(0,"end") 

    def book():
        try:
            mysqldb=mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="Sonia1978",
                database="hospital")
            bookingid=random.randint(9999,99999)
            name=fname1_inut.get()
            age=age1_inut.get()
            number=number1_inut.get()
            problem=problem1_inut.get()
            room=combobox1.get() 
            gender=combobox.get()
            mycursor=mysqldb.cursor()
            ind="INSERT INTO booking (bookingid,name, age, phoneno, problem, gender, room) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            t=(bookingid,name,age,number,problem,room,gender)
            mycursor.execute(ind,t)
            mysqldb.commit(); 
            
            sql="SELECT bookingid,name, age, phoneno, problem, gender,room FROM booking WHERE bookingid= %s"
            tt=(bookingid)
            mycursor=mysqldb.cursor()
            mycursor.execute(sql,(tt,))
            result = mycursor.fetchall() 
            for item in result:
                tree2.insert("", "end", values=item)

        except mysql.connector.errors.IntegrityError:
            messagebox.showinfo('information',"Room Is already Book on this Patient")
        except:
            messagebox.showinfo('information',"PLZ Check All The Information And Fill Corectly")    



    patient_frame=Frame(root2,width=900,height=900,)
    patient_frame.place(x=140,y=0)

    check_lable=tb.Label(patient_frame,text="Book Room In Hospital",font=('verdina',40,'bold'))
    check_lable.config(background="gray14", foreground="orange2")
    check_lable.place(y=60,x=155)

    fname1_inut=Entry(patient_frame,width=25, borderwidth=10)
    fname1_inut.insert(0,'Full Name')
    fname1_inut.place(y=150,x=60)
    fname1_inut.bind("<FocusIn>",bk_text)

    age1_inut=Entry(patient_frame,width=25, borderwidth=10)
    age1_inut.insert(0,'Enter Your Age')
    age1_inut.place(y=150,x=400)
    age1_inut.bind("<FocusIn>",bk1_text)

    number1_inut=Entry(patient_frame,width=25, borderwidth=10)
    number1_inut.insert(0,'Enter Your PhoneNO')
    number1_inut.place(y=200,x=60)
    number1_inut.bind("<FocusIn>",bk2_text)

    problem1_inut=Entry(patient_frame,width=25, borderwidth=10)
    problem1_inut.insert(0,'Enter Your Problem')
    problem1_inut.place(y=200,x=400)
    problem1_inut.bind("<FocusIn>",bk3_text)

    options=['ICU','Deluxe','General','Children']
    combobox = tb.Combobox(patient_frame,state='readonly',value=options,width=25)
    combobox.set("Select The Room")
    combobox.place(y=250,x=400)

    options=["Male",'Femail','Rather Not Say']
    combobox1 = tb.Combobox(patient_frame,state='readonly',value=options,width=25)
    combobox1.set("Select Your Gender")
    combobox1.place(y=250,x=60)

    book_button=tb.Button(patient_frame,text='Confirm Booking',width=25,style='warning.outline-toolbutton.TButton',command=lambda:book())
    book_button.place(y=300,x=220)

    check_lable1=tb.Label(patient_frame,text="[ICU ₹1500/Day] | [Deluxe ₹1200/Day] | [General ₹1000/Day] | [Children 1500/Day]",font=('verdina',15,'bold'))
    check_lable1.config(background="gray14", foreground="orange2")
    check_lable1.place(y=360,x=80)

    info_frame2=Frame(patient_frame,width=2,height=2)
    info_frame2.config(bg='orange1')
    info_frame2.place(x=10,y=385)

    tree2 = tb.Treeview(info_frame2, columns=("BookingNo","Patient Name","Age","PhoneNo","Problem","Gender","Room Type"), show="headings")

    tree2.heading("BookingNo", text="BokkingNo")
    tree2.heading("Patient Name", text="Patient Name")
    tree2.heading("Age", text="Age")
    tree2.heading("PhoneNo", text="PhoneNo")
    tree2.heading("Problem", text="Problem")
    tree2.heading("Gender", text="Gender")
    tree2.heading("Room Type", text="Room Type")
    
    tree2.column("BookingNo", width=90,anchor="center")
    tree2.column("Patient Name", width=137,anchor="center")
    tree2.column("Age", width=50,anchor="center")
    tree2.column("PhoneNo", width=137,anchor="center")
    tree2.column("Problem", width=137,anchor="center")
    tree2.column("Gender", width=60,anchor="center")
    tree2.column("Room Type", width=110,anchor="center")

    tree2.grid(padx=5,pady=5)


def Appoint():
    def ap_text(e):
        fname_inut.delete(0,"end") 
    def ap1_text(e):
        age_inut.delete(0,"end") 
    def ap2_text(e):
        number_inut.delete(0,"end") 
    def ap3_text(e):
        mail_inut.delete(0,"end") 
    def ap4_text(e):
        synt_input.delete(0,"end")     
    
    def app():
        try:
            mysqldb=mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="Sonia1978",
                database="hospital")
            patientno=random.randint(99999,999999)
            name=fname_inut.get()
            age=age_inut.get()
            number=number_inut.get()
            mail=mail_inut.get() 
            appoint= appoint_input.entry.get()
            gender=combobox.get()
            Syntoms= synt_input.get()
            problem=combobox1.get()
            mycursor=mysqldb.cursor()
            ind="INSERT INTO appointment (patientid, name, age, number, mail, date, gender, syntoms, problem) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            t=(patientno,name,age,number,mail,appoint,gender,Syntoms,problem)
            mycursor.execute(ind,t)
            mysqldb.commit(); 
            
            sql="SELECT patientid,name,age,syntoms,problem,date FROM appointment WHERE name= %s"
            tt=(name)
            mycursor=mysqldb.cursor()
            mycursor.execute(sql,(tt,))
            result = mycursor.fetchall() 
            for item in result:
                tree1.insert("", "end", values=item)
        except mysql.connector.errors.IntegrityError:
            messagebox.showinfo('information',"Appointment is already fixed")
        except:
            messagebox.showinfo('information',"PLZ Check All The Information And Fill Corectly")
            


    appoint_frame=Frame(root2,width=900,height=900,)
    appoint_frame.place(x=140,y=0)

    app_lable=tb.Label(appoint_frame,text="Book an Appointment",font=('verdina',40,'bold'))
    app_lable.config(background="gray14", foreground="orange2")
    app_lable.place(y=60,x=155)
    
    fname_inut=Entry(appoint_frame,width=25, borderwidth=10)
    fname_inut.insert(0,'Full Name')
    fname_inut.place(y=150,x=60)
    fname_inut.bind("<FocusIn>",ap_text)

    age_inut=Entry(appoint_frame,width=25, borderwidth=10)
    age_inut.insert(0,'Enter Your Age')
    age_inut.place(y=150,x=400)
    age_inut.bind("<FocusIn>",ap1_text)

    number_inut=Entry(appoint_frame,width=25, borderwidth=10)
    number_inut.insert(0,'Enter Your PhoneNO')
    number_inut.place(y=200,x=60)
    number_inut.bind("<FocusIn>",ap2_text)

    mail_inut=Entry(appoint_frame,width=25, borderwidth=10)
    mail_inut.insert(0,'Enter Your Email')
    mail_inut.place(y=200,x=400)
    mail_inut.bind("<FocusIn>",ap3_text)

    appoint_input=tb.DateEntry(appoint_frame,width=23,dateformat='%d/%m/%Y')
    appoint_input.place(y=250,x=58)

    options=["Male",'Femail','Rather Not Say']
    combobox = tb.Combobox(appoint_frame,state='readonly',value=options,width=25)
    combobox.set("Select Your Gender")
    combobox.place(y=250,x=400)

    synt_input=Entry(appoint_frame,width=26, borderwidth=5)
    synt_input.insert(0,'Enter Your Syntoms')
    synt_input.place(y=290,x=60)
    synt_input.bind("<FocusIn>",ap4_text)
    

    options=['Cardiologist','Neurologist','Orthopedic Surgeon','Pediatrician','Dermatologist','Gastroenterologist','General Practitioner','Oncologist','Endocrinologist','Ophthalmologist']
    combobox1 = tb.Combobox(appoint_frame,state='readonly',value=options,width=25)
    combobox1.set("Select The Problem")
    combobox1.place(y=290,x=400)

    fixapoi_button=tb.Button(appoint_frame,text='Fix Appointment',width=25,style='warning.outline-toolbutton.TButton',command=lambda:app())
    fixapoi_button.place(y=340,x=220)


    info_frame1=Frame(appoint_frame,width=2,height=2)
    info_frame1.config(bg='orange1')
    info_frame1.place(x=30,y=385)

    tree1 = tb.Treeview(info_frame1, columns=("AppointmentNo","Patient Name","Age","Syomptom","Problem","Date of Appointment"), show="headings")

    tree1.heading("AppointmentNo", text="AppointmentNo")
    tree1.heading("Patient Name", text="Patient Name")
    tree1.heading("Age", text="Age")
    tree1.heading("Syomptom", text="Syomptom")
    tree1.heading("Problem", text="Problem")
    tree1.heading("Date of Appointment", text="Date of Appointment")
    
    tree1.column("AppointmentNo", width=90,anchor="center")
    tree1.column("Patient Name", width=137,anchor="center")
    tree1.column("Age", width=50,anchor="center")
    tree1.column("Syomptom", width=137,anchor="center")
    tree1.column("Problem", width=137,anchor="center")
    tree1.column("Date of Appointment", width=137,anchor="center")

    tree1.grid(padx=5,pady=5)
    

frame2 =tb.Frame(root2,width=130, height=900)  
frame2.grid(pady=(0,100),padx=(0,850))

side_frame=Frame(frame2,width=128,height=900)
side_frame.config(background='orange2')
side_frame.pack(padx=0,pady=0)  


image = Image.open('logo and images/b91e06b7-b913-4ca2-8225-713054908541.png')
resize_image1=image.resize((126,100),Image.Resampling.LANCZOS)
image=ImageTk.PhotoImage((resize_image1))
image_label=Label(side_frame,image=image)
image_label.place(x=0,y=0)

photohome=Image.open("logo and images/home.png")
resize_home=photohome.resize((100,85))
photohome1=ImageTk.PhotoImage(resize_home) 
home=tb.Button(text='SignUp', image = photohome1 ,style='warning-toolbutton',command=lambda:Homepage())
home.grid(row=0,column=0,pady=(0,650),padx=(0,850))

photodock=Image.open("logo and images/doctor.png")
resize_dock=photodock.resize((100,85))
photohome2=ImageTk.PhotoImage(resize_dock) 
dock=tb.Button(text='SignUp', image = photohome2 ,style='warning-toolbutton',command=lambda:Doctor())
dock.grid(row=0,column=0,pady=(0,430),padx=(0,850))

photopait=Image.open("logo and images/hospitalisation.png")
resize_pait=photopait.resize((100,85))
photohome3=ImageTk.PhotoImage(resize_pait) 
pait=tb.Button(text='SignUp', image = photohome3 ,style='warning-toolbutton',command=lambda:Patient())
pait.grid(row=0,column=0,pady=(0,210),padx=(0,850))

photoapoint=Image.open("logo and images/doctor-appointment.png")
resize_apoint=photoapoint.resize((100,85))
photohome4=ImageTk.PhotoImage(resize_apoint) 
apoint=tb.Button(text='SignUp', image = photohome4 ,style='warning-toolbutton',command=lambda:Appoint())
apoint.grid(row=0,column=0,pady=(10,0),padx=(0,850))

Homepage()
root2.mainloop()