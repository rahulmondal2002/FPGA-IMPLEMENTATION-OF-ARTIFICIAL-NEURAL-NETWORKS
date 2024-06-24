
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os
 
 
class upload_image:
   def __init__(self,root,sname,sid):

        self.root = root
        self.root.geometry('300x150+600+300')
        # root.eval('tk::PlaceWindow . center')
        self.root.attributes('-topmost',True)
        
        self.root.title("Upload Images")
        self.root.iconbitmap('Image1/my.ico')

        self.sname=sname
        self.sid=sid
        img=Image.open("Image1/gray_background.jpg")
    
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
        path = filedialog.askopenfilename(title='Select Student Image',filetypes=f_types,parent=self.root)
        # print('Selected:', filename)
        if len(path)>0:
          filename=os.path.split(path)[1]
          if len(filename)>20:             
                    self.choose_btn['text']=str(filename[0:15]+'....'+filename[-5:])
          else: self.choose_btn['text']=str(filename)
          self.picture = Image.open(path)       
          #    print(filename)
          # print(str(filename[0:5]+'....'+filename[-5:]))


   def upload_Btn(self):
          
          path=os.getcwd()+"\\ImagesAttendance\\StudentPhoto\\"
          try:
               if (os.path.isdir(path)):
                         pat = 'ImagesAttendance/StudentPhoto/{}.{}.jpg'.format(self.sname,self.sid)
                         picture=self.picture.save(pat) 
                         
                         # print("true")
               else:        
                    os.makedirs(path)
                    # print("false")
                    pat = 'ImagesAttendance/StudentPhoto/{}.{}.jpg'.format(self.sname,self.sid)
                    picture=self.picture.save(pat) 
               self.root.destroy()
               
          except: 
               try:
                    rgb_im = self.picture.convert('RGB')
                    pat = 'ImagesAttendance/StudentPhoto/{}.{}.jpg'.format(self.sname,self.sid)
                    rgb_im.save(pat)
                    self.root.destroy()
               except Exception as e:
                    print(str(e))
                    messagebox.showinfo("Error",f'{str(e)}\n[\'Plese select an Image\'] ',parent=self.root)
if __name__=='__main__':
  root=Tk()
  sid=32
  sname='tanmoy'
  obj=upload_image(root,sname,sid)
  root.mainloop()