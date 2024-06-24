


import csv
import face_recognition
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Labelframe
import numpy as np
import cv2
import datetime
import os
import mysql.connector
from PIL import Image, ImageTk
from tkinter import messagebox
class kk:
    def __init__(self,root):
        self.root =root
        self.root.geometry("1500x800")

        self.root.title("Face_Recognition")
        self.root.iconbitmap('Image1/my.ico')

        img=Image.open("Image1/gray_background.jpg")
        
        img=img.resize((1500,800),Image.ANTIALIAS)
        self.imge=ImageTk.PhotoImage(img)
        

        lebel1=Label(self.root,image=self.imge)
        lebel1.place(x=0,y=0,width=1500,height=800)

        self.exit_btn_img =Image.open("Image1/exit (3).png")
        self.exit_btn_img=self.exit_btn_img.resize((20,20),Image.ANTIALIAS)
        self.exit_btn_img=ImageTk.PhotoImage(self.exit_btn_img)


        self.exit_btn=Button(lebel1,image=self.exit_btn_img,command=self._exit,cursor="hand2",border='0')

        self.exit_btn.place(x=1450,y=1,width=25,height=25)
        # cap = cv2.VideoCapture(0)

        m_frame=Frame(lebel1)
        m_frame.place(x=10,y=30,width=1480,height=750)

        left_frame =LabelFrame(m_frame,text="Identification",fg='green')
        left_frame.place(x=20, y=30, width=900, height=700)

        
        right_frame =LabelFrame(m_frame,text="Attedence Details",fg='green')
        right_frame.place(x=950, y=30, width=500, height=700)

#------------------------------camera frame-------------------------
        cam_frame =LabelFrame(left_frame,border=1)
        cam_frame.place(x=20, y=50, width=860, height=560)
        img1=Image.open("Image1/no_img.jpg")
        
        img1=img1.resize((860,560),Image.ANTIALIAS)
        self.imge1=ImageTk.PhotoImage(img1)

        self.cam_lable=Label(cam_frame,image=self.imge1)
        self.cam_lable.place(x=0, y=0, width=860, height=560)

        Play_btn_img=Image.open("Image1/Play_Button.png")
        Play_btn_im=Play_btn_img.resize((40,40),Image.ANTIALIAS)
        self.Play_btn_im=ImageTk.PhotoImage(Play_btn_im)

        Pause_btn_img=Image.open("Image1/Stop_Button.png")
        Pause_btn_im=Pause_btn_img.resize((40,40),Image.ANTIALIAS)
        self.Pause_btn_im=ImageTk.PhotoImage(Pause_btn_im)

        cam_btn1=Button(left_frame,cursor='hand2',image=self.Play_btn_im,command=self.show_frame,borderwidth='0')
        cam_btn1.place(x=410, y=630, width=40, height=40)
        cam_btn2=Button(left_frame,cursor='hand2',image=self.Pause_btn_im,command=self.close,borderwidth='0')
        cam_btn2.place(x=460, y=630, width=40, height=40)

        #--------------------------Right Frame-------------------------------
                #display fram
        display_frame=LabelFrame(right_frame)
        display_frame.place(x=2, y=2, width=490, height=240)

        self.photo_label=LabelFrame(display_frame,text="Photo", font=("Comic Sans MS", 10, "bold"),fg='red',bg='white')
        self.photo_label.place(x=0,y=2,width=210,height=230)
        imgpk=Image.open("Image1/No-Image.png")
        imgpk=imgpk.resize((205,220),Image.ANTIALIAS)
        self.imo=ImageTk.PhotoImage(imgpk)

        self.pl=Label(self.photo_label,image=self.imo)
        self.pl.place(x=2,y=1,width=200,height=220)
#----------------------------------------------------------------
        details_lable=LabelFrame(display_frame)
        details_lable.place(x=215,y=12,width=260,height=115)

        name_lable=Label(details_lable,text='Name :', font=("Comic Sans MS", 10, "bold"))
        name_lable.grid(column=0,row=0, padx=10, pady=5, sticky=W)

        self.name_lable=Label(details_lable,text='', font=("Comic Sans MS", 10, "bold"))
        self.name_lable.grid(column=1,row=0, padx=1, pady=0, sticky=W)

        Roll_lable=Label(details_lable,text='Roll No. :', font=("Comic Sans MS", 10, "bold"))
        Roll_lable.grid(column=0,row=1, padx=1, pady=0, sticky=W)

        self.Roll_lable=Label(details_lable, font=("Comic Sans MS", 10, "bold"))
        self.Roll_lable.grid(column=1,row=1, padx=1, pady=0, sticky=W)
       
        Age_lable=Label(details_lable,text='Age :', font=("Comic Sans MS", 10, "bold"))
        Age_lable.grid(column=0,row=2, padx=1, pady=0, sticky=W)

        self.Age_lable=Label(details_lable, font=("Comic Sans MS", 10, "bold"))
        self.Age_lable.grid(column=1,row=2, padx=1, pady=0, sticky=W)
       
        Gender_lable=Label(details_lable,text='Gender :', font=("Comic Sans MS", 10, "bold"))
        Gender_lable.grid(column=0,row=3, padx=1, pady=0, sticky=W)

        self.Gender_lable=Label(details_lable, font=("Comic Sans MS", 10, "bold"))
        self.Gender_lable.grid(column=1,row=3, padx=1, pady=0, sticky=W)
#----------------------------------------------------------------------
        details_lable2=LabelFrame(display_frame)
        details_lable2.place(x=215,y=115+13,width=125,height=105)  
        Teenager_lable=Label(details_lable2,text='Teenager :', font=("Comic Sans MS", 10, "bold"))
        Teenager_lable.grid(column=0,row=0, padx=5, pady=0, sticky=W)

        self.Teenager_lable=Label(details_lable2,text= '', font=("Comic Sans MS", 10, "bold"))
        self.Teenager_lable.grid(column=1,row=0, padx=5, pady=0, sticky=W)

        adult_lable=Label(details_lable2,text='Adult :', font=("Comic Sans MS", 10, "bold"))
        adult_lable.grid(column=0,row=1, padx=5, pady=0, sticky=W)

        self.adult_lable=Label(details_lable2,text='', font=("Comic Sans MS", 10, "bold"))
        self.adult_lable.grid(column=1,row=1, padx=5, pady=0, sticky=W)

       
        senior=Label(details_lable2,text='senior :', font=("Comic Sans MS", 10, "bold"))
        senior.grid(column=0,row=2, padx=5, pady=0, sticky=W)

        self.senior=Label(details_lable2,text='', font=("Comic Sans MS", 10, "bold"))
        self.senior.grid(column=1,row=2, padx=5, pady=0, sticky=W)
       

#----------------------------------------------------------
        details_lable3=LabelFrame(display_frame)
        details_lable3.place(x=215+130,y=115+13,width=130,height=105) 

        Gender_lable=Label(details_lable3,text='Female :', font=("Comic Sans MS", 10, "bold"))
        Gender_lable.grid(column=0,row=0, padx=5, pady=5, sticky=W)

        self.Female_lable=Label(details_lable2,text='', font=("Comic Sans MS", 10, "bold"))
        self.Female_lable.grid(column=1,row=0, padx=5, pady=5, sticky=W)

        Gender_lable=Label(details_lable3,text='Male :', font=("Comic Sans MS", 10, "bold"))
        Gender_lable.grid(column=0,row=1, padx=5, pady=5, sticky=W)

        self.Male_lable=Label(details_lable2,text='', font=("Comic Sans MS", 10, "bold"))
        self.Male_lable.grid(column=1,row=1, padx=5, pady=5, sticky=W)

#---------------------------------exal sheet----------------------------------------

        exl_frame=LabelFrame(right_frame)
        exl_frame.place(x=3, y=252, width=490, height=420)

        t_lable_frame=LabelFrame(exl_frame,border=1,bg="white")
        t_lable_frame.place(x=2,y=2,width=480,height=410)

        xscroll_bar = ttk.Scrollbar(t_lable_frame,orient=HORIZONTAL)
        yscroll_bar=ttk.Scrollbar(t_lable_frame,orient=VERTICAL)


        self.student_table=ttk.Treeview(t_lable_frame,column=('SID','Name','Roll No.','DOB','Gender','DateTime'),xscrollcommand=xscroll_bar.set,yscrollcommand=yscroll_bar.set)
        xscroll_bar.pack(side=BOTTOM, fill=X)
        yscroll_bar.pack(side=RIGHT, fill=Y)
        xscroll_bar.config(command=self.student_table.xview)
        yscroll_bar.config(command=self.student_table.yview)

        #selt column widht___________________________________________
        self.student_table.column('SID',anchor=CENTER, width=50)
        self.student_table.column('Name',anchor=CENTER, width=180)
        self.student_table.column('Roll No.', anchor=CENTER,width=150)
        self.student_table.column('DOB',anchor=CENTER, width=150)
        self.student_table.column('Gender',anchor=CENTER, width=150)
        self.student_table.column('DateTime',anchor=CENTER, width=150)
        
        # set column heading________________________________________
        self.student_table.heading('SID',text='SID',anchor=CENTER)
        self.student_table.heading('Name',text='Name',anchor=CENTER)
        self.student_table.heading('Roll No.',text='Roll No.',anchor=CENTER)
        self.student_table.heading('DOB',text='DOB',anchor=CENTER)
        self.student_table.heading('Gender',text='Gender',anchor=CENTER)
        self.student_table.heading('DateTime',text='DateTime',anchor=CENTER)
        
        self.student_table['show']='headings'
        # self.student_table.bind('<ButtonRelease>',self.mouse_click)

        self.student_table.pack(fill=BOTH,expand=1)
        # self.view()

#----------------------------main recognition algo-------------
        self.encodelk = np.load("Encode_Images.npy")
        # self.personNames = np.load("Student_Name.npy")
        self.SID = np.load("Student_ID.npy")
        self.student_id=0
        # print("All Encodings Complete!!!")

        
    def show_frame(self):
        self.cap = cv2.VideoCapture(0)
        self.con=True
        cascad=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        while True:
            _, frame = self.cap.read()
            frame = cv2.flip(frame, 1)
            
            faces = cv2.resize(frame,(0, 0), None, 0.25, 0.25)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

            fac_cur_fm=face_recognition.face_locations(self.faces)
            # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # faces = cascad.detectMultiScale(gray_frame,scaleFactor=1.3,minNeighbors=5,minSize=(30, 30))

            # print(faces)
            # for (x,y,w,h) in faces:
            #       x1=x
            #       x2=x+w
            #       y1=y
            #       y2=y+h
            encod_cur_fm= face_recognition.face_encodings(self.faces,fac_cur_fm)

            for encodeFace, faceLoc in zip(encod_cur_fm,fac_cur_fm):
                face_matches=face_recognition.compare_faces(self.encodelk,encodeFace)
                face_dis=face_recognition.face_distance(self.encodelk, encodeFace)
                match_index= np.argmin(face_dis)
                print(face_matches[match_index])
                if face_matches[match_index]:
                    # self.name=self.personNames[match_index].upper()
                    self.student_id= str(self.SID[match_index])
                    db = mysql.connector.connect(user='root', password='pass0808', host='localhost', port=3306)
                    cdb = db.cursor()

                    cdb.execute("use student_data")
                    
                    cdb.execute(f"select SName from data1 where SID = {self.student_id}")
                    nm=cdb.fetchone()
                    db.close()
                    
                    if nm is not None:
                        try:
                            self.name=nm[0]
                        except :
                            messagebox.showerror("Error!","Student Images are not Reloaded\n\t[\'Please Reload First\']",parent=self.root)
                        # print(self.student_id)
                else:
                    self.name = "Unknown"
                    self.student_id=0

                y1,x2,y2,x1= faceLoc
                y1, x2, y2, x1=  y1*4,x2*4,y2*4,x1*4
            #print(f'{y1}\t{y2}\t{x1}\t{x2}')
                cv2.rectangle(frame,(x1,y1-11),(x2,y2),(0,0,204),2)
                cv2.rectangle(frame, (x1-2, y1 - 12), (x2+2, y2+2), (0,255,0), 2)
                cv2.rectangle(frame,(x1-2,y1-20),(x2+2,y1-11),(0,255,0),cv2.FILLED)
                cv2.rectangle(frame, (x2+33, y1 + 27), ((x2 * 2) - 198, y1 + 35), (0,255,0), cv2.FILLED)
                cv2.line(frame,  (x2+2, y1 - 11),(x2+25,y1 + 35), (10,255,0, 2,), lineType=4)
                cv2.line(frame, (x2+25, y1 + 35), ((x2 * 2) - 198, y1 + 27), (0,255,0), 2, lineType=4)
            # cv2.rectangle(frame, (x1, y2 -35 ), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.rectangle(frame, (x2+35,y1), ((x2*2)-200, y1+25), (3,20,2), cv2.FILLED)
                cv2.rectangle(frame, (x2 + 33, y1-2), ((x2 * 2) - 198, y1 + 27), (0,255,0),1)
                # cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
                cv2.putText(frame, self.name, (x2 + 41, y1 +16), cv2.FONT_HERSHEY_COMPLEX, 0.50, (255,255,255), 2)
                # fancyDraw(frame,faceLoc)
            # cv2.imshow('camp',frame)



            # self.ll=Image.fromarray(cv2image)
            img1=Image.fromarray(frame)
            img3=img1.resize((860,560),Image.ANTIALIAS)
            self.imgtk = ImageTk.PhotoImage(image=img3)
            self.cam_lable['image']=self.imgtk
            self.root.update()
            if self.con==False:
                break 
            try:

                db = mysql.connector.connect(user='root', password='pass0808', host='localhost', port=3306)
                cdb = db.cursor()

                cdb.execute("use student_data")
                cdb.execute(f"select SID from data1 where SID = {self.student_id}")
                i=cdb.fetchone()
                cdb.execute(f"select SName from data1 where SID = {self.student_id}")
                j=cdb.fetchone()
                # print (i,j)
                
                if ((str(self.student_id) == str(i[0])) and (self.name==j[0].upper())):
                    # print(self.student_id)
                    # print (i[0],j[0])
                    self.markAttendance()
                db.close()
            except :
                pass
    #---------------------------------exit------------------------
    def _exit(self):
        ma=messagebox.askyesno("Warning!","Do you want to exit ?",parent=self.root)
        if ma>0:
                self.root.destroy()
    def close(self):
        self.con=False
        self.cap.release()
        cv2.destroyAllWindows()
        self.cam_lable['image']=self.imge1
        self.name_lable['text']=''
        self.root.update()

    def markAttendance(self):
#-------------------------------------------------------------------------------------------------------------
        cur_dt=datetime.datetime.now()
        hh=cur_dt.strftime('%d-%m-%Y')

        path=os.getcwd()+"\\StudentAttendance\\csvfiles\\"
        if (os.path.isdir(path))!=True:       
            os.makedirs(path)
            
            print("false")
        if (os.path.isfile(f'{path}Attendance {hh}.csv'))!=True: 
            with open(f'{path}Attendance {hh}.csv', 'w') as f:
                pass

        with open(f'{path}Attendance {hh}.csv', 'r+',newline='') as f:
            # myData = csv.reader(f)
            # myDataList=list(myData)
            myDataList=f.readlines()
            # print(myDataList)
        #---------------------------------------------------------------------------------------

            # print(list(myData))
            sid = []
            for line in myDataList:
                entry = line.split(',')
                sid.append(entry[0])
            print(sid[:])
            if str(self.student_id) not in sid:
 #-------------------------------------------------------------------------------------------------
                db = mysql.connector.connect(user='root', password='pass0808', host='localhost', port=3306)
                cdb = db.cursor()

                cdb.execute("use student_data")
                cdb.execute(f"select SID,SName,Roll_No,Gender,DOB from data1 where SID = {self.student_id}")
                result=cdb.fetchall()
                restult=list(result[0])
#---------------------------------------------------------------------------------------------------------------
                now = datetime.datetime.now()
                dtString = now.strftime('%H:%M:%S')
                restult.append(dtString)
                print(restult)
                # f.writelines(f'\n{restult}')
                w=csv.writer(f)
                w.writerow(restult)

                db.close()
    # def view(self):
    #     db = mysql.connector.connect(user='root', password='pass0808', host='localhost', port=3306)
    #     cdb = db.cursor()

    #     cdb.execute("use student_data")
    #     cdb.execute(f"select SID,SName,Roll_No,Gender,DOB from data1 where SID = {self.student_id}")
    #     result=cdb.fetchall()
    #     print(result)
        # if len(result) !=0:
        #     self.student_table.delete(*self.student_table.get_children())
        #     for i in result:
        #         self.student_table.insert('',END,values=i)

        # db.close()
    # def mouse_click(self,even):
    #     st=self.student_table.focus()
    #     mk=self.student_table.item(st)
    #     ls=mk['values']
    #     self.dept_combo.set(ls[1])
    #     self.var_SID.set(ls[2])
    #     self.var_SName.set(ls[3])
    #     self.var_roll_no.set(ls[4])
    #     self.course_combo.set(ls[5])
    #     self.Year_combo.set(ls[6])
    #     self.sem_combo.set(ls[7])
    #     self.var_div.set(ls[8])
    #     self.var_phone_no.set(ls[9])
    #     self.var_Email.set(ls[10])
    #     self.sGender_combo.set(ls[11])
    #     self.var_dob.set(ls[12])
    #     self.var_Address.set(ls[13])
    #     self.var_parents.set(ls[14])
    #     self.var_radeio1.set(ls[15])
    # # ~~~~~~~~~~~~~~~~~~~~~~~~~~~Image~~~~~~~~~~~~~~~~~~~~~~~~ 
    #     path = 'G:\PycharmProjects\Face_recognitaion\ImagesAttendance'

    #     myList = os.listdir(path)
    #     # print(myList)
        
    #     for cu_i in myList:
    #         if ls[3] in cu_i:
    #             img=Image.open(f"ImagesAttendance/{cu_i}")
    #             img=img.resize((205,220),Image.ANTIALIAS)
    #             self.imo=ImageTk.PhotoImage(img)

    #             self.pl=Label(self.photo_label,image=self.imo)
    #             self.pl.place(x=2,y=1,width=200,height=220)
if __name__ == '__main__':
    root = Tk()
    obj = kk(root)
    root.mainloop()
