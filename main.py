# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import math
import glob
import os
import numpy as np
import re


def findClassname(classname):
    
    if classname == "0":
        classname ="Longitudinal_Cracking"
    elif classname == "1":
        classname ="Crocodile_Cracking"
    elif classname == "2":
        classname ="Pumping_Cracking"
    elif classname == "3":
        classname ="Transverse_Cracking"
    else:
        classname = "Block_Cracking"
    
    return classname

def main ():

    # jpg file in dir
    for label_path in sorted(glob.glob("cracking/labels/*.txt")):
        # create path to image
        image_name = label_path.split("/")[-1]
        image_path = "cracking/images/" + image_name.removesuffix(".txt") +".jpg"

        if os.path.isfile(image_path):
            # read in label
            with open(label_path, "r") as label_file:
                labels = label_file.readlines()
                
            for label in labels:
                org_image = cv2.imread(image_path)
                image_height,image_width,colour = org_image.shape
                #print(image_height)
                label_spilt = re.split("\s+",label)
                class_name = label_spilt[0]
                class_name = findClassname(class_name)
                if class_name == "Longitudinal_Cracking":

                    centerX = float(label_spilt[1])
                    centerY = float(label_spilt[2])
                    w = float(label_spilt[3]) 
                    h = float(label_spilt[4])  
                    ox1 = (centerX - w/2) * image_width
                    ox2 = (centerX + w/2) * image_width
                    oy1 = (centerY - h/2) * image_height
                    oy2 = (centerY + h/2) * image_height
                   
                    image = org_image[int(oy1):int(oy2), int(ox1):int(ox2)] 
                    cv2.imshow("Org", image)
                    
                    # double image size
                    width = int(image.shape[1] * 200 / 100)
                    height = int(image.shape[0] * 200 / 100)
                  
                    resized = cv2.resize(image,(width,height),interpolation = cv2.INTER_LINEAR)
                   
                    
                    # turn image gray    
                    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
                    cv2.imshow("test ",gray)

                    # compute gamma = log(mid*255)/log(mean)
                    mid = 0.9
                    mean = np.mean(gray)
                    gamma = math.log(mid*255)/math.log(mean)
                   

                    # do gamma correction
                    gamma = np.power(gray, gamma).clip(0,255).astype(np.uint8)

                    # noise removal and edge preservation
                    blur = cv2.bilateralFilter(gamma,9,150,150) 
                    cv2.imshow("test0 ",gamma)
                 
                   
                    
                    # detect edges
                    edges = cv2.Canny(blur,50, 100,3)
                    cv2.imshow("test3 ",edges)
                   
                    # fill gaps
                    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10,10))
                    opening = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel) 
                    cv2.imshow("tes4 ",opening)

                   # compact blobls
                    thinned = cv2.ximgproc.thinning(opening)
                    cv2.imshow("tes54 ",thinned)
                    cv2.waitKey()
                 
                    
                    # Apply HoughLinesP method to
                    #  directly obtain line end points
                    lines = cv2.HoughLinesP(thinned, # Input edge image
                            1, # Distance resolution in pixels
                            np.pi/180, # Angle resolution in radians
                            threshold=15, # Min number of votes for valid line
                            minLineLength=3, # Min allowed length of line

                            maxLineGap=15 # Max allowed gap bet
                                            )
                    lines_list= list()
                    dist =0
                    
                    # Iterate over points
                    if lines is not None:
                        print("lines found")
                        for points in lines:
                            # Extracted points nested in the list
                            x1, y1, x2, y2 = points[0]
                            # Draw the lines join the points
                            # On the original image
                            print(image_width)
                            print(image_height)
                           

                            x1=(x1/2) + int(ox1)
                            x2=(x2/2) + int(ox1)
                            y1=(y1/2) + int(oy1)
                            y2=(y2/2) + int(oy1)
                           
                            print(x1,x2,y1,y2)
                      
                           
            
                            cv2.line(org_image, (int(x1), int(y1)), (int(x2),int(y2)), (0, 255, 0), 2)
                            # Maintain a simples lookup list for points
                            lines_list.append([(x1, y1), (x2, y2)])
                            dist = dist + ((x2)-(x1) + (y2)-(y2))
                    
                        
                        cv2.imshow("Lines ", org_image)
                        cv2.waitKey()
                 
                    
                    
                    print("total pixels:", dist)
                else: 
                    print("Not Target class... found class:",class_name)
                print("No lines found for",image_name)

if __name__ == '__main__':
    # read a cracked sample image
    main()

