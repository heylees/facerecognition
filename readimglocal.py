# -*- coding: utf-8 -*-
import cv2
import face_recognition
import os
library_face_encodings = []
nam = ['unknown']
zz = 0
for filename in os.listdir(r'C:/pic'):
    file = 'C:/' + filename
    image = face_recognition.load_image_file(file)
    lib_face_encoding = face_recognition.face_encodings(image)[0]
    library_face_encodings.append(lib_face_encoding)
    nam.append(filename[:-4])
with open('D:/data.txt','w') as f:
    for library_face_encoding in library_face_encodings:
        f.write(nam[zz]+ ' ')
        zz+= 1
        for i in range(128):
            f.write(str(int(library_face_encoding[i])))
            f.write(' ')
        f.write('\r\n')