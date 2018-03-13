# Find-Phone-with-Opencv

The task is to identify the phone from the given image

![alt_text](https://github.com/raj-shah14/Find-Phone-with-Opencv/blob/master/images/1.jpg)

## Training Classifier
Use  `train_phone.py` to first crop the object from the image based on the `labels.txt` provided in the images folder.
Give the correct path
`
path="C:/Python27/find_phone/images\\"`
`pathsave="C:/Python27/find_phone/pos_img\\"` at line 8 and 9 of the file.

`getdata` function combines the text file and images and returns an array,which is passed to the function `crop_save`.

Crop Images

![alt_text](https://github.com/raj-shah14/Find-Phone-with-Opencv/blob/master/Pos_img/crop_img10.jpg) ![alt_text](https://github.com/raj-shah14/Find-Phone-with-Opencv/blob/master/Pos_img/crop_img1.jpg) ![alt_text](https://github.com/raj-shah14/Find-Phone-with-Opencv/blob/master/Pos_img/crop_img11.jpg) ![alt_text](https://github.com/raj-shah14/Find-Phone-with-Opencv/blob/master/Pos_img/crop_img13.jpg) ![alt_text](https://github.com/raj-shah14/Find-Phone-with-Opencv/blob/master/Pos_img/crop_img14.jpg) ![alt_text](https://github.com/raj-shah14/Find-Phone-with-Opencv/blob/master/Pos_img/crop_img15.jpg) ![alt_text](https://github.com/raj-shah14/Find-Phone-with-Opencv/blob/master/Pos_img/crop_img16.jpg) ![alt_text](https://github.com/raj-shah14/Find-Phone-with-Opencv/blob/master/Pos_img/crop_img19.jpg) ![alt_text](https://github.com/raj-shah14/Find-Phone-with-Opencv/blob/master/Pos_img/crop_img21.jpg)

Using `makefile` function create `info.dat` file for positive images and `bg.txt` for negative images.
Once that is done using `train` function start classifier training

Use `train('LBP')` for Local Binary Patterns(LBP) classifier,
Use `train('HAAR')` for HAAR classifier

First it generates a `positives.vec` file and then begins training.

## Prediction

The `cascade.xml` file will get created in data folder which is used for prediction in `find_phone.py` 

The results of the x,y cordinates of a phone in an image are stored in the `res.txt` file. The cordinates are normalized.

### Results
![alt_text](https://github.com/raj-shah14/Find-Phone-with-Opencv/blob/master/res1.jpg)

### Other Resutls
![alt_text](https://github.com/raj-shah14/Find-Phone-with-Opencv/blob/master/res2.jpg)
![alt_text](https://github.com/raj-shah14/Find-Phone-with-Opencv/blob/master/res0.jpg)
![alt_text](https://github.com/raj-shah14/Find-Phone-with-Opencv/blob/master/res56.jpg)
![alt_text](https://github.com/raj-shah14/Find-Phone-with-Opencv/blob/master/res62.jpg)


