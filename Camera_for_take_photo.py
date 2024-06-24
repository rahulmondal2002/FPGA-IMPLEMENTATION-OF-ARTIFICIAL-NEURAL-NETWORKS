
from tkinter import *

from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import os

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
        cascad=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        

        lebel1=Label(self.root,image=self.imge)
        lebel1.place(x=0,y=0,width=1000,height=1000)

        frameWidth = 500
        frameHeight = 480
        
    # #===========================webcam change==================
    #     def connect_to_iriun():
    # # Attempt to connect to Iriun Wi-Fi Webcam
    #         try:
    #             self.cap = cv2.VideoCapture('http://192.168.137.55:1941/camera')
    #             if self.cap.isOpened():
    #                 print("Connected to Iriun Wi-Fi Webcam successfully.")
    #                 return self.cap
    #             else:
    #                 print("Failed to open Iriun Wi-Fi Webcam.")
    #                 self.cap.release()
    #                 return None
    #         except cv2.error as e:
    #             print("Error connecting to Iriun Wi-Fi Webcam:", e)
    #             return None

        def connect_to_usb_iriun():
            # Attempt to connect to USB webcam (index may vary)
            try:
                self.cap = cv2.VideoCapture(0)  # Adjust index as needed
                if self.cap.isOpened():
                    print("Connected to Iriun USB Webcam successfully.",self.cap)
                    return self.cap
                else:
                    print("Failed to open Iriun USB Webcam.")
                    self.cap.release()
                    return None
            except cv2.error as e:
                print("Error connecting to Iriun USB Webcam:", e)
                return None

        # def connect_to_default_webcam():
        #     # Attempt to connect to default webcam (0 index)
        #     try:
        #         self.cap = cv2.VideoCapture(0)
        #         if self.cap.isOpened():
        #             print("Connected to default webcam successfully.")
        #             return self.cap
        #         else:
        #             print("Failed to open default webcam.")
        #             self.cap.release()
        #             return None
        #     except cv2.error as e:
        #         print("Error connecting to default webcam:", e)
        #         return None

        # Try to connect to Iriun Wi-Fi Webcam
        # self.cap = connect_to_iriun()

        # # If connection to Iriun fails, try to connect to USB webcam
        # if self.cap is None or not self.cap.isOpened():
        #     print("Connection to Iriun Wi-Fi Webcam failed. Attempting to connect to Iriun USB Webcam.")
        self.cap = connect_to_usb_iriun()

        # # If connection to USB webcam fails, fall back to default webcam
        # if self.cap is None or not self.cap.isOpened():
        #     print("Connection to Iriun USB Webcam failed. Falling back to default webcam.")
        #     self.cap = connect_to_default_webcam()




        
        self.cap.set(3, frameWidth)
        self.cap.set(4, frameHeight)
        
        # set brightness, id is 10 and
        # value can be changed accordingly
        self.cap.set(10,100)

        
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
        self.sample_no=0 
        path=os.getcwd()+"\\ImagesAttendance\\StudentPhotos\\SampleOfPhoto\\"
        while True:
            try:
                _, frame = self.cap.read()
                self.frame = cv2.flip(frame, 1)
                gray_frame=cv2.cvtColor(self.frame,cv2.COLOR_BGR2GRAY)

                self.cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
                # self.ll=Image.fromarray(cv2image)

                faces = cascad.detectMultiScale(gray_frame,scaleFactor=1.3,minNeighbors=5,minSize=(100, 100),flags=cv2.CASCADE_SCALE_IMAGE)
                for (x,y,w,h) in faces:
                    face_loca=gray_frame[y:y+h,x:x+w]
                    cv2.rectangle(self.cv2image,(x,y),(x+w,y+h),(0,0,204),2)
                    face_frame=cv2.resize(face_loca,(450,450))
                # face_frame=cv2.cvtColor(face_frame,cv2.COLOR_BGR2GRAY)
                
                self.imgtk = ImageTk.PhotoImage(Image.fromarray(self.cv2image))
                lmain['image']=self.imgtk
                lmain.update()

                if ((self.sample_no>0) and (self.sample_no<=75)):
                # cv2.imshow('Captured_image',self.frame)
                    
                    if (os.path.isdir(path)):
                            pat = 'ImagesAttendance/StudentPhotos/SampleOfPhoto/{}.{}.{}.jpg'.format(self.sname,self.sid,self.sample_no)
                            cv2.imwrite(pat, face_frame)
                            if face_loca is not None: self.sample_no+=1
                            print("true")
                    else:        
                        os.makedirs(path)
                        print("false")
                        pat = 'ImagesAttendance/StudentPhotos/SampleOfPhoto/{}.{}.{}.jpg'.format(self.sname,self.sid,self.sample_no)
                        cv2.imwrite(pat, face_frame)
                        self.sample_no+=1
                if ( self.sample_no==10):
                    pat = 'ImagesAttendance/StudentPhotos/{}.{}.jpg'.format(self.sname,self.sid)
                    cv2.imwrite(pat, self.frame)
                if ((self.hh== False ) or ( self.sample_no==76)):
                    break
            except Exception as e:
                    messagebox.showinfo("Error",f'{str(e)}\n[\'Please sit straight & closer in camera frame\'] ',parent=self.root)
                    self.cap.release()
        self.cap.release()
    def close(self):
        self.hh=False
        
        self.cap.release()
        self.root.destroy()
    def take_shot(self):
        self.sample_no+=1


if __name__ == '__main__':
    root=Tk()
    sname='tanmoy'
    sid='455'
    obj=Take(root,sname,sid)
    root.mainloop()
