##############################################]
#authors : d.aboud / p.alexandre / q.gourier  |
#project : PMI                                |
#date    : 22-jan-23                          |
##############################################]

# imports
import cv2

#specific function for plotting rectangle on demonstration template
def split(file):
    img = cv2.imread(file)
    img = cv2.resize(img, (450,350)) 
    x1, y1, x2, y2 = 45, 250, 110, 318
    a1, b1, a2, b2 = 120, 250, 212, 318
    c1, d1, c2, d2 = 222, 250, 317, 318
    e1, f1, e2, f2 = 325, 250, 420, 318

    g1, h1, g2, h2 = 47, 50, 118, 103
    i1, j1, i2, j2 = 125, 50, 212, 103
    k1, l1, k2, l2 = 220, 50, 312, 103
    m1, n1, m2, n2 = 320, 50, 410, 103

    place1 = (g1, h1, g2, h2)
    place2 = (i1, j1, i2, j2)
    place3 = (k1, l1, k2, l2)
    place4 = (m1, n1, m2, n2)
    place5 = (x1, y1, x2, y2)
    place6 = (a1, b1, a2, b2)
    place7 = (c1, d1, c2, d2)
    place8 = (e1, f1, e2, f2)

    # rectangles coordinates
    rectangles = [place1, place2, place3, place4, place5, place6, place7, place8]

    i = 1
    for x1, y1, x2, y2 in rectangles:
        # drawing rectangles on image
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

        # cropping image around rectangle
        cropped_img = img[y1:y2, x1:x2]

        # saving subfiles
        # cv2.imwrite("lot_{}.png".format(i), cropped_img) #enable for empty lot
        cv2.imwrite("cam_{}.png".format(i), cropped_img) #enable for cam lot
        i += 1