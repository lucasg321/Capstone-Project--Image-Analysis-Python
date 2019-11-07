import numpy as np
import cv2

image = cv2.imread('droneviewoffarmland.jpg') #load the image that the analysis should be done on
original = image.copy()
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #change the image to type HSV for better results in opencv
lower = np.array([18, 240, 250], dtype="uint8") #declare the lower range of the shade to test for
upper = np.array([20, 255, 255], dtype="uint8") #declare the upper range of the shade to test for

mask = cv2.inRange(image, lower, upper) #inRange function turns all pixels in the image in the defined range to black

cv2.imshow('original', original) #show image
cv2.imshow('mask', mask) # show new masked image

image[mask>0]=(0,0,255)  #turns all the previously black pixels into red

cv2.imshow("result.png",image) # shows the new image with red in it

#cv2.waitKey()

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower1 = np.array([10, 0, 0])
upper1 = np.array([20, 255, 255])

mask=cv2.inRange(hsv,lower1,upper1)

cv2.imshow('original', original)
cv2.imshow('mask', mask)

image[mask>0]=(0,0,255)

cv2.imshow("result2.png",image)

cv2.waitKey()

#brown_mask = cv2.inRange(hsv, lower, upper)

#(contours,_) = cv2.findContours(brown_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#for contour in contours:
#    area = cv2.contourArea(contour)

#    if(area > 800):
#        x,y,w,h = cv2.boundingRect(contour)
#        image = cv2.rectangle(image, (x,y),(x+w,y+h),(0,0,255),10)
#        cv2.imshow('tracking', image)
#        k=cv2.waitKey(5) & 0xFF
#        if k == 27:
#            break

#cv2.destroyAllWindows()


#points= cv2.findnonzero(mask)

#avg = np.mean(points, axis=0)

#print(avg)

#resimage = [640, 480]
#resscreen = [1920, 1080]

## points are in x,y coordinates
#pointinscreen = ((resscreen[0] / resimage[0]) * avg[0], (resscreen[1] / resimage[1]) * avg[1] )


#kernel = cv2.getstructuringelement(cv2.morph_rect, (3,3))
#opening = cv2.morphologyex(mask, cv2.morph_open, kernel, iterations=1)

#cnts = cv2.findcontours(opening, cv2.retr_external, cv2.chain_approx_simple)
#cnts = cnts[0] if len(cnts) == 2 else cnts[1]

#area = 0
#for c in cnts:
#    area += cv2.contourarea(c)
#    cv2.drawcontours(original,[c], 0, (0,0,0), 2)

#aftermask = np.where(mask == 255)

#listi = []    #---stores coordinate corresponding to height of the image
#listj = []    #---stores coordinate corresponding to width of the image

#for i in range(0, mask.shape[0]):
#    for j in range(0, mask.shape[1]):
#        if(mask[i, j] == 255):
#            listi = np.append(listi, i)
#            listj = np.append(listj, j)
#            #print(listi, listj)


#coord = cv2.findnonzero(mask)
##cv2.circle(mask,coord, 5, (0,255,0), -1)
#print(coord)
#coord = 255;
#print(np.transpose(mask.nonzero()))

#print(aftermask)
#coordinates = zip(aftermask[0], aftermask[1])
#print (coordinates)
#np.asarray(coordinates)
#print(coordinates)

#print(area)
#cv2.imshow('mask', mask)
#cv2.imshow('original', original)
#cv2.imshow('opening', opening)
#cv2.waitkey()