import cv2
# read image
im = cv2.imread('download.jpg')
h,w = im.shape[:2]
print ('Image Read successfully done')
print('width:  ', w)
print('height: ', h)
