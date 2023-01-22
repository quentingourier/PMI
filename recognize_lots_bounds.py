##############################################]
#authors : d.aboud / p.alexandre / q.gourier  |
#project : PMI                                |
#date    : 22-jan-23                          |
##############################################]

# imports
import cv2
import numpy as np

# image processing
img = cv2.imread("temp\\sub_example0.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #apply gray filter
gray = cv2.GaussianBlur(gray, (5, 5), 0) #gaussian blur to reduce noise
edges = cv2.Canny(gray, 50, 150) #cany edge detection
lines = cv2.HoughLinesP(edges, 1, np.pi/180, 50, minLineLength=50, maxLineGap=5) #find lines

# image modifications
rects = []
for line in lines:
    x1, y1, x2, y2 = line[0]
    rects.append([x1,y1,x2,y2]) #create list of rectangle corners coordinates

for rect in rects:
    x1, y1, x2, y2 = rect[0], rect[1], rect[2], rect[3]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2) #draw rectangles on image

# output results
cv2.imshow("Parking Lots", img)
cv2.waitKey(0)
cv2.destroyAllWindows()