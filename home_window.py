from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import os


from HelpWindow import GetHelp
from Studen_details import student_list
from Train_Images import face_encoder
from FaceRecognition import kk
class main_system:
    def __init__(self,root):
        self.root=root
        
        self.root.geometry("1500x800+0+0")
        self.root.resizable(0,0)
        self.root.attributes('-topmost', False)
        self.root.title("system")
        self.root.iconbitmap('Image1/my.ico')
      

        img3 = Image.open("Image1/pngwing.com.png").convert('RGBA')

        img = img3.resize((1500, 130), Image.LANCZOS)
        self.imge3 = ImageTk.PhotoImage(img)

        lebel3 = Label(image=self.imge3)
        lebel3.place(x=0, y=0, width=1500, height=130)
        # lebel1.pack()

        txt_lab=Label(lebel3,text="FACE RECOGNITION",font=("times new roman",35,"bold"),fg="blue",borderwidth=0)
        txt_lab.place(x=500,y=22)



        bg_img = Image.open("Image1/Bg.jpg")
        bg_img = bg_img.resize((1500, 670), Image.LANCZOS)
        self.bg_imge = ImageTk.PhotoImage(bg_img)

        bg_lebel1 = Label(image=self.bg_imge)
        bg_lebel1.place(x=0, y=130, width=1500, height=670)
        # lebel1.pack()


        #button 1
        btn_img1 = Image.open("Image1/pngfind.com-maintenance-icon-png-4652096.png")
        btn_img1 = btn_img1.resize((120, 100), Image.LANCZOS)
        self.btn_imge = ImageTk.PhotoImage(btn_img1)

        btn_1=Button(bg_lebel1,image=self.btn_imge,command=self.student_details,cursor="hand2",borderwidth="0")
        btn_1.place(x=220,y=495,width=120,height=100)

        btn_2=Button(bg_lebel1,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",12,"bold"),borderwidth="0")
        btn_2.place(x=220,y=595,width=120,height=40)

        #button 2
        btn_img2 = Image.open("Image1/training.png")
        btn_img2 = btn_img2.resize((120, 100), Image.LANCZOS)
        self.btn_imge2 = ImageTk.PhotoImage(btn_img2)

        btn_3=Button(bg_lebel1,image=self.btn_imge2,command=self.Training,cursor="hand2",borderwidth="0")
        btn_3.place(x=375,y=495,width=120,height=100)

        btn_4=Button(bg_lebel1,text="Reload Images",command=self.Training,cursor="hand2",font=("times new roman",12,"bold"),borderwidth="0")
        btn_4.place(x=375,y=595,width=122,height=40)

        #button 3
        btn_img3 = Image.open("Image1/facial-recognition.jpg")
        btn_img3 = btn_img3.resize((120, 100), Image.LANCZOS)
        self.btn_imge3 = ImageTk.PhotoImage(btn_img3)

        btn_5=Button(bg_lebel1,image=self.btn_imge3,cursor="hand2",command=self.face_rec,borderwidth="0")
        btn_5.place(x=530,y=495,width=120,height=100)

        btn_6=Button(bg_lebel1,text="Face Detector",cursor="hand2",command=self.face_rec,font=("times new roman",12,"bold"),borderwidth="0")
        btn_6.place(x=530,y=595,width=122,height=40)

        #button 4
        btn_img4 = Image.open("Image1/images2.png")
        btn_img4 = btn_img4.resize((120, 100), Image.LANCZOS)
        self.btn_imge4 = ImageTk.PhotoImage(btn_img4)
#===================================================================================================================
        btn_7=Button(bg_lebel1,image=self.btn_imge4,command=self.view_attendance
                     ,cursor="hand2",borderwidth="0")
        btn_7.place(x=685,y=495,width=120,height=100)

        btn_8=Button(bg_lebel1,text="Attendance",cursor="hand2",command=self.view_attendance,font=("times new roman",12,"bold"),borderwidth="0")
        btn_8.place(x=685,y=595,width=122,height=40)
#=====================================================================================================================
        #button 5
        btn_img5 = Image.open("Image1/recognize1.jpg")
        btn_img5 = btn_img5.resize((120, 100), Image.LANCZOS)
        self.btn_imge5 = ImageTk.PhotoImage(btn_img5)

        btn_9=Button(bg_lebel1,image=self.btn_imge5,command=self.view_img,cursor="hand2",borderwidth="0")
        btn_9.place(x=840,y=495,width=120,height=100)

        btn_10=Button(bg_lebel1,text="Photos",command=self.view_img,cursor="hand2",font=("times new roman",15,"bold"),borderwidth="0")
        btn_10.place(x=840,y=595,width=122,height=40)

        #button 6
        btn_img6 = Image.open("Image1/help_icon.png")
        btn_img6 = btn_img6.resize((120, 100), Image.LANCZOS)
        self.btn_imge6 = ImageTk.PhotoImage(btn_img6)

        btn_11=Button(bg_lebel1,image=self.btn_imge6,bg='#0B1222',command=self.gethelp,cursor="hand2",border="0")

        btn_11.place(x=995,y=495,width=120,height=100)

        btn_12=Button(bg_lebel1,text="Help",command=self.gethelp,cursor="hand2",font=("times new roman",15,"bold"),border="0")
        btn_12.place(x=995,y=595,width=120,height=40)

        #button 7
        # btn_img7 = Image.open("Image1/exit_.png")
        # btn_img7 = btn_img7.resize((120, 100), Image.LANCZOS)
        self.btn_imge7 =PhotoImage(file="Image1/exit (3).png")

        btn_13=Button(bg_lebel1,image=self.btn_imge7,command=self._exit,bg='#0B1222',cursor="hand2",border='0')

        btn_13.place(x=1150,y=495,width=120,height=100)

        btn_14=Button(bg_lebel1,text="Exit",command=self._exit,cursor="hand2",font=("times new roman",15,"bold"),borderwidth="0")
        btn_14.place(x=1150,y=595,width=120,height=40)

#--------------------student details----------------------
    def student_details(self):
            newindow=Toplevel(self.root)
            self.data=student_list(newindow)
#---------------------view photo---------------------------
    def view_img(self):
        path=os.getcwd()+"\\ImagesAttendance\\StudentPhotos\\"
        os.startfile(path)
#--------------------------------------------------------------
    def view_attendance(self):
        path=os.getcwd()+"\\StudentAttendance\\csvfiles"
        os.startfile(path)

#---------------------------------exit------------------------
    def _exit(self):
        ma=messagebox.askyesno("Warning!","Do you want to exit ?",parent=self.root)
        if ma>0:
                self.root.destroy()
#---------------------------------------------------------------------------
    def gethelp(self):
            newindow=Toplevel(self.root)
            self.data=GetHelp(newindow)
#---------------------------------------------------------------------------
    def face_rec(self):
            newindow=Toplevel(self.root)
            self.data=kk(newindow)
            #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Training>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def Training(self):
                newindow=Toplevel(self.root)
                path=os.getcwd()+"\\ImagesAttendance\\StudentPhotos\\SampleOfPhoto\\"
            

                self.data=face_encoder(newindow,path)

if __name__ == '__main__':
    root=Tk()
    obj=main_system(root)
    root.mainloop()
