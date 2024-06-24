
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
import cv2
from matplotlib.pyplot import gray
from numpy import empty
from scipy.misc import face
 
 
class upload_image:
   def __init__(self,root,sname,sid):

        self.root = root
        self.root.geometry('300x150+600+300')
        # root.eval('tk::PlaceWindow . center')
        self.root.attributes('-topmost',True)
        self.root.resizable(0,0)
        self.root.title("Upload Images")
        self.root.iconbitmap('Image1/my.ico')

        self.sname=sname
        self.sid=sid
        img=Image.open("Image1/gray_background.jpg")
        self.cascad=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
        img=img.resize((300,150),Image.LANCZOS)
        self.imge=ImageTk.PhotoImage(img)
        

        label1=Label(self.root,image=self.imge)
        label1.place(x=0,y=0,width=300,height=150)

        grid_label=Label(label1,bg='red')
        grid_label.place(x=20,y=40,width=260,height=30)

        brow_btn=Button(grid_label,text='Browser',anchor=NW,command=self.UploadAction)
        brow_btn.place(x=1,y=1,width=53,height=25)
        self.choose_btn=Button(grid_label,text='Choose..',anchor=NW,command=self.UploadAction,bg='white',state=DISABLED)
        self.choose_btn.place(x=53,y=1,width=203,height=25)
#  corner_radius=10
        upload_btn=Button(label1,text='Upload',command=self.upload_Btn)
        upload_btn.place(x=90,y=100,width=130,height=30)
     #    print(os.getcwd())

   def UploadAction(self):
        f_types = [('Jpg Files', '*.jpg')]
        path = filedialog.askopenfilename(title='Select Student Image To Upload',filetypes=f_types,parent=self.root)
        # print('Selected:', filename)
        if len(path)>0:
          filename=os.path.split(path)[1]
          if len(filename)>20:             
                    self.choose_btn['text']=str(filename[0:15]+'....'+filename[-5:])
          else: self.choose_btn['text']=str(filename)
          self.orginal_pic = Image.open(path)
          hll= cv2.imread(path) 
          self.pict = cv2.resize(hll, (520, 600))
          #    print(filename)
          # print(str(filename[0:5]+'....'+filename[-5:]))


   def upload_Btn(self):
     sample_no=1
     # rgb_frame=cv2.cvtColor(self.pict,cv2.COLOR_BGR2RGB)
     gray_frame=cv2.cvtColor(self.pict,cv2.COLOR_BGR2GRAY)
     cv2.imshow('kdjkf',gray_frame)
     faces = self.cascad.detectMultiScale(gray_frame,scaleFactor=1.3,minNeighbors=5)
     print(faces)
     try:
          for (x,y,w,h) in faces:
               face_loca=gray_frame[y:y+h,x:x+w]   
          picture=cv2.resize(face_loca,(450,450))
     except Exception as e:
           messagebox.showinfo("Error",f'{str(e)}\n[\'Plese select a straight Image\'] ',parent=self.root)
     if len(faces)!=0:
          # picture=cv2.cvtColor(picture,cv2.COLOR_BGR2GRAY)
          path=os.getcwd()+"\\ImagesAttendance\\StudentPhotos\\SampleOfPhoto\\"
          while  sample_no<=30:
               try:
                    if (os.path.isdir(path)):
                              pat = 'ImagesAttendance/StudentPhotos/SampleOfPhoto/{}.{}.{}.jpg'.format(self.sname,self.sid,sample_no)
                              
                              cv2.imwrite(pat,    picture) 
                              
                              # print("true")
                    else:        
                         os.makedirs(path)
                         # print("false")
                         pat = 'ImagesAttendance/StudentPhotos/SampleOfPhoto/{}.{}.{}.jpg'.format(self.sname,self.sid,sample_no)
                         
                         cv2.imwrite(pat,    picture) 
                    
               except Exception as e:
                         print(str(e))
                         messagebox.showinfo("Error",f'{str(e)}\n[\'Plese select a straight Image\'] ',parent=self.root)
                         break
               sample_no+=1
               if ( sample_no==10):
                    try:
                         pat = 'ImagesAttendance/StudentPhotos/{}.{}.jpg'.format(self.sname,self.sid)
                         pic=self.orginal_pic.save(pat)
                    except:
                         try:
                              rgb_im = self.orginal_pic.convert('RGB')
                              pat = 'ImagesAttendance/StudentPhotos/{}.{}.jpg'.format(self.sname,self.sid)
                              rgb_im.save(pat)
                              
                         except Exception as e:
                              # print(str(e))
                              messagebox.showinfo("Error",f'{str(e)}\n[\'Plese select a straight Image\'] ',parent=self.root)
          self.root.destroy()
if __name__=='__main__':
  root=Tk()
  sid=32
  sname='tanmoy'
  obj=upload_image(root,sname,sid)
  root.mainloop()