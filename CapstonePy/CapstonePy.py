import numpy as np
import cv2
import logging 
np.seterr(divide='ignore', invalid='ignore')  
#Create and configure logger 
logging.basicConfig(filename="newfile.log", 
                    format='%(asctime)s %(message)s', 
                    filemode='w') 
  
#Creating an object 
logger=logging.getLogger() 
  
#Setting the threshold of logger to DEBUG 
logger.setLevel(logging.DEBUG) 

image = cv2.imread('Images/Uw2-91s.jpg') #load the image that the analysis should be done on

#BGR value extraction taking the average pixel values from an image
rgbExtraction1 = cv2.imread('Images/light-soilbin.jpg'); #27.23628093 47.27746177 66.95177992 - 91 [60.63844851 54.92196398 78.35154687]
avg_color_per_row = np.average(rgbExtraction1, axis=0)    #64.52385635 104.4465545  132.43190441 - 41
avg_color = np.average(avg_color_per_row, axis=0)
print(avg_color)
#another way to do the same thing - extract rgb values and average over the array/image
#array = ([[[ 0.,  0.,  0.],
#        [ 0.,  0.,  0.]],

#       [[ 1.,  1.,  1.],
#        [ 1.,  1.,  1.]]])

#avg = np.mean(array, axis=(0, 1))
#print(avg)

#finding 20x20 blocks of pixels that average to a specific rgb value and changing those pixels to red
rows,cols,channels = image.shape;
i=0
j=0
rgbExtraction = cv2.imread('Images/soilbin.jpg');
rgbMask = cv2.imread('Images/soilbin.jpg'); 
while(i<899):
    j=0;
    while(j<642):
        try:
            #with warnings.catch_warnings():
                #warnings.simplefilter("ignore", category=RuntimeWarning)
                avg_color_per_row = np.average(rgbExtraction[i:i+100,j:j+100], axis=0)  
                avg_color = np.average(avg_color_per_row, axis=0)
        except:
            logger.info('Got exception on main handler')
        
        #check if matches uw2-42 avg rgb color
        if (avg_color[0] >= 64 and avg_color[1] >= 104 and avg_color[2] >= 132) and (avg_color[0] <= 66 and avg_color[1] <= 106 and avg_color[2] <= 134):
            try:
                print(avg_color)
                rgbMask[i:i+100,j:j+100] = rgbMask[i:i+100,j:j+100] + [0, 0, 122]
            except:
                logger.info('Got exception on main handler')
            #rgbMask[i:i+20,i:i+20] = rgbMask[i:i+20,i:i+20] + [0, 0, 255]
            #i += 100
        #check if matches uw2-42 avg rgb color
        if (avg_color[0] >= 61 and avg_color[1] >= 101 and avg_color[2] >= 128) and (avg_color[0] <= 63 and avg_color[1] <= 103 and avg_color[2] <= 131):
            try:
                print(avg_color)
                rgbMask[i:i+100,j:j+100] = rgbMask[i:i+100,j:j+100] + [0, 0, 122]
            except:
                logger.info('Got exception on main handler')
            #rgbMask[i:i+20,i:i+20] = rgbMask[i:i+20,i:i+20] + [0, 0, 200]
            #i += 100
        if (avg_color[0] >= 18 and avg_color[1] >= 19 and avg_color[2] >= 30) and (avg_color[0] <= 20 and avg_color[1] <= 21 and avg_color[2] <= 33):
            try:
                print(avg_color)
                rgbMask[i:i+100,j:j+100] = rgbMask[i:i+100,j:j+100] + [0, 0, 122]
            except:
                logger.info('Got exception on main handler')
                #[60.63844851 54.92196398 78.35154687]
        if (avg_color[0] >= 59 and avg_color[1] >= 53 and avg_color[2] >= 77) and (avg_color[0] <= 61 and avg_color[1] <= 56 and avg_color[2] <= 79):
            try:
                print(avg_color)
                rgbMask[i:i+100,j:j+100] = rgbMask[i:i+100,j:j+100] + [0, 0, 122]
            except:
                logger.info('Got exception on main handler')
               # 34.21031746 48.14484127 69.65065193
        if (avg_color[0] >= 32 and avg_color[1] >= 47 and avg_color[2] >= 68) and (avg_color[0] <= 35 and avg_color[1] <= 50 and avg_color[2] <= 71):
            try:
                print(avg_color)
                rgbMask[i:i+100,j:j+100] = rgbMask[i:i+100,j:j+100] + [0, 0, 122]
            except:
                logger.info('Got exception on main handler')
            #rgbMask[i:i+20,i:i+20] = rgbMask[i:i+20,i:i+20] + [0, 0, 200]
            #i += 100
        #if (avg_color[0] >= 0 and avg_color[1] >= 0 and avg_color[2] >= 0) and (avg_color[0] <= 255 and avg_color[1] <= 255 and avg_color[2] <= 255):
        #    print(avg_color)
        #    rgbMask[i:i+100,j:j+100] = rgbMask[i:i+100,j:j+100] + [0, 0, 122]
        #    #rgbMask[i:i+20,i:i+20] = rgbMask[i:i+20,i:i+20] + [0, 0, 200]
        #    #i += 100
        j+=1
    i += 1;
cv2.imshow('Select Mask', rgbMask)

cv2.waitKey()
