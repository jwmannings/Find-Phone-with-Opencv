import cv2
import glob

##LBP Cascade Classifier
#phone_cascade=cv2.CascadeClassifier('phonecascadeLBP25.xml')

##HAAR Cascade Classifier
phone_cascade=cv2.CascadeClassifier('phonecascade30.xml')

img_path="C:/Python27/find_phone/images/"
ii=0
for i in glob.glob(img_path+'*.jpg'):
    img=cv2.imread(i)
    #print i
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    phone=phone_cascade.detectMultiScale(gray,1.3,10)

    for (x, y, w, h) in phone:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cx=float(x+(w/2))
        cy=float(y+(h/2))
        cv2.circle(img,(int(cx),int(cy)),1,(0,0,255),1)

    cx=round(cx/img.shape[1],3)
    cy=round(cy/img.shape[0],3)
    #print(cx,cy)
    line=i+' '+str(cx)+' '+str(cy)+'\n'
    with open('res.txt','a') as f:
        f.write(line)
    cv2.imshow('img', img)
    #cv2.waitKey()
    cv2.imwrite('C:/Python27/find_phone/Results/res'+str(ii)+'.jpg',img)
    ii+=1
    cv2.destroyAllWindows()