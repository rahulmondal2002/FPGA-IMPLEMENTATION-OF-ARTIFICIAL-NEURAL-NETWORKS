
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from sklearn.feature_extraction import image



class GetHelp:
    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x700+180+90")
        self.root.attributes('-topmost',True)
        self.root.title("GetHelp")
        self.root.resizable(0,0)
        self.root.iconbitmap('Image1/my.ico')
        
        img=Image.open("Image1/help2.jpg")
        img=img.resize((150,200),Image.LANCZOS)
        self.imge=ImageTk.PhotoImage(img)

        lebel1=Label(self.root,bg='#BACCE6')
        lebel1.place(x=0,y=0,width=1200,height=700)
        
        nav_lab = Label(lebel1, bg="#E0E0E0")
        nav_lab.place(x=0, y=1,width=1500,height=43)

        im=img.resize((30,20),Image.LANCZOS)
        self.im=ImageTk.PhotoImage(im)
        nav_photo = Label(nav_lab,image= self.im)
        nav_photo.place(x=0, y=3,width=30,height=30)

        txt_lab = Label(nav_lab, text="HelpLine :)", font=("Comic Sans MS", 12 ,"bold"),bg="#E0E0E0", fg="blue", borderwidth=0)
        txt_lab.place(x=31, y=1,width=100,height=35)
        
        

        labe=Label(lebel1,image=self.imge)
        labe.place(x=500,y=250,width=150,height=200)

        txt1_lab = Label(lebel1, text="Contact :", font=("Comic Sans MS", 15,"bold"),bg="#BACCE6", fg="blue")
        txt1_lab.place(x=500, y=475,width=90,height=35)
        
        txt2_lab = Label(lebel1, text="myself.mr.tmaity@gamil.com", font=("Comic Sans MS", 12,"bold"),bg="#BACCE6", fg="Black")
        txt2_lab.place(x=590, y=475,width=300,height=35)
        
if __name__ == '__main__':
    root=Tk()
    obj=GetHelp(root)
    root.mainloop()
