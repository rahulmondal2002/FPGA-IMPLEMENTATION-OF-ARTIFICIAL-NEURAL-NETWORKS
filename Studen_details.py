
from os import path
from tkinter import*
import time
import os
import cv2
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox

import mysql.connector
from Camera_for_take_photo import Take
from Uplaoad_Photo_image_file_screen import upload_image
class student_list:
    
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1500x800+0+0")
        self.root.resizable(0,0)
        self.root.title("Student Details")
        self.root.iconbitmap('Image1/my.ico')
        img=Image.open("Image1/Visa Banner - Study.png")
        img=img.resize((500,130),Image.LANCZOS)
        self.imge=ImageTk.PhotoImage(img)

        lebel1=Label(self.root,image=self.imge)
        lebel1.place(x=0,y=0,width=500,height=130)
        # lebel1.pack()

        img1 = Image.open("Image1/Student-Well-Being_1410x820-705x410.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.imge1 = ImageTk.PhotoImage(img1)

        lebel2 = Label(self.root,image=self.imge1)
        lebel2.place(x=500, y=0, width=500, height=130)
        # lebel1.pack()


        img3 = Image.open("Image1/Students (1).jpg").convert('RGBA')
        img = img3.resize((500, 130), Image.LANCZOS)
        self.imge3 = ImageTk.PhotoImage(img)

        lebel3 = Label(self.root,image=self.imge3)
        lebel3.place(x=1000, y=0, width=500, height=130)
        # lebel1.pack()
    

        bg_img = Image.open("Image1/facial-recognition-software-image.jpg")
        bg_img = bg_img.resize((1500, 670), Image.LANCZOS)
        self.bg_imge = ImageTk.PhotoImage(bg_img)

        bg_lebel1 = Label(self.root,image=self.bg_imge)
        bg_lebel1.place(x=0, y=130, width=1500, height=670)
        # lebel1.pack()

        txt_lab = Label(bg_lebel1, text="Student Details", font=("Comic Sans MS", 29 ,"bold"),bg="white", fg="blue", borderwidth=0)
        txt_lab.place(x=0, y=1,width=1500,height=43)

        #variables
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_SID=StringVar()
        self.var_SName=StringVar()
        self.var_div=StringVar()
        self.var_roll_no=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_Email=StringVar()
        self.var_phone_no=StringVar()
        self.var_Address=StringVar()
        self.var_parents=StringVar()
        
        
        #database creation----------------------------------
        try:
            
            db = mysql.connector.connect(user='root', password='pass0808', host='localhost', port=3306)
            cdb = db.cursor()

            # Check if the database exists
            cdb.execute("SHOW DATABASES LIKE 'student_data'")
            db_exists = cdb.fetchone()

            if not db_exists:
                # Create the database if it doesn't exist
                cdb.execute("CREATE DATABASE student_data")

            # Use the database
            cdb.execute("USE student_data")

            # Check if the table exists
            cdb.execute("SHOW TABLES LIKE 'data1'")
            table_exists = cdb.fetchone()

            if not table_exists:
                # Create the table if it doesn't exist
                cdb.execute('''CREATE TABLE data1 (
                                ID INT,
                                Dept VARCHAR(20),
                                SID INT,
                                SName VARCHAR(50),
                                Roll_No BIGINT(16) NOT NULL,
                                Course VARCHAR(50),
                                Year VARCHAR(50),
                                Sem VARCHAR(50),
                                Divi VARCHAR(50),
                                Phone_No BIGINT(12) NOT NULL,
                                Email VARCHAR(50),
                                Gender VARCHAR(50),
                                DOB VARCHAR(50),
                                Address VARCHAR(50),
                                Gurdean VARCHAR(50),
                                Photo VARCHAR(50)
                                )''')

            db.commit()
            db.close()

            self.massge = Message(self.msg, text="Submit Successfuly!", font=("Comic Sans MS", 12, 'bold', "italic"),
                                fg='green', bg='#99FF99', width=280)

            self.massge.place(x=4, y=4, width=285, height=30)

        except Exception as e:
            print("Error while connecting to MySQL", e)


        m_frame=Frame(bg_lebel1)
        m_frame.place(x=10,y=49,width=1480,height=670)

        #left frame
        l_frame=LabelFrame(m_frame,text="Information form",bg="white",fg='green',border=1)
        l_frame.place(x=10,y=5,width=650,height=650)

        l_f_img = Image.open("Image1/student2.jpg").convert('RGBA')
        img =l_f_img.resize((645, 130), Image.LANCZOS)
        self.l_f_img = ImageTk.PhotoImage(l_f_img)

        ll_f_img = Label(l_frame,image=self.l_f_img,border='0')
        ll_f_img.place(x=2, y=0, width=643, height=130)

        #cours
        left_cours_frame = LabelFrame(l_frame, text="Our courses", bg="white", fg='green', border=1)
        left_cours_frame.place(x=2, y=133, width=643, height=90)

        dept_leb=Label(left_cours_frame,text="Department : ",font=("Comic Sans MS", 10, "bold"),bg="white")
        dept_leb.grid(row=0,column=0,padx=6,pady=6,sticky=W)
        self.dept_combo= ttk.Combobox(left_cours_frame,textvariable=self.var_dep,width=30,height=25,state='readonly')
        self.dept_combo['value']=("Select","Computer Science Techonology","Civil","Machanical","Electrical","Electronics","IT","farmecy",'Others')
        self.dept_combo.current(0)
        self.dept_combo.grid(row=0,column=1,padx=12,pady=6,sticky=W)

        course_leb=Label(left_cours_frame,text="Courses : ",font=("Comic Sans MS", 10, "bold"),bg="white")
        course_leb.grid(row=0,column=2,padx=6,pady=6,sticky=W)
        self.course_combo= ttk.Combobox(left_cours_frame,textvariable=self.var_course,width=30,height=25,state='readonly')
        self.course_combo['value']=("Select","Regular","Job Candirate")
        self.course_combo.current(0)
        self.course_combo.grid(row=0,column=3,padx=3,pady=6,sticky=W)

        Year_leb=Label(left_cours_frame,text="Years : ",font=("Comic Sans MS", 10, "bold"),bg="white")
        Year_leb.grid(row=1,column=0,padx=6,pady=6,sticky=W)
        self.Year_combo= ttk.Combobox(left_cours_frame,textvariable=self.var_year,width=30,height=25,state='readonly')
        self.Year_combo['value']=("Select Years",'2018-22','2019-23','2020-24','2021-25','2022-26','2023-27')
        self.Year_combo.current(0)
        self.Year_combo.grid(row=1,column=1,padx=10,pady=6,sticky=W)

        sem_leb=Label(left_cours_frame,text="Semester : ",font=("Comic Sans MS", 10, "bold"),bg="white")
        sem_leb.grid(row=1,column=2,padx=6,pady=6,sticky=W)
        self.sem_combo= ttk.Combobox(left_cours_frame,textvariable=self.var_sem,width=30,height=25,state='readonly')
        self.sem_combo['value']=("Select Semester","1st",'2nd','3rd','4th','5th','6th','7th','8th')
        self.sem_combo.current(0)
        self.sem_combo.grid(row=1,column=3,padx=6,pady=6,sticky=W)

        #class details
        left_class_frame = LabelFrame(l_frame, text="Student Class Informaiton", bg="white", fg='green', border=1)
        left_class_frame.place(x=2, y=223, width=643, height=240)

        studentID_leb = Label(left_class_frame, text="Student ID : ", font=("Arial", 10, "bold"), bg="white")
        studentID_leb.grid(row=0, column=0, padx=6, pady=6, sticky=W)
        self.sID_entry = Entry(left_class_frame,textvariable=self.var_SID,font=("Arial", 10),highlightthickness=1, bg="white",width=25)
        self.sID_entry.grid(row=0, column=1, padx=5, pady=6, sticky=W)
        # self.sID_entry.insert(0,'000000')

        classDivision_leb = Label(left_class_frame, text="Class Division : ", font=("Arial", 10, "bold"), bg="white")
        classDivision_leb.grid(row=0, column=2, padx=6, pady=6, sticky=W)
        self.sDivision_combo = ttk.Combobox(left_class_frame, textvariable=self.var_div,width=25, height=25, state='readonly')
        self.sDivision_combo['value'] = ("Select", "A", 'B', 'C')
        self.sDivision_combo.current(0)
        self.sDivision_combo.grid(row=0, column=3, padx=5, pady=6, sticky=W)


        student_name_leb = Label(left_class_frame, text="Student Name : ", font=("Arial", 10, "bold"),bg="white")
        student_name_leb.grid(row=1, column=0, padx=6, pady=6, sticky=W)
        self.sName_entry = Entry(left_class_frame,textvariable=self.var_SName, font=("Arial", 10),highlightthickness=1, bg="white", width=25)
        self.sName_entry.grid(row=1, column=1, padx=5, pady=6, sticky=W)

        student_Roll_leb = Label(left_class_frame, text="Roll No : ", font=("Arial", 10, "bold"), bg="white")
        student_Roll_leb.grid(row=1, column=2, padx=6, pady=6, sticky=W)
        self.sRoll_entry = Entry(left_class_frame,textvariable=self.var_roll_no,font=("Arial", 10),highlightthickness=1, bg="white",width=25)
        self.sRoll_entry.grid(row=1, column=3, padx=5, pady=6, sticky=W)

        studentSex_leb = Label(left_class_frame, text="Gender : ", font=("Arial", 10, "bold"), bg="white")
        studentSex_leb.grid(row=2, column=0, padx=6, pady=6, sticky=W)
        self.sGender_combo = ttk.Combobox(left_class_frame, textvariable=self.var_gender,width=25, height=25, state='readonly')
        self.sGender_combo['value'] = ("Select", "Male", 'Female', 'Others')
        self.sGender_combo.current(0)
        self.sGender_combo.grid(row=2, column=1, padx=5, pady=6, sticky=W)


        student_Dob_leb = Label(left_class_frame, text="DOB : ", font=("Arial", 10, "bold"), bg="white")
        student_Dob_leb.grid(row=2, column=2, padx=6, pady=6, sticky=W)
        self.sDob_entry = Entry(left_class_frame,textvariable=self.var_dob,font=("Arial", 10), highlightthickness=1,bg="white",width=25)
        self.sDob_entry.grid(row=2, column=3, padx=5, pady=6, sticky=W)

        studentEmail_leb = Label(left_class_frame, text="Email ID : ", font=("Arial", 10, "bold"), bg="white")
        studentEmail_leb.grid(row=3, column=0, padx=6, pady=6, sticky=W)
        self.sEmail_entry = Entry(left_class_frame,textvariable=self.var_Email,font=("Arial", 10),highlightthickness=1, bg="white",width=25)
        self.sEmail_entry.grid(row=3, column=1, padx=5, pady=6, sticky=W)

        student_PhoneNo_leb = Label(left_class_frame, text="Phone No. : ", font=("Arial", 10, "bold"), bg="white")
        student_PhoneNo_leb.grid(row=3, column=2, padx=6, pady=6, sticky=W)
        self.sPhoneNo_entry = Entry(left_class_frame,textvariable=self.var_phone_no,font=("Arial", 10),highlightthickness=1, bg="white",width=25)
        self.sPhoneNo_entry.grid(row=3, column=3, padx=5, pady=6, sticky=W)

        studentAddress_leb = Label(left_class_frame, text="Address : ", font=("Arial", 10, "bold"), bg="white")
        studentAddress_leb.grid(row=4, column=0, padx=6, pady=6, sticky=W)
        self.sAddress_entry = Entry(left_class_frame,textvariable=self.var_Address,font=("Arial", 10),highlightthickness=1, bg="white",width=25)
        self.sAddress_entry.grid(row=4, column=1, padx=5, pady=6, sticky=W)

        student_Parents_leb = Label(left_class_frame, text="Parents : ", font=("Arial", 10, "bold"), bg="white")
        student_Parents_leb.grid(row=4, column=2, padx=6, pady=6, sticky=W)
        self.sParents_entry = Entry(left_class_frame,textvariable=self.var_parents,font=("Arial", 10), highlightthickness=1,bg="white",width=25)
        self.sParents_entry.grid(row=4, column=3, padx=5, pady=6, sticky=W)

        self.var_radeio1=StringVar()
        take_photo=ttk.Radiobutton(left_class_frame,text="Take Photo Sample",variable=self.var_radeio1,value="CamPhoto",).grid(row=5, column=0, padx=6, pady=6, sticky=W)
        
        NO_photo=ttk.Radiobutton(left_class_frame,text="Upload Photo Sample",variable=self.var_radeio1,value="UploadPhoto").grid(row=5, column=1, padx=6, pady=6, sticky=W)
        
        self.msg=Label(left_class_frame,border='0',bg='white')
        self.msg.place(x=280, y=180, width=300, height=40)
        # if (self.massge=='.!label4.!frame.!labelframe.!labelframe2.!label11.!message'):
        #     time.sleep(5)
        #     self.massge.destroy()

        #botton
        btn_frame = LabelFrame(l_frame, bg="white", fg='green', border=1)
        btn_frame.place(x=2, y=470, width=643, height=90)
        btn_Save = Button(btn_frame, text="Save",command=self.submit, cursor="hand2", font=("Comic Sans MS", 12, "bold"),
                       borderwidth="0",fg="red",bg="yellow")
        btn_Save.place(x=2, y=1, width=157, height=40)

        btn_Update = Button(btn_frame, text="Update", cursor="hand2", command=self.update,font=("Comic Sans MS", 12, "bold"),
                       borderwidth="0",fg="red",bg="yellow")
        btn_Update.place(x=161, y=1, width=158, height=40)

        btn_delete = Button(btn_frame, text="Delete", cursor="hand2", command=self.delet,font=("Comic Sans MS", 12, "bold"),
                       borderwidth="0",fg="red",bg="yellow")
        btn_delete.place(x=321, y=1, width=158, height=40)

        btn_Reset = Button(btn_frame, text='Reset', cursor="hand2", command=self.rest,font=("Comic Sans MS", 12, "bold"),
                       borderwidth="0",fg="red",bg="yellow")
        btn_Reset.place(x=481, y=1, width=158, height=40)

        # btn_Photo_take = Button(btn_frame, text='Take photo Sample', cursor="hand2", font=("Comic Sans MS", 12, "bold"),
        #                borderwidth="0",fg="red",bg="yellow")
        # btn_Photo_take.place(x=2, y=44, width=318, height=40)

        # btn_Update_photo = Button(btn_frame, text='Update Photo Sample', cursor="hand2", font=("Comic Sans MS", 12, "bold"),
        #                borderwidth="0",fg="red",bg="yellow")
        # btn_Update_photo.place(x=323, y=44, width=317, height=40)
#```````````````````````````````````````````````````````````````````````````````````````````````````````````
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #right frame
        r_frame=LabelFrame(m_frame,text="Student Information",bg="white",fg='green',border=1)
        r_frame.place(x=670,y=5,width=800,height=650)

        #search box
        serch_frame=LabelFrame(r_frame,border=1)
        serch_frame.place(x=3,y=2,width=560,height=40)

        search_leb = Label(serch_frame, text="Search by : ", font=("Arial", 10, "bold"), bg="white")
        search_leb.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.search_combo = ttk.Combobox(serch_frame, width=10, height=25, state='readonly')
        self.search_combo['value'] = ("Select", "Student ID", 'Roll No.', 'Phone No.')
        self.search_combo.current(0)
        self.search_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        self.search_entry = Entry(serch_frame, font=("Arial", 10, "bold"), bg="white", width=25)
        self.search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        btn_search = Button(serch_frame, text='Search', command=self.Searching,cursor="hand2",
                                  font=("Arial", 12, "bold"),
                                  borderwidth="0", fg="white", bg="green").grid(row=0,column=3,padx=5,pady=5)
        btn_search = Button(serch_frame, text='Refresh', command=self.rest,cursor="hand2",
                                  font=("Arial", 12, "bold"),
                                  borderwidth="0", fg="white", bg="#3374F7").grid(row=0,column=4,padx=5,pady=5)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #student table
        table_frame=Frame(r_frame,border=1)
        table_frame.place(x=3,y=50,width=560,height=630)

        t_lable_frame=LabelFrame(table_frame,border=1,bg="white")
        t_lable_frame.place(x=2,y=2,width=558,height=500)

        xscroll_bar = ttk.Scrollbar(t_lable_frame,orient=HORIZONTAL)
        yscroll_bar=ttk.Scrollbar(t_lable_frame,orient=VERTICAL)


        self.student_table=ttk.Treeview(t_lable_frame,column=('ID','Dept','SID','SName','Roll No.', 'Course','Year','Sem','Div',
                                                       'Phone No.','Email','Gender','DOB','Address',
                                                       'Gurdean','Photo'),xscrollcommand=xscroll_bar.set,yscrollcommand=yscroll_bar.set)
        xscroll_bar.pack(side=BOTTOM, fill=X)
        yscroll_bar.pack(side=RIGHT, fill=Y)
        xscroll_bar.config(command=self.student_table.xview)
        yscroll_bar.config(command=self.student_table.yview)

        #selt column widht___________________________________________
        self.student_table.column('ID',anchor=CENTER, width=50)
        self.student_table.column('Dept',anchor=CENTER, width=180)

        self.student_table.column('SID', anchor=CENTER,width=150)
        self.student_table.column('SName',anchor=CENTER, width=150)
        self.student_table.column('Roll No.',anchor=CENTER, width=150)
        self.student_table.column('Course',anchor=CENTER, width=150)
        self.student_table.column('Year',anchor=CENTER, width=150)
        self.student_table.column('Sem',anchor=CENTER, width=150)
        self.student_table.column('Div',anchor=CENTER, width=150)
        self.student_table.column('Phone No.',anchor=CENTER, width=150)
        self.student_table.column('Email',anchor=CENTER, width=150)
        self.student_table.column('Gender', anchor=CENTER,width=150)
        self.student_table.column('DOB', anchor=CENTER,width=150)
        self.student_table.column('Address',anchor=CENTER, width=150)
        self.student_table.column('Gurdean',anchor=CENTER, width=150)
        self.student_table.column('Photo', anchor=CENTER,width=150)
        # set column heading________________________________________
        self.student_table.heading('ID',text='ID',anchor=CENTER)
        self.student_table.heading('Dept',text='Department',anchor=CENTER)
        self.student_table.heading('SID',text='Student ID',anchor=CENTER)
        self.student_table.heading('SName',text='Student Name',anchor=CENTER)
        self.student_table.heading('Roll No.',text='Roll No.',anchor=CENTER)
        self.student_table.heading('Course',text='Courses',anchor=CENTER)
        self.student_table.heading('Year',text='Years',anchor=CENTER)
        self.student_table.heading('Sem',text='Semister',anchor=CENTER)
        self.student_table.heading('Div',text='Division',anchor=CENTER)
        self.student_table.heading('Phone No.',text='Phone No.',anchor=CENTER)
        self.student_table.heading('Email',text='Email ID',anchor=CENTER)
        self.student_table.heading('Gender',text='Gender',anchor=CENTER)
        self.student_table.heading('DOB',text='DOB',anchor=CENTER)
        self.student_table.heading('Address',text='Address',anchor=CENTER)
        self.student_table.heading('Gurdean',text='Gurdean',anchor=CENTER)
        self.student_table.heading('Photo',text='Photo sample',anchor=CENTER)
        self.student_table['show']='headings'
        self.student_table.bind('<ButtonRelease>',self.mouse_click)

        self.student_table.pack(fill=BOTH,expand=1)
        self.view()
        #display fram
        display_frame=Frame(r_frame,border=1)
        display_frame.place(x=570, y=2, width=220, height=630)

        self.photo_label=LabelFrame(display_frame,text="Photo", font=("Comic Sans MS", 10, "bold"),fg='red',bg='white')
        self.photo_label.place(x=2,y=2,width=210,height=230)
        imgpk=Image.open("Image1/No-Image.png")
        imgpk=imgpk.resize((205,220),Image.LANCZOS)
        self.imo=ImageTk.PhotoImage(imgpk)

        self.pl=Label(self.photo_label,image=self.imo)
        self.pl.place(x=2,y=1,width=200,height=220)



        btn_exit= Button(display_frame, text='Exit',command=self.root.destroy, cursor="hand2",
                                  font=("Comic Sans MS", 12, "bold"),
                                  borderwidth="0", fg="white", bg="red")
        btn_exit.place(x=5, y=500, width=200, height=40)
    #submit botton
    def submit(self):
        if (self.dept_combo.get()=='Select' or
                    self.sID_entry.get()== '' or
                    self.sName_entry.get()== '' or
                    self.sRoll_entry.get()== '' or
                    self.course_combo.get()== '' or
                    self.Year_combo.get()== 'Select Years' or
                    self.sem_combo.get()== 'Select Semister' or
                    self.sDivision_combo.get()== 'Select' or
                    self.sPhoneNo_entry.get()== '' or
                    self.sEmail_entry.get()== '' or
                    self.sGender_combo.get()== 'Select' or
                    self.sDob_entry.get()== '' or
                    self.sAddress_entry.get()== '' or
                    self.sParents_entry.get()==''):

                    self.sID_entry.config(highlightbackground = "red", highlightcolor= "red")
                    self.sID_entry.grid(row=0, column=1)
                    
                    self.sName_entry.config(highlightbackground = "red", highlightcolor= "red")
                    self.sName_entry.grid(row=1, column=1)
                    self.sRoll_entry.config(highlightbackground = "red", highlightcolor= "red")
                    self.sRoll_entry.grid(row=1, column=3)
                    self.sDob_entry.config(highlightbackground = "red", highlightcolor= "red")
                    self.sDob_entry.grid(row=2, column=3)
                    self.sEmail_entry.config(highlightbackground = "red", highlightcolor= "red")
                    self.sEmail_entry.grid(row=3, column=1)
                    self.sPhoneNo_entry.config(highlightbackground = "red", highlightcolor= "red")
                    self.sPhoneNo_entry.grid(row=3, column=3)
                    self.sAddress_entry.config(highlightbackground = "red", highlightcolor= "red")
                    self.sAddress_entry.grid(row=4, column=1)
                    self.sParents_entry.config(highlightbackground = "red", highlightcolor= "red")
                    self.sParents_entry.grid(row=4, column=3)
                    messagebox.showerror('Blank Entry',"All Entry requird to fill",parent=self.root)


                    self.root.after(2000,
                    self.sID_entry.config(highlightbackground = "#A0A0A0", highlightcolor= "#A0A0A0"),
                    self.sParents_entry.config(highlightbackground = "#A0A0A0", highlightcolor= "#A0A0A0"),
                    self.sName_entry.config(highlightbackground = "#A0A0A0", highlightcolor= "#A0A0A0"),
                    self.sRoll_entry.config(highlightbackground = "#A0A0A0", highlightcolor= "#A0A0A0"),
                    self.sDob_entry.config(highlightbackground = "#A0A0A0", highlightcolor= "#A0A0A0"),
                    self.sEmail_entry.config(highlightbackground = "#A0A0A0", highlightcolor= "#A0A0A0"),
                    self.sPhoneNo_entry.config(highlightbackground = "#A0A0A0", highlightcolor= "#A0A0A0"),
                    self.sAddress_entry.config(highlightbackground = "#A0A0A0", highlightcolor= "#A0A0A0"),
                   )
                    
        elif ( self.sName_entry.get().endswith('.')):
                    self.sName_entry.config(highlightbackground = "red", highlightcolor= "red")
                    self.sName_entry.grid(row=1, column=1)
                    messagebox.showerror('Blank Entry',"All Entry requird to fill",parent=self.root)
                    self.root.after(2000,self.sName_entry.config(highlightbackground = "#A0A0A0", highlightcolor= "#A0A0A0"))
        else:
    # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  CAMERA SYSTME >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            if self.var_radeio1.get().lower()=='camphoto':
                newindow=Toplevel(self.root)
                self.data=Take(newindow, 'student',self.sID_entry.get())
            else:
                newindow=Toplevel(self.root)
                self.data=upload_image(newindow, 'student',self.sID_entry.get())

        #    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<</


            try:

                SUBMIT_data=messagebox.askyesno("Submit","Are you sure 'SUBMIT' data ?",parent=self.root)
                if SUBMIT_data>0:    


                    db = mysql.connector.connect(user='root', password='pass0808', host='localhost', port=3306)
                    cdb = db.cursor()
                    # cdb.execute("create database student_data")
                    cdb.execute("use student_data")
                    # # cdb.execute('create table data1(Dept varchar(20)  , SID int , SName varchar(20)  , Roll_No int ,  Course varchar(20)  , Year int , Sem  varchar(20) , Divi varchar(20)  ,Phone_No bigint(12) not null , Email varchar(20)  , Gender  varchar(20)  , DOB  varchar(20)  , Address  varchar(30) ,Gurdean varchar(20)  , Photo varchar(20)  )' )
                    # # cdb.execute("insert into data1(SName,Phone_No) values('babo',58465479876)")
                    #
                    # cdb.execute("select * from data1")
                    # result = cdb.fetchall()
                    #
                    # for i in result:
                    #     print(i)
                    # cdb.execute('insert into data1() values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                    cdb.execute("INSERT INTO data1 (Dept, SID, SName, Roll_No, Course, Year, Sem, Divi, Phone_No, Email, Gender, DOB, Address, Gurdean,Photo) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(                                                       
                                                                                  self.dept_combo.get(),
                                                                                  self.sID_entry.get(),
                                                                                  self.sName_entry.get(),
                                                                                  self.sRoll_entry.get(),
                                                                                  self.course_combo.get(),
                                                                                  self.Year_combo.get(),
                                                                                  self.sem_combo.get(),
                                                                                  self.sDivision_combo.get(),
                                                                                  self.sPhoneNo_entry.get(),
                                                                                  self.sEmail_entry.get(),
                                                                                  self.sGender_combo.get(),
                                                                                  self.sDob_entry.get(),
                                                                                  self.sAddress_entry.get(),
                                                                                  self.sParents_entry.get(),
                                                                                  self.var_radeio1.get()

                    #                                                             # self.var_dep.get(),
                    #                                                             # self.var_SID.get(),
                    #                                                             # self.var_SName.get(),
                    #                                                             # self.var_roll_no.get(),
                    #                                                             # self.var_course.get(),
                    #                                                             # self.var_year.get(),
                    #                                                             # self.var_sem.get(),
                    #                                                             # self.var_div.get(),
                    #                                                             # self.var_phone_no.get(),
                    #                                                             # self.var_Email.get(),
                    #                                                             # self.var_gender.get(),
                    #                                                             # self.var_dob.get(),
                    #                                                             # self.var_Address.get(),
                    #                                                             # self.var_parents.get()
                     ))
                    db.commit()
                    db.close()
                    self.massge=Message(self.msg,text = "Submit Successfuly!", font=("Comic Sans MS", 12,'bold' ,"italic"),fg='green',bg='#99FF99',width=280)
                    
                    self.massge.place(x=4,y=4,width=285,height=30)
                    
                    self.rest()
                    
                    self.view()

                    self.root.after(2000, self.massge.destroy)#I Love This LINE-------------------------------------------->
                    
            except Exception as e:
                    messagebox.showinfo("Error",f'{str(e)} ',parent=self.root)

# <0000000000000000000000 veiw the data base entery 00000000000000000000000000000000
    def view(self):
        db = mysql.connector.connect(user='root', password='pass0808', host='localhost', port=3306)
        cdb = db.cursor()

        cdb.execute("use student_data")
        

        cdb.execute(' select ID,Dept, SID, SName, Roll_No, Course, Year, Sem, Divi, Phone_No, Email, Gender, DOB, Address, Gurdean,Photo from data1')
        result=cdb.fetchall()
        if len(result) !=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in result:
                self.student_table.insert('',END,values=i)

        db.close()
#~~~~~~~~~~~~~~~~~~~~SEARCHING~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    def Searching(self):
        db = mysql.connector.connect(user='root', password='pass0808', host='localhost', port=3306)
        cdb = db.cursor()

        cdb.execute("use student_data")
        # /"Select", "Student ID", 'Roll No.', 'Phone No.'
        # print(self.search_entry.get())
        
        if (('Student ID' == self.search_combo.get())&(len(self.search_entry.get()) !=0)):
            print
            cdb.execute(f"select * from data1 where  SID = {self.search_entry.get()}")
            result=cdb.fetchall()
        
        elif (('Roll No.' == self.search_combo.get())&(len(self.search_entry.get()) !=0)):
            cdb.execute(f"select * from data1 where  Roll_No = {self.search_entry.get()}")
            result=cdb.fetchall()
        
        elif (('Phone No.' == self.search_combo.get())&(len(self.search_entry.get()) !=0)):
            cdb.execute(f"select * from data1 where  Phone_No = {self.search_entry.get()}")
            result=cdb.fetchall()
        
        else:
            cdb.execute(' select * from data1')
            self.search_entry.delete(0,END)
            result=cdb.fetchall()
        
        if len(result) !=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in result:
                self.student_table.insert('',END,values=i)
        db.close()
#<------------------------------mouse click------------------->
    def mouse_click(self,even):
        st=self.student_table.focus()
        mk=self.student_table.item(st)
        ls=mk['values']
        # print(ls)
        if len(ls)!=0:
            self.dept_combo.set(ls[1])
            self.var_SID.set(ls[2])
            self.var_SName.set(ls[3])
            self.var_roll_no.set(ls[4])
            self.course_combo.set(ls[5])
            self.Year_combo.set(ls[6])
            self.sem_combo.set(ls[7])
            self.var_div.set(ls[8])
            self.var_phone_no.set(ls[9])
            self.var_Email.set(ls[10])
            self.sGender_combo.set(ls[11])
            self.var_dob.set(ls[12])
            self.var_Address.set(ls[13])
            self.var_parents.set(ls[14])
            self.var_radeio1.set(ls[15])
            
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~ Image~~~~~~~~~~~~~~~~~~~~~~~~ 
            path=os.getcwd()+"\\ImagesAttendance\\StudentPhotos\\"

            myList = os.listdir(path)
            # print(myList)
            k=True
            for cu_i in myList:
                if str(ls[2]) in cu_i:
                    img=Image.open(f"{path}/{cu_i}")
                    img=img.resize((205,220),Image.LANCZOS)
                    self.imo=ImageTk.PhotoImage(img)

                    self.pl=Label(self.photo_label,image=self.imo)
                    self.pl.place(x=2,y=1,width=200,height=220)
                    k=False
                # else:
            if k:
                imgpk=Image.open("Image1/No-Image.png")
                imgpk=imgpk.resize((205,220),Image.LANCZOS)
                self.imo=ImageTk.PhotoImage(imgpk)

                self.pl=Label(self.photo_label,image=self.imo)
                self.pl.place(x=2,y=1,width=200,height=220)

#---------------------------update button------------------------------------->
    def update(self):
        if (self.dept_combo.get()=='Select' or
                    self.sID_entry.get()== '' or
                    self.sName_entry.get()== '' or
                    self.sRoll_entry.get()== '' or
                    self.course_combo.get()== '' or
                    self.Year_combo.get()== 'Select Years' or
                    self.sem_combo.get()== 'Select Semister' or
                    self.sDivision_combo.get()== 'Select' or
                    self.sPhoneNo_entry.get()== '' or
                    self.sEmail_entry.get()== '' or
                    self.sGender_combo.get()== 'Select' or
                    self.sDob_entry.get()== '' or
                    self.sAddress_entry.get()== '' or
                    self.sParents_entry.get()==''):

                    self.sID_entry.config(highlightbackground = "red", highlightcolor= "red")
                    self.sID_entry.grid(row=0, column=1)
                    self.sName_entry.config(highlightbackground = "red", highlightcolor= "red")
                    self.sName_entry.grid(row=1, column=1)
                    self.sRoll_entry.config(highlightbackground = "red", highlightcolor= "red")
                    self.sRoll_entry.grid(row=1, column=3)
                    self.sDob_entry.config(highlightbackground = "red", highlightcolor= "red")
                    self.sDob_entry.grid(row=2, column=3)
                    self.sEmail_entry.config(highlightbackground = "red", highlightcolor= "red")
                    self.sEmail_entry.grid(row=3, column=1)
                    self.sPhoneNo_entry.config(highlightbackground = "red", highlightcolor= "red")
                    self.sPhoneNo_entry.grid(row=3, column=3)
                    self.sAddress_entry.config(highlightbackground = "red", highlightcolor= "red")
                    self.sAddress_entry.grid(row=4, column=1)
                    self.sParents_entry.config(highlightbackground = "red", highlightcolor= "red")
                    self.sParents_entry.grid(row=4, column=3)
                    messagebox.showerror('Blank Entry',"All Entry requird to fill",parent=self.root)


                    self.root.after(2000,
                    self.sID_entry.config(highlightbackground = "#A0A0A0", highlightcolor= "#A0A0A0"),
                    self.sParents_entry.config(highlightbackground = "#A0A0A0", highlightcolor= "#A0A0A0"),
                    self.sName_entry.config(highlightbackground = "#A0A0A0", highlightcolor= "#A0A0A0"),
                    self.sRoll_entry.config(highlightbackground = "#A0A0A0", highlightcolor= "#A0A0A0"),
                    self.sDob_entry.config(highlightbackground = "#A0A0A0", highlightcolor= "#A0A0A0"),
                    self.sEmail_entry.config(highlightbackground = "#A0A0A0", highlightcolor= "#A0A0A0"),
                    self.sPhoneNo_entry.config(highlightbackground = "#A0A0A0", highlightcolor= "#A0A0A0"),
                    self.sAddress_entry.config(highlightbackground = "#A0A0A0", highlightcolor= "#A0A0A0"),
                   )
                    
        elif ( self.sName_entry.get().endswith('.')):
                    self.sName_entry.config(highlightbackground = "red", highlightcolor= "red")
                    self.sName_entry.grid(row=1, column=1)
                    messagebox.showerror('Blank Entry',"Student Name Should not end with Dots ['.'] ",parent=self.root)
                    self.root.after(2000,self.sName_entry.config(highlightbackground = "#A0A0A0", highlightcolor= "#A0A0A0"))
        else:
           
            # <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  CAMERA SYSTME >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
            if self.var_radeio1.get().lower()=='camphoto':
                newindow=Toplevel(self.root)
                self.data=Take(newindow, 'student',self.sID_entry.get())
            else:
                newindow=Toplevel(self.root)
                self.data=upload_image(newindow, 'student',self.sID_entry.get())

            #    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<</
            try:
                update_data=messagebox.askyesno("Update","Are you sure 'UPDATE' data ?",parent=self.root)
                if update_data>0:
                    db = mysql.connector.connect(user='root', password='pass0808', host='localhost', port=3306)
                    cdb = db.cursor()
                    cdb.execute("use student_data")
                    cdb.execute("update data1 set Dept = %s, SID = %s, SName = %s, Roll_No = %s, Course = %s, Year = %s, Sem = %s, Divi = %s, Phone_No = %s, Email = %s, Gender = %s, DOB = %s, Address = %s, Gurdean = %s,Photo = %s where  SID = %s",(                                                       
                                                                                  self.dept_combo.get(),
                                                                                  self.sID_entry.get(),
                                                                                  self.sName_entry.get(),
                                                                                  self.sRoll_entry.get(),
                                                                                  self.course_combo.get(),
                                                                                  self.Year_combo.get(),
                                                                                  self.sem_combo.get(),
                                                                                  self.sDivision_combo.get(),
                                                                                  self.sPhoneNo_entry.get(),
                                                                                  self.sEmail_entry.get(),
                                                                                  self.sGender_combo.get(),
                                                                                  self.sDob_entry.get(),
                                                                                  self.sAddress_entry.get(),
                                                                                  self.sParents_entry.get(),
                                                                                  self.var_radeio1.get(),
                                                                                  self.sID_entry.get()

                      ))
                    db.commit()
                    db.close()
                    self.massge=Message(self.msg,text = "Update Successfuly!", font=("Comic Sans MS", 12,'bold' ,"italic"),fg='#FF7A04',bg='#FFCC99',width=280)
                    
                    self.massge.place(x=4,y=4,width=285,height=30)
                    
                    self.view()
                    self.rest()
                    

                    self.root.after(2000, self.massge.destroy)#I Love This LINE-------------------------------------------->
                    
            except Exception as e:
                    messagebox.showinfo("Error",f':{str(e)} ',parent=self.root)

#--------------------------------------Delete Data------------------------------------------------------>
    def delet(self):
        if (self.sID_entry.get()== '' ):

                    self.sID_entry.config(highlightbackground = "red", highlightcolor= "red")
                    self.sID_entry.grid(row=0, column=1)
                    messagebox.showerror('Blank Entry',"Studen ID requird to fill",parent=self.root)


                    self.root.after(2000,
                    self.sID_entry.config(highlightbackground = "#A0A0A0", highlightcolor= "#A0A0A0") )
        else:
           
            try:
                delete_data=messagebox.askyesno("Delete",'Are you sure to "DELETE DATA" ?',parent=self.root)
                if delete_data>0:
                    db = mysql.connector.connect(user='root', password='pass0808', host='localhost', port=3306)
                    cdb = db.cursor()
                    cdb.execute("use student_data")
                    cdb.execute(f"delete from data1 where SID = {self.sID_entry.get()}")
                    db.commit()
                    db.close()
                    sample_no=1
                    while sample_no<=75:
                        pat = 'ImagesAttendance/StudentPhotos/SampleOfPhoto/{}.{}.{}.jpg'.format('student',self.sID_entry.get(),sample_no)
                        if os.path.exists(pat):
                                 os.remove(pat)
                        # else:
                        #      print("The file does not exist") 
                        sample_no+=1
                    pa = 'ImagesAttendance/StudentPhotos/{}.{}.jpg'.format('student',self.sID_entry.get())
                    if os.path.exists(pa):
                            os.remove(pa)
                    self.massge=Message(self.msg,text = "Dlete Successfuly!", font=("Comic Sans MS", 12,'bold' ,"italic"),fg='#FF0606',bg='#FF9999',width=280)
                    
                    self.massge.place(x=4,y=4,width=285,height=30)
                    
                    self.view()
                    self.rest()
                    

                    self.root.after(2000, self.massge.destroy)#I Love This LINE-------------------------------------------->
                    
            except Exception as e:
                    messagebox.showinfo("Error",f':{str(e)} ',parent=self.root)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def rest(self):
        self.dept_combo.current(0)
        self.course_combo.current(0)
        self.sem_combo.current(0)
        self.Year_combo.current(0)
        self.sID_entry.delete(0,END)                  
        self.sDivision_combo.current(0)
        self.sName_entry.delete(0,END)
        self.sRoll_entry.delete(0,END)
        self.sGender_combo.current(0)
        self.sDob_entry.delete(0,END)
        self.sEmail_entry.delete(0,END)
        self.sPhoneNo_entry.delete(0,END)
        self.sAddress_entry.delete(0,END)
        self.sParents_entry.delete(0,END)
        self.var_radeio1.set(None)
        self.search_combo.current(0)
        self.search_entry.delete(0,END)

        self.view()
        imgpk=Image.open("Image1/No-Image.png")
        imgpk=imgpk.resize((205,220),Image.LANCZOS)
        self.imo=ImageTk.PhotoImage(imgpk)

        self.pl=Label(self.photo_label,image=self.imo)
        self.pl.place(x=2,y=1,width=200,height=220)
if __name__ == '__main__':
    root=Tk()
    obj=student_list(root)
    root.mainloop()

    