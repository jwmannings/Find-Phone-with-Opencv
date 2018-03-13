import cv2
import glob
import os
import numpy as np
import time
data=open('C:/Python27/find_phone/images/labels.txt','r')

path="C:/Python27/find_phone/images\\"
pathsave="C:/Python27/find_phone/pos_img\\"

def getdata(path):
    imagespath=[]
    for i in glob.glob(path+'*.jpg'):
        imagespath.append(i.split('\\'))
    datapath=[]
    for i in data:
        datapath.append( i.strip().split(' '))
    #print datapath
    img_name=[]
    for i in imagespath:
        img_name.append(i[1])

    fulldata=[]
    for i in datapath:
        if i[0] in img_name:
            fulldata.append((path+i[0],i[1],i[2]))
    #print(fulldata)
    return fulldata

def crop_save(fulldata):
    ii=0
    for i in fulldata:
        image=cv2.imread(i[0])
        x,y=(int(float(i[1])*image.shape[1]),int(float(i[2])*image.shape[0]))
        radius=22
        #cv2.circle(image,(x,y),1,(0,0,255),1,-1)
        #cv2.rectangle(image,(x-radius,y-radius),(x+radius,y+radius),(0,255,0),1)
        cv2.imshow('test',image)
        crop_img=image[y-radius:y+radius,x-radius:x+radius]
        crop_img=cv2.resize(crop_img,(50,50))
        cv2.imshow('crop',crop_img)
        cv2.imwrite(pathsave+'crop_img'+str(ii)+'.jpg',crop_img)
        cv2.waitKey()
        ii=ii+1
        cv2.destroyAllWindows()

def makefile(ftype):
    for filetype in [ftype]:
        if filetype == 'neg_img':
            for img in os.listdir(filetype):
                line=filetype+'\\'+img+'\n'#' 1 0 0 50 50\n'
                with open('bg.txt','a') as f:
                    f.write(line)
        elif filetype=='pos_img':
            for img in os.listdir(filetype):
                line = filetype + '\\' + img +' 1 0 0 50 50\n'
                with open('info.dat', 'a') as f:
                    f.write(line)

def train(featuretype):
    os.system('opencv_createsamples -info info.dat -num 100 -w 25 -h 25 -vec positives.vec')
    time.sleep(1)
    os.system('opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 100 -numNeg 200 -numStages 30 -w 25 -h 25 -featureType '+featuretype)

#fulldata=getdata(path)
#crop_save(fulldata)        #To crop the object and save as positive
#makefile('pos_img')        #To make positive info file and negative bg.txt file
train('LBP')               #To train our classifier