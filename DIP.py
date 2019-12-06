import cv2 as cv
import numpy as np
import os
import xlrd

 # Give the location of the file
 loc = ("E:/img/test/annotations_test.xls")

 # To open Workbook
 wb = xlrd.open_workbook(loc)
 sheet = wb.sheet_by_index(0)
 Excelimg =[]
 # For row 0 and column 0
 sheet.cell_value(0, 0)
 for i in range(sheet.nrows):
     if(sheet.cell_value(i, 1)==1):
         Excelimg.append(1)
     else:
         Excelimg.append(0)




location = os.listdir("E:/img/test")
images = []
imagek = []
dataSetresult=[]
countNEG = 0
countPOS = 0
Correctimg = 0

for i in location:
    if(i.endswith("png")):
     images.append(i)
for i in range (len(images)):
   imagek.append(images[i].split('.',1)[0])
   imagek.sort(key=int)
for i in range(len(images)):
 img= cv.imread("E:/img/test/"+imagek[i]+'.png',0)
 img = cv.equalizeHist(img)
 width = img.shape[0]
 height = img.shape[1]
 clahe = cv.createCLAHE(clipLimit=170, tileGridSize=(3, 3))
 cl1 = clahe.apply(img)
 blur = cv.blur(img, (5, 5))
 ret, o = cv.threshold(blur, 175, 255, cv.THRESH_BINARY)
 print(imagek[i])
 kernel = np.ones((3, 3), np.uint8)
 img_ero = cv.erode(o, kernel, iterations=1)
 img_dilation = cv.dilate(img_ero, kernel, iterations=1)
 cv.imshow('Equalized Image', o)
 cv.imshow('ll', img_ero)
 cv.imshow('lle', img_dilation)
 l = []
 for i in range(19):
  for k in range(48):
   img_dilation[k, i] = 0
  pass
 pass
 for i in range(29, 48):
  for k in range(48):
   img_dilation[k, i] = 0
   pass
  pass
 for i in range(width - 1):
  for k in range(height - 1):
   l.append(img_dilation[i, k])
   pass
 pass
 for i in range(48):
  for k in range(40, 48):
   img_dilation[k, i] = 0
   pass
  pass

 # for i in range(1142):
 #  l[i] = 0
 # for i in range(1152, width):
 #  l[i] = 0

 count = 0

 for i in range(len(l)):
  if l[i] == 255:
   count = count + 1

 # print(l)
 for i in range(len(l)):
  if count > 10:
   dataSetresult.append(1)
   break
  else:
   # print("doesnt have virus")
   # countNEG = countNEG + 1
   dataSetresult.append(0)
   break
# print(countPOS)
# print(countNEG)

for i in range(dataSetresult.__len__()):
 if(dataSetresult[i]==Excelimg[i]):
  Correctimg = Correctimg + 1

print("total images number = "+str(dataSetresult.__len__()))
print("correct images number = "+str(Correctimg))
print("the percentage = "+str(Correctimg/dataSetresult.__len__()))

cv.waitKey(10)