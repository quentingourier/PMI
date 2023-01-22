##############################################]
#authors : d.aboud / p.alexandre / q.gourier  |
#project : PMI                                |
#date    : 22-jan-23                          |
##############################################]

# imports
import cv2, os
import numpy as np
import update_database

def isavailable(file):

    # setting files variables
    id = file.split('.')[0].split('_')[1] #isolate id of cam picture
    ref_pathfile = "lot_"+str(id)+".png" #take lot reference picture according to id
    reference_image = cv2.imread(os.getcwd()+"\\"+ref_pathfile)
    # reference_image = cv2.resize(reference_image, (450,350)) #resizing the ref picture if too large
    gray_reference = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY) #apply gray filter
    current_image = cv2.imread(os.getcwd()+"\\"+file)
    # current_image = cv2.resize(current_image, (reference_image.shape[1], reference_image.shape[0])) #resizing to the ref picture size
    gray_current = cv2.cvtColor(current_image, cv2.COLOR_BGR2GRAY) #apply gray filter

    # images processing
    difference = cv2.absdiff(gray_reference, gray_current) #get abs diff between gray pics
    threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1] #tol value
    kernel = np.ones((5,5),np.uint8)
    threshold = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel) # apply morphology to delete noise
    threshold = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel)

    # detect difference pixels 
    contours = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    # output results
    if len(contours) != 0:
        # Draw rectangle around the detected difference
        for contour in contours:
            if cv2.contourArea(contour) > 1000:
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(current_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
                print("Place n°",id,": occupée")
                return 1
            else:
                print("Place n°",id,": libre")
                return 0
    else:
        print("Place n°",id,": libre")
        return 0

    # cv2.imshow("lot", reference_image)  #enable to display cam and lot pictures
    # cv2.moveWindow("lot", 40,150)
    # cv2.imshow("lot detection", current_image)
    # cv2.moveWindow("lot detection", 500,150)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

def main():
    status_list = []
    print("\nreal time status")
    print("----------------")
    for i in range(1,9):
        id_cam = i
        file = "cam_"+str(id_cam)+".png"
        status_list.append(isavailable(file))
    # update_database.insert(status_list) #enable for initialization
    update_database.update_status(status_list) #enable for update
    print("----------------\nupdate done!")