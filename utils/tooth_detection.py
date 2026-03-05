# tooth detection logic
import cv2

def detect_teeth(mask):

    contours,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    teeth_boxes=[]

    for c in contours:

        x,y,w,h = cv2.boundingRect(c)

        if w*h>500:

            teeth_boxes.append((x,y,w,h))

    return teeth_boxes
