import cv2
import numpy
im_g=cv2.imread("5Numpy/102 smallgray.png",0) # 0 means you are reading image gray scale and 1 means reading image in bgr
print(im_g)
cv2.imwrite("newsmallgray.png",im_g)

print(im_g[0:2,2:4])
for i in im_g.flat:
    print(i)

#  stacking and spiliting

ims1=numpy.hstack((im_g,im_g,im_g)) # this will concanate the array in horizontal order
ims2=numpy.vstack((im_g,im_g,im_g)) # this will concanate the array in vertical order
print(ims1,'\n')
print(ims2,'\n')

ims3=numpy.vsplit(ims2,3)  #Split an array into multiple sub-arrays vertically (row-wise).
print(ims3)