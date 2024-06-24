
import csv
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
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
        self.root.resizable(0,0)
        self.root.title("Face_Recognition")
        self.root.iconbitmap('Image1/my.ico')

        img=Image.open("Image1/gray_background.jpg")
        
        img=img.resize((1500,800),Image.LANCZOS)
        self.imge=ImageTk.PhotoImage(img)
        

        lebel1=Label(self.root,image=self.imge)
        lebel1.place(x=0,y=0,width=1500,height=800)

        self.exit_btn_img =Image.open("Image1/exit (3).png")
        self.exit_btn_img=self.exit_btn_img.resize((20,20),Image.LANCZOS)
        self.exit_btn_img=ImageTk.PhotoImage(self.exit_btn_img)


        self.exit_btn=Button(lebel1,image=self.exit_btn_img,command=self._exit,cursor="hand2",border='0')

        self.exit_btn.place(x=1450,y=1,width=25,height=25)
        # cap = cv2.VideoCapture(0)

        m_frame=Frame(lebel1)
        m_frame.place(x=10,y=30,width=1480,height=750)

        left_frame =LabelFrame(m_frame,text="Identification",fg='green',bg='#E5CCFF')
        left_frame.place(x=20, y=30, width=900, height=700)

        
        right_frame =LabelFrame(m_frame,text="Attedence Details",fg='green')
        right_frame.place(x=950, y=30, width=500, height=700)

#------------------------------camera frame-------------------------
        cam_frame =LabelFrame(left_frame,border=1)
        cam_frame.place(x=20, y=50, width=860, height=560)
        img1=Image.open("Image1/no_img.jpg")
        
        img1=img1.resize((860,560),Image.LANCZOS)
        self.imge1=ImageTk.PhotoImage(img1)

        self.cam_lable=Label(cam_frame,image=self.imge1)
        self.cam_lable.place(x=0, y=0, width=860, height=560)

        Play_btn_img=Image.open("Image1/Play_Button.png")
        Play_btn_im=Play_btn_img.resize((40,40),Image.LANCZOS)
        self.Play_btn_im=ImageTk.PhotoImage(Play_btn_im)

        Pause_btn_img=Image.open("Image1/Stop_Button.png")
        Pause_btn_im=Pause_btn_img.resize((40,40),Image.LANCZOS)
        self.Pause_btn_im=ImageTk.PhotoImage(Pause_btn_im)

        cam_btn1=Button(left_frame,cursor='hand2',image=self.Play_btn_im,command=self.show_frame,borderwidth='0',bg='#E5CCFF')
        cam_btn1.place(x=410, y=630, width=40, height=40)
        cam_btn2=Button(left_frame,cursor='hand2',image=self.Pause_btn_im,command=self.close,borderwidth='0',bg='#E5CCFF')
        cam_btn2.place(x=460, y=630, width=40, height=40)

        #--------------------------Right Frame-------------------------------
                #display fram
        display_frame=LabelFrame(right_frame)
        display_frame.place(x=2, y=2, width=490, height=240)

        self.photo_label=LabelFrame(display_frame,text="Photo", font=("Comic Sans MS", 10, "bold"),fg='red',bg='white')
        self.photo_label.place(x=0,y=2,width=210,height=230)
        imgpk=Image.open("Image1/No-Image.png")
        imgpk=imgpk.resize((205,220),Image.LANCZOS)
        self.imo=ImageTk.PhotoImage(imgpk)

        self.pl=Label(self.photo_label,image=self.imo)
        self.pl.place(x=2,y=1,width=200,height=220)
#----------------------------------------------------------------
        details_lable=LabelFrame(display_frame,bg='white')
        details_lable.place(x=215,y=12,width=260,height=115)

        name_lable=Label(details_lable,text='Name :', font=("Comic Sans MS", 10, "bold"),anchor=W)
        name_lable.place(x=5,y=2,width=70,height=25)

        self.name_lable=Label(details_lable,text='',bg='#FFFF99', font=("Comic Sans MS", 10, "bold"))
        self.name_lable.place(x=78,y=2,width=175,height=25)

        Roll_lable=Label(details_lable,text='Roll No. :', font=("Comic Sans MS", 10, "bold"),anchor=W)
        Roll_lable.place(x=5,y=27+2,width=70,height=25)

        self.Roll_lable=Label(details_lable,bg='#FFFF99', font=("Comic Sans MS", 10, "bold"))
        self.Roll_lable.place(x=78,y=27+2,width=175,height=25)
       
        Age_lable=Label(details_lable,text='Age :', font=("Comic Sans MS", 10, "bold"),anchor=W)
        Age_lable.place(x=5,y=(27*2)+2,width=70,height=25)
        self.Age_lable=Label(details_lable,bg='#FFFF99', font=("Comic Sans MS", 10, "bold"))
        self.Age_lable.place(x=78,y=(27*2)+2,width=175,height=25)
       
        Gender_lable=Label(details_lable,text='Gender :', font=("Comic Sans MS", 10, "bold"),anchor=W)
        Gender_lable.place(x=5,y=(27*3)+2,width=70,height=25)

        self.Gender_lable=Label(details_lable,bg='#FFFF99', font=("Comic Sans MS", 10, "bold"))
        self.Gender_lable.place(x=78,y=(27*3)+2,width=175,height=25)
#----------------------------------------------------------------------
        details_lable2=LabelFrame(display_frame,bg='white')
        details_lable2.place(x=215,y=115+13,width=125+15,height=72)  
        Teenager_lable=Label(details_lable2,text='Teenager :', font=("Helvetica", 10, "bold"),anchor=W)
        Teenager_lable.place(x=5,y=2,width=70,height=20)

        self.Teenager_lable=Label(details_lable2,text= '',bg='#CCFF99', font=("Helvetica", 10, "bold"),anchor=CENTER)
        self.Teenager_lable.place(x=78,y=2,width=55,height=20)

        adult_lable=Label(details_lable2,text='Adult :', font=("Helvetica", 10, "bold"),anchor=W)
        adult_lable.place(x=5,y=22+2,width=70,height=20)

        self.adult_lable=Label(details_lable2,text='',bg='#CCFF99', font=("Helvetica", 10, "bold"),anchor=CENTER)
        self.adult_lable.place(x=78,y=22+2,width=55,height=20)

       
        senior=Label(details_lable2,text='Senior :', font=("Helvetica", 10, "bold"),anchor=W)
        senior.place(x=5,y=44+2,width=70,height=20)

        self.senior=Label(details_lable2,text='',bg='#CCFF99', font=("Helvetica", 10, "bold"),anchor=CENTER)
        self.senior.place(x=78,y=44+2,width=55,height=20)
       

#----------------------------------------------------------
        details_lable3=LabelFrame(display_frame,bg='white')
        details_lable3.place(x=215+130+15,y=115+13,width=130-15,height=51) 

        Gender_lable=Label(details_lable3,text='Female :', font=("Helvetica", 10, "bold"),anchor=W)
        Gender_lable.place(x=2,y=2,width=55,height=20)

        self.Female_lable=Label(details_lable3,text='',bg='#CCFFE5', font=("Helvetica", 10, "bold"),anchor=CENTER)
        self.Female_lable.place(x=60,y=2,width=48,height=20)

        Gender_lable=Label(details_lable3,text='Male :', font=("Helvetica", 10, "bold"),anchor=W)
        Gender_lable.place(x=2,y=22+2,width=55,height=20)

        self.Male_lable=Label(details_lable3,text='', bg='#CCFFE5',font=("Helvetica", 10, "bold"),anchor=CENTER)
        self.Male_lable.place(x=60,y=22+2,width=48,height=20)

#----------------------------------------date entry----------------------------
        date_lable_frame=LabelFrame(display_frame,bg='#E5CCFF',border='0')
        date_lable_frame.place(x=215,y=115+13+73,width=125+22,height=30)
        date_lable=Label(date_lable_frame,text='Date :', font=("Helvetica", 10, "bold"),anchor=W)
        date_lable.place(x=3,y=5,width=45,height=20)
        self.entry_date=Entry(date_lable_frame,font=("Arial", 10),highlightthickness=1, bg="#E5CCFF",width=25)
        self.entry_date.place(x=52,y=5,width=90,height=20)
        
        cur_dt=datetime.datetime.now()
        hh=cur_dt.strftime('%d-%m-%Y')

        path=os.getcwd()+"\\StudentAttendance\\csvfiles\\"
#-----------------------------------------------Button--------------------------------
        button_lable=LabelFrame(display_frame,bg='#E5CCFF',border='0')
        button_lable.place(x=215+130+15,y=115+13+55,width=130-15,height=50)
        search_btn_img=Image.open("Image1/search.png")
        search_btn_im=search_btn_img.resize((50,45),Image.LANCZOS)
        self.search_btn_im=ImageTk.PhotoImage(search_btn_im)

        search_btn1=Button(button_lable,cursor='hand2',image=self.search_btn_im,command=lambda:self.search(path),borderwidth='0',bg='#E5CCFF')
        search_btn1.place(x=3, y=1, width=50, height=45)

        csv_btn_img=Image.open("Image1/csv_export.png")
        csv_btn_im=csv_btn_img.resize((50,45),Image.LANCZOS)
        self.csv_btn_im=ImageTk.PhotoImage(csv_btn_im)

        csv_btn1=Button(button_lable,cursor='hand2',image=self.csv_btn_im,command=self.CSV_file_save,borderwidth='0',bg='#E5CCFF')
        csv_btn1.place(x=58, y=1, width=50, height=45)


#---------------------------------exal sheet----------------------------------------

        exl_frame=LabelFrame(right_frame)
        exl_frame.place(x=3, y=252, width=490, height=420)

        t_lable_frame=LabelFrame(exl_frame,border=1,bg="white")
        t_lable_frame.place(x=2,y=2,width=480,height=410)

        xscroll_bar = ttk.Scrollbar(t_lable_frame,orient=HORIZONTAL)
        yscroll_bar=ttk.Scrollbar(t_lable_frame,orient=VERTICAL)


        self.student_table=ttk.Treeview(t_lable_frame,column=('DateTime','Name','Roll No.','Gender','DOB','SID'),xscrollcommand=xscroll_bar.set,yscrollcommand=yscroll_bar.set)
        xscroll_bar.pack(side=BOTTOM, fill=X)
        yscroll_bar.pack(side=RIGHT, fill=Y)
        xscroll_bar.config(command=self.student_table.xview)
        yscroll_bar.config(command=self.student_table.yview)

        #selt column widht___________________________________________
        self.student_table.column('DateTime',anchor=CENTER, width=150)
        self.student_table.column('Name',anchor=CENTER, width=180)
        self.student_table.column('Roll No.', anchor=CENTER,width=150)
        self.student_table.column('Gender',anchor=CENTER, width=150)
        self.student_table.column('DOB',anchor=CENTER, width=150)
        self.student_table.column('SID',anchor=CENTER, width=50)
        
        # set column heading________________________________________
        self.student_table.heading('DateTime',text='DateTime',anchor=CENTER)
        self.student_table.heading('Name',text='Name',anchor=CENTER)
        self.student_table.heading('Roll No.',text='Roll No.',anchor=CENTER)
        self.student_table.heading('DOB',text='DOB',anchor=CENTER)
        self.student_table.heading('Gender',text='Gender',anchor=CENTER)
        self.student_table.heading('SID',text='SID',anchor=CENTER)
        
        self.student_table['show']='headings'
        self.student_table.bind('<ButtonRelease>',self.mouse_click)

        self.student_table.pack(fill=BOTH,expand=1)
        # self.view()
        self.view(hh,path)
#----------------------------main recognition algo-------------
        # self.encodelk = np.load("Encode_Images.npy")
        # self.personNames = np.load("Student_Name.npy")
        # self.SID = np.load("Student_ID.npy")
        # self.student_id=0
        # print("All Encodings Complete!!!")

        
        
    def show_frame(self):
        cascad = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        lbph = cv2.face.LBPHFaceRecognizer_create()
        lbph.read('encoding_data.yml')

        self.cap = cv2.VideoCapture(2)
        if not self.cap.isOpened():
            print("Failed to open webcam.")
            return

        self.con = True
        attendlist = []
        atte = 0

        while True:
            _, frame = self.cap.read()
            frame = cv2.flip(frame, 1)
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = cascad.detectMultiScale(
                gray_frame,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(150, 150),
                flags=cv2.CASCADE_SCALE_IMAGE
            )

            for (x, y, w, h) in faces:
                np_frame = np.array(gray_frame[y:y+h, x:x+w], 'uint8')
                student_id, confidence = lbph.predict(np_frame)
                persatage = int(100 * (1 - confidence / 300))

                print(f"Predicted ID: {student_id}, Confidence: {confidence}, Percentage: {persatage}%")

                namepos = (x + 5, y - 5)
                confpos = (x + 5, y + h - 5)

                if confidence < 100:
                    if persatage > 83:
                        db = mysql.connector.connect(user='root', password='pass0808', host='localhost', port=3306)
                        cdb = db.cursor()
                        cdb.execute("USE student_data")
                        cdb.execute(f"SELECT SName FROM data1 WHERE SID = {student_id}")
                        nm = cdb.fetchone()
                        db.close()

                        if nm is not None:
                            name = nm[0]
                            attendlist.append(student_id)
                            atte += 1
                            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 204), 2)
                            cv2.putText(frame, str(name), namepos, cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                            cv2.putText(frame, str(f"{persatage}%"), confpos, cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 1)
                        else:
                            name = "Unknown"
                            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
                            cv2.putText(frame, name, namepos, cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
                            cv2.putText(frame, str(f"{persatage}%"), confpos, cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 1)
                    else:
                        name = "Unknown"
                        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
                        cv2.putText(frame, name, namepos, cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
                        cv2.putText(frame, str(f"{persatage}%"), confpos, cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 1)
                else:
                    name = "Unknown"
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
                    cv2.putText(frame, name, namepos, cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
                    cv2.putText(frame, str(f"{persatage}%"), confpos, cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0), 1)

            
            # self.ll=Image.fromarray(cv2image)
            img1=Image.fromarray(frame)
            img3=img1.resize((860,560),Image.LANCZOS)
            self.imgtk = ImageTk.PhotoImage(image=img3)
            self.cam_lable['image']=self.imgtk
            self.root.update()
            if self.con==False:
                break 
            #---------------------------------attendenc taker callig------------------------
            if atte== 40:
                student_id=max(attendlist,key=attendlist.count)
                try:

                    db = mysql.connector.connect(user='root', password='pass0808', host='localhost', port=3306)
                    cdb = db.cursor()

                    cdb.execute("use student_data")
                    cdb.execute(f"select SID from data1 where SID = {student_id}")
                    i=cdb.fetchone()
                    
                    
                    if (str(student_id) == str(i[0])) :
                    #     # print(self.student_id)
                    #     # print (i[0],j[0])
                        self.markAttendance(student_id)
                    db.close()
                except :
                    pass
                attendlist.clear()
                atte=0

    #---------------------------------exit------------------------
    def _exit(self):
        ma=messagebox.askyesno("Warning!","Do you want to exit ?",parent=self.root)
        if ma>0:
                self.root.destroy()
#-------------------------------------------------------------------------------------------------------------
    def close(self):
        self.con=False
        self.cap.release()
        cv2.destroyAllWindows()
        self.cam_lable['image']=self.imge1
        self.name_lable['text']=''
        self.root.update()

#-------------------------------------------------------------------------------------------------------------
    def markAttendance(self,student_id):
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
                sid.append(int(entry[5]))
            print(sid[:])
            # print(sid)
            if int(student_id) not in sid:
 #-------------------------------------------------------------------------------------------------
                db = mysql.connector.connect(user='root', password='pass0808', host='localhost', port=3306)
                cdb = db.cursor()

                cdb.execute("use student_data")
                cdb.execute(f"select SName,Roll_No,Gender,DOB,SID from data1 where SID = {student_id}")
                result=cdb.fetchall()
                restult=list(result[0])
#---------------------------------------------------------------------------------------------------------------
                now = datetime.datetime.now()
                dtString = now.strftime('%H:%M:%S')
                restult.insert(0,dtString)
                # print(restult)
                # f.writelines(f'\n{restult}')
                w=csv.writer(f)
                w.writerow(restult)

                db.close()
        self.view(hh,path)
#--------------------------------------------------------------------------------
    def search(self,path):
        # path=os.getcwd()+"\\StudentAttendance\\csvfiles\\"
        dd=self.entry_date.get()
        if '.' in dd:
            date=dd.replace('.','-')
        elif '/' in dd:
            date=dd.replace('/','-')
        else: date=dd
        self.view(date,path)
#-------------------------------------------------------------------------
    def view(self,hh,path):
        self.entry_date.delete(0,END)
        self.entry_date.insert(0,str(hh))
        cur_dt=datetime.datetime.now()
        # hh=cur_dt.strftime('%d-%m-%Y')
        cr_yy=cur_dt.strftime('%Y')
        cr_mm=cur_dt.strftime('%m')
        cr_dd=cur_dt.strftime('%d')

        # path=os.getcwd()+"\\StudentAttendance\\csvfiles\\"
        gender=[]
        dob=[]
        age=[]
        self.SaveCsvPath=f'{path}Attendance {hh}.csv'
        if (os.path.isfile(f'{path}Attendance {hh}.csv'))==True:
            with open(f'{path}Attendance {hh}.csv', 'r+',newline='') as f:
            # with open(f'{path}Attendance 08-02-2022.csv', 'r+',newline='') as f:
        
                result=csv.reader(f)
                result=list(result)
                if len(result) !=0:

                    self.student_table.delete(*self.student_table.get_children())
                    for i in result:
                        self.student_table.insert('',END,values=i)
                        gender.append(i[3].upper())
                        dob.append(i[4])
                    for i in dob:
                        try:
                            bd=i.replace('.','/')
                            bd=datetime.datetime.strptime(bd,'%d/%m/%Y').date()
                            hi=(int(cr_yy)-int(datetime.datetime.strftime(bd,'%Y'))-((int(cr_mm), int(cr_dd)) <
                            (int(datetime.datetime.strftime(bd,'%m')), int(datetime.datetime.strftime(bd,'%d')))))
                            age.append(hi)
                        except:
                            bd=i.replace('-','/')
                            bd=datetime.datetime.strptime(bd,'%d/%m/%Y').date()
                            hi=(int(cr_yy)-int(datetime.datetime.strftime(bd,'%Y'))-((int(cr_mm), int(cr_dd)) <
                            (int(datetime.datetime.strftime(bd,'%m')), int(datetime.datetime.strftime(bd,'%d')))))
                            age.append(hi)
                    t=a=s=0
                    for i in age:
                        if i<18:
                            t+=1
                        elif i>18 and i<60:
                            a+=1
                        else:
                            s+=1
                    self.adult_lable['text']=a
                    self.senior['text']=s
                    self.Teenager_lable['text']=t

                    self.Female_lable['text']=('{}').format(gender.count('FEMALE'))
                    self.Male_lable['text']=('{}').format(gender.count('MALE'))
                    
                    # print(age,a,t,s,gender,gender.count('MALE'),gender.count('FEMALE'))
        else:
            self.student_table.delete(*self.student_table.get_children())
#--------------------------------------------------------------------------------------------------------------------
    def mouse_click(self,even):
        cur_dt=datetime.datetime.now()
        cr_yy=cur_dt.strftime('%Y')
        cr_mm=cur_dt.strftime('%m')
        cr_dd=cur_dt.strftime('%d')

        st=self.student_table.focus()
        mk=self.student_table.item(st)
        ls=mk['values']
        if len(ls)!=0:
            self.name_lable['text']=ls[1]
            self.Roll_lable['text']=ls[2]
            self.Gender_lable['text']=ls[3]
            
            try:
                bd=ls[4].replace('.','/')
                bd=datetime.datetime.strptime(bd,'%d/%m/%Y').date()
                hi=(int(cr_yy)-int(datetime.datetime.strftime(bd,'%Y'))-((int(cr_mm), int(cr_dd)) <
                (int(datetime.datetime.strftime(bd,'%m')), int(datetime.datetime.strftime(bd,'%d')))))
                self.Age_lable['text']=hi
            except:
                bd=ls[4].replace('-','/')
                bd=datetime.datetime.strptime(bd,'%d/%m/%Y').date()
                hi=(int(cr_yy)-int(datetime.datetime.strftime(bd,'%Y'))-((int(cr_mm), int(cr_dd)) <
                (int(datetime.datetime.strftime(bd,'%m')), int(datetime.datetime.strftime(bd,'%d')))))
                self.Age_lable['text']=hi

            path=os.getcwd()+"\\ImagesAttendance\\StudentPhotos\\"

            myList = os.listdir(path)
            # print(myList)
            k=True
            for cu_i in myList:
                # print(ls[0],cu_i)
                if str(ls[5]) in cu_i:
                    img=Image.open(f"{path}/{cu_i}")
                    img=img.resize((205,220),Image.LANCZOS)
                    self.imo=ImageTk.PhotoImage(img)
                    # print(self.imo)
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

#---------------------------------------------------------------------------------

    def CSV_file_save(self):
        files = [('CSV', '*.csv'),('Text Document', '*.txt')]
        file_name=(os.path.split(self.SaveCsvPath)[1]).split('.')[0]
        # print(file_name)
        if (os.path.isfile(self.SaveCsvPath))==True:
            f = filedialog.asksaveasfile(title='Save as',filetypes=files,mode='w',initialfile =file_name, defaultextension=".csv",parent=self.root)
            if f is None: 
                    return
            with open(self.SaveCsvPath, 'r+',newline='') as q:

                result=q.readlines()
                result=list(result)
              
                if len(result) !=0:
                    for i in result:
                        i=i.replace('\n','')
                        f.writelines(i)
              
                f.close()
if __name__ == '__main__':
    root = Tk()
    obj = kk(root)
    root.mainloop()
