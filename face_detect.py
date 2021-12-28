
import cv2
import os
def face_cut(img):
    face_cascade = cv2.CascadeClassifier(r'C:\Users\chicony\anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
    # 轉成灰階圖片
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 偵測臉部
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.08,minNeighbors=10,minSize=(32, 32))
    #裁減
    
    (x, y, w, h)=faces[0]
    print (x, y, w, h)
    d1=20
    d2=20
    if y<d1:
        d1=y
    if x<d2:
        d2=x
    print(d1,d2)
    img = img[y-d1:y+h+d1, x-d2:x+w+d2]
    return img
def mult_face_cut(input_path,local_path):
    imgnamelist=os.listdir(input_path)
    for i in imgnamelist:
        try:
            img = cv2.imread("{}\{}".format(input_path,i))
            print("{}\{}".format(input_path,i))
            img=face_cut(img)
            print("{}\cut_{}".format(local_path,i))
            cv2.imwrite( "{}\cut_{}".format(local_path,i), img )
        except:
            print('img_no_people')



