# -*- coding: utf-8 -*-
#author：leehongbo
#STU-ID:2017311020115
import cv2
import face_recognition
video_capture = cv2.VideoCapture(0)
#苦力读取脸图片
ftl_image = face_recognition.load_image_file("C:/2.jpg")
ftl_face_encoding = face_recognition.face_encodings(ftl_image)[0]
wqm_image = face_recognition.load_image_file("C:/1.jpg")
wqm_face_encoding = face_recognition.face_encodings(wqm_image)[0]
#定义名字对应照片
nam = ['unknown','ftl','hw','hw','zym','ch','hs','sy','lee']
#人脸库
library_face_encodings = (ftl_face_encoding, wqm_face_encoding)
with open("D:/1.txt",'w') as f:
    i = 0
    for library_face_encoding in library_face_encodings:
        f.write(str(library_face_encoding))
        f.write('\r\n')
#初始化参数值
face_locations = []
face_encodings = []
face_names = []
process_this_frame = 0
name = 'unknow'
while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    #找到face位置
    face_locations = face_recognition.face_locations(small_frame)
    #投机取巧的处理视频帧
    if (process_this_frame % 3) == 0:
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            results = []
            #比对
            for library_face_encoding in library_face_encodings:
                match = face_recognition.compare_faces([library_face_encoding], face_encoding, tolerance=0.4)
                results.append(match[0])
            i = na_before = result_before = na = lis = 0
            #比对结果处理
            for result in results:
                na = result * (i+1) + na_before
                na_before = na
                lis= result + result_before
                result_before = lis
                i+=1
            print(results,lis,na)
            #去除误差结果
            if lis < 2:
                print(lis,na)
                name = nam[na]
            face_names.append(name)
            
    process_this_frame += 1
    
    if process_this_frame > pow(100,100):
        process_this_frame = 0

    # 显示结果
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
    
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
