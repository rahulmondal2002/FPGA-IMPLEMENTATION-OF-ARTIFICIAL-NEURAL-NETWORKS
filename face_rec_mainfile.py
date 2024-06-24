import cv2
import numpy as np
import face_recognition
import os
import yaml

class face_rec_main:
    def __init__(self):
    
        # with open("Encoded_Image.txt") as f:
        #     encodelk = yaml.load(f)	

        # dataset_faces_name = list(all_face_encodings.keys())
        # dataset_faces      = np.array(list(all_face_encodings.values()))
            # lk= f.read()
            # encodelk= lk.replace("\n", "")
            # # encodelk= list(encodelk)
        # with open("Image_name.txt") as f:
        #     personNames= f.read()
            # personNames= list(personNames)
        encodelk = np.load("face_repr.npy")
        personNames = np.load("labels.npy")
        print("All Encodings Complete!!!")
        # print(encodelk[:])
        # print(personNames[:])

        cap= cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            faces = cv2.resize(frame,(0, 0), None, 0.25, 0.25)
            faces= cv2.cvtColor(faces,cv2.COLOR_BGR2RGB)

            fac_cur_fm=face_recognition.face_locations(faces)
            encod_cur_fm= face_recognition.face_encodings(faces,fac_cur_fm)

            for encodeFace, faceLoc in zip(encod_cur_fm,fac_cur_fm):
                face_matches=face_recognition.compare_faces(encodelk,encodeFace)
                face_dis=face_recognition.face_distance(encodelk, encodeFace)
                name = "Unknown"
                match_index= np.argmin(face_dis)

                if face_matches[match_index]:
                    name=personNames[match_index].upper()
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
                cv2.putText(frame, name, (x2 + 41, y1 +16), cv2.FONT_HERSHEY_COMPLEX, 0.50, (255,255,255), 2)
                # fancyDraw(frame,faceLoc)
            cv2.imshow('camp',frame)
            if cv2.waitKey(10)== 13:
                break
        cap.release()
        cv2.destroyAllWindows()

if __name__=="__main__":
   
   obj=face_rec_main()


