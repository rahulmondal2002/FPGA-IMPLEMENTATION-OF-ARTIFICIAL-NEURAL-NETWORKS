import os
from tkinter import messagebox, Tk, Label
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import numpy as np  # Import numpy module

class face_encoder:
    def __init__(self, root, path):
        self.root = root
        self.root.geometry('300x150+600+300')
        self.root.resizable(0,0)
        self.root.attributes('-topmost', True)
        self.root.title("Encoding..")
        self.root.iconbitmap('Image1/my.ico')

        img = Image.open("Image1/video-encoding.jpg")
        img = img.resize((300, 150), Image.LANCZOS)
        self.imge = ImageTk.PhotoImage(img)

        label1 = Label(self.root, image=self.imge)
        label1.place(x=0, y=0, width=300, height=150)

        cascad = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        lbph = cv2.face.LBPHFaceRecognizer_create()  # Corrected line

        pb = ttk.Progressbar(
            label1, orient='horizontal', mode='determinate', length=280
        )
        pb.place(x=10, y=55, width=280, height=30)

        txt = Label(
            label1,
            text='0%',
            bg='white',
            fg='black'
        )
        txt.place(x=130, y=95, width=45, height=25)

        images = []
        sid = []

        try:
            myList = os.listdir(path)
            if len(myList) != 0:
                l = 100 / len(myList)

            for cu_i in myList:
                cur_Img = Image.open(f'{path}/{cu_i}').convert('L')
                np_img = np.array(cur_Img, 'uint8')
                face = cascad.detectMultiScale(np_img)

                for (x, y, w, h) in face:
                    images.append(np_img[y:y + h, x:x + w])
                    sid.append(int(os.path.split(cu_i)[1].split('.')[1]))

                root.update_idletasks()
                pb['value'] += l
                txt['text'] = format(pb['value'], '.2f'), '%'

            lbph.train(images, np.array(sid))  # Corrected line
            lbph.write('encoding_data.yml')  # Corrected line

            messagebox.showinfo('System', "Encoding Completed!", parent=self.root)
            self.root.destroy()
            cv2.destroyAllWindows()
        
        except Exception as e:
            messagebox.showinfo("Error", f'{str(e)} ', parent=self.root)
            self.root.destroy()
            cv2.destroyAllWindows()

if __name__ == '__main__':
    root = Tk()
    path = os.getcwd() + "\\ImagesAttendance\\StudentPhotos\\SampleOfPhoto\\"
    obj = face_encoder(root, path)
    root.mainloop()
