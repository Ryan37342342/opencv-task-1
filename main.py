# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import math
import glob
import os
import numpy as np

def main ():

    # jpg file in dir
    for label_path in sorted(glob.glob("cracking/labels/*.txt")):
        # create path to image
        image_name = label_path.split("/")[-1]
        image_path = "cracking/images/" + image_name.removesuffix(".txt") +".jpg"
        if os.path.isfile(image_path):
            print(label_path)
            # read in label
            with open(label_path, "r") as label_file:
                labels = label_file.readlines()
                
            for label in labels:
                image = cv2.imread(image_path)
                image_height,image_width,colour = image.shape
                label = label.split(" ")
                print(label[0])
                # cv2.imshow("test",image)
                # cv2.waitKey()
           
             #image = image[y1:y2, x1:x2]
            
            # class_name = "cracking"
            # resized = cv2.resize(image,(300,300),interpolation = cv2.INTER_AREA)
            # cv2.imshow("0 "+ class_name, resized)
            
            
                
            # gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
            
            # # cv2.imshow("1 "+ class_name, src)
            # # cv2.waitKey()
            # # contrast the image
            # adjusted = cv2.convertScaleAbs(gray, alpha=4, beta=2) 
            # src = cv2.bilateralFilter(adjusted,9,75,75) 
            # cv2.imshow("1 "+ class_name, adjusted)

            # cv2.imshow("2 "+ class_name, src)
            
            

            # edges = cv2.Canny(adjusted,50, 100,3)

            # cv2.imshow("3 "+ class_name, edges)
            
            
            # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7,7))
            # opening = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
            # cv2.imshow("d "+ class_name, opening)

            # # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
            # # opening = cv2.morphologyEx(opening, cv2.MORPH_ERODE, kernel)
            # # cv2.imshow("e "+ class_name, opening)
                
            
            # # Apply HoughLinesP method to
            # #  directly obtain line end points
            # lines = cv2.HoughLinesP(opening, # Input edge image
            #         1, # Distance resolution in pixels
            #         np.pi/180, # Angle resolution in radians
            #         threshold=50, # Min number of votes for valid line
            #         minLineLength=50, # Min allowed length of line

            #         maxLineGap=2 # Max allowed gap bet
            #                         )
            # lines_list= list()
            # dist =0
            
            # # Iterate over points
            # if lines is not None:
            #     print("lines found")
            #     for points in lines:
            #         # Extracted points nested in the list
            #         x1, y1, x2, y2 = points[0]
            #         # Draw the lines join the points
            #         # On the original image
            #         cv2.line(resized, (x1, y1), (x2, y2), (0, 255, 0), 2)
            #         # Maintain a simples lookup list for points
            #         lines_list.append([(x1, y1), (x2, y2)])
            #         dist = dist + (x2-x1 + y2-y1)
            
                
            #     cv2.imshow("4 "+ class_name, resized)
            #     cv2.waitKey()
            #     print("total pixels:", dist)
            
            # print("No lines found for",filename)

if __name__ == '__main__':
    # read a cracked sample image
    main()

