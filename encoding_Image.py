from dataclasses import replace
from tkinter import messagebox
import cv2
import face_recognition
import os
from tkinter import *
import numpy as np
from PIL import Image, ImageTk
from tkinter import ttk
import time
 
 
class face_encoder:
   def __init__(self,root,path):

        self.root = root
        self.root.geometry('300x150+600+300')
        
        root.resizable(0,0)
        # root.eval('tk::PlaceWindow . center')
        self.root.attributes('-topmost',True)
        self.root.title("Encoding..")
        self.root.iconbitmap('Image1/my.ico')


        img=Image.open("Image1/video-encoding.jpg")
    
        img=img.resize((300,150),Image.LANCZOS)
        self.imge=ImageTk.PhotoImage(img)
        

        label1=Label(self.root,image=self.imge)
        label1.place(x=0,y=0,width=300,height=150)

        pb = ttk.Progressbar(
            label1,
            orient='horizontal',
            mode='determinate',
            length=280
        )
        pb.place(x=10,y=55,width=280,height=30)
        txt = Label(
            label1,
            text = '0%',
            bg = 'white',
            fg = 'black'
        )
        txt.place(x=130 ,y=95 ,width=45,height=25)
    
        # for i in range(5):
        #     root.update_idletasks()
        #     pb['value'] += 20
        #     time.sleep(1)
        #     txt['text']=pb['value'],'%'
        images = []
        # personNames = []
        sid=[]
        # try:
        myList = os.listdir(path)
        print(myList)
        for i in range(1,len(myList)):
            cur_Img = cv2.imread(f'{path}/{myList[i]}')

            images.append(cur_Img)
            # personNames.append(os.path.splitext(os.path.splitext(cu_i)[0])[0])
            sid.append(int(os.path.split(myList[i])[1].split('.')[1]))
        # print(personNames[:])
        # print(sid[:])
        
            # print(sid[:])
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        if len(images) !=0:
            l=100/len(images)
        #++++++++++++++++++++++++++++++++++++++++++++++++++++
        encodelist=[]
        for i,img in enumerate(images):
            img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            fac_cur_fm=face_recognition.face_locations(img)
            print(sid[i])
            encode=face_recognition.face_encodings(img,fac_cur_fm)[0]
            #----------------for progressbar persentage----------------------
            root.update_idletasks()
            pb['value'] += l
            txt['text']=format(pb['value'],'.2f'),'%'
            #--------------------------------------------------------------------
            encodelist.append(encode)
        #################################################################
        ###############################################################
        # with open("Encoded_Image.txt",'w') as f:
        #     # f.write(str(encodelist))
        #     yaml.dump(encodelist, f, default_flow_style=False)
        # with open("Image_name.txt",'w') as f:
        #     f.write(str(personNames))
        # print(personNames)
        ########################################################
        #####################################################
        np.save('Encode_Images.npy', encodelist)
        # np.save('Student_Name.npy', personNames)
        np.save('Student_ID.npy', sid)
        messagebox.showinfo('System',"Encoding Completed!",parent=self.root)
        self.root.destroy()
    # except Exception as e:
        
    #     messagebox.showinfo("Error",f'{str(e)} ',parent=self.root)
   
if __name__=='__main__':
  root=Tk()
  path=os.getcwd()+"\\ImagesAttendance\\StudentPhotos\\"
  obj=face_encoder(root,path)
  root.mainloop()