from tkinter import *
import numpy as np
import cv2
from PIL import Image, ImageTk
import os

from sqlalchemy import true
class Take:
    def __init__(self,root,jj,sid):
        self.root = root
        self.root.geometry("1000x700+0+0")
        self.root.title("Camera")
        # self.root.attributes('-topmost',True)
        self.root.iconbitmap('Image1/my.ico')

        self.sname=jj
        self.sid=sid
        img=Image.open("Image1/facial-recognition-software-image.jpg")
    
        img=img.resize((1000,1000),Image.LANCZOS)
        self.imge=ImageTk.PhotoImage(img)
        

        lebel1=Label(self.root,image=self.imge)
        lebel1.place(x=0,y=0,width=1000,height=1000)



        def connect_to_iriun():
            # Attempt to connect to Iriun Webcam
            try:
                return cv2.VideoCapture(3)
            except cv2.error as e:
                print("Error connecting to Iriun Wi-Fi Webcam:", e)
                return None

        def connect_to_usb_iriun():
            # Attempt to connect to USB webcam (index may vary)
            try:
                return cv2.VideoCapture(3)  # Adjust index as needed
            except cv2.error as e:
                print("Error connecting to Iriun USB Webcam:", e)
                return None

        def connect_to_default_webcam():
            # Attempt to connect to default webcam (0 index)
            try:
                return cv2.VideoCapture(3)
            except cv2.error as e:
                print("Error connecting to default webcam:", e)
                return None

        self.cap = None

        # Attempt to connect to Iriun Wi-Fi Webcam
        self.cap = connect_to_iriun()

        # If connection to Iriun fails, fall back to USB webcam
        if self.cap is None or not self.cap.isOpened():
            print("Connection to Iriun Wi-Fi Webcam failed. Falling back to USB webcam.")
            self.cap = connect_to_usb_iriun()

        # If connection to USB webcam fails, fall back to default webcam
        if self.cap is None or not self.cap.isOpened():
            print("Connection to Iriun USB Webcam failed. Falling back to default webcam.")
            self.cap = connect_to_default_webcam()


        
        lmain =Label(lebel1,bg='red')
        lmain.pack()
        btn_= Button(lebel1, text="Shot", cursor="hand2",command=self.take_shot,font=("Comic Sans MS", 12, "bold"),
                       borderwidth="0",fg="red",bg="yellow")
        btn_.place(x=340, y=550, width=158, height=40)
        btn_2 = Button(lebel1, text="close", cursor="hand2", command=self.close,
                                  font=("Comic Sans MS", 12, "bold"),
                                  borderwidth="0", fg="red", bg="yellow")
        btn_2.place(x=590, y=550, width=158, height=40)
        self.hh=True   
        while True:
            _, frame = self.cap.read()
            self.frame = cv2.flip(frame, 1)
            self.cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            # self.ll=Image.fromarray(cv2image)
            self.imgtk = ImageTk.PhotoImage(Image.fromarray(self.cv2image))

            lmain['image']=self.imgtk
            lmain.update()
            if self.hh== False:
                break
    def close(self):
        self.hh=False
        self.cap.release()
        self.root.destroy()
        cv2.destroyWindows()
    def take_shot(self):

            cv2.imshow('Captured_image',self.frame)
            path=os.getcwd()+"\\ImagesAttendance\\StudentPhoto\\"
            if (os.path.isdir(path)):
                    pat = 'ImagesAttendance/StudentPhoto/{}.{}.jpg'.format(self.sname,self.sid)
                    cv2.imwrite(pat, self.frame)
                    print("true")
            else:        
                os.makedirs(path)
                print("false")
                pat = 'ImagesAttendance/StudentPhoto/{}.{}.jpg'.format(self.sname,self.sid)
                cv2.imwrite(pat, self.frame)


if __name__ == '__main__':
    root=Tk()
    sname='tanmoy'
    sid='455'
    obj=Take(root,sname,sid)
    root.mainloop()
