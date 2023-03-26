# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import cv2
import math
import xmltodict
import numpy as np
def main ():

    # # Convert into gray scale

    with open("cracking/Labels/GX010120-138.xml", "r") as xml_obj:
        # coverting the xml data to Python dictionary
        my_dict = xmltodict.parse(xml_obj.read())
        # closing the file
        xml_obj.close()
    image = cv2.imread('cracking/Images/GX010120-138.jpg')
    objects = my_dict["annotation"]["object"]
    bbox = objects["bndbox"]
    x1=int(bbox["xmin"])
    x2 = int(bbox["xmax"])
    y1= int(bbox['ymin'])
    y2 = int(bbox['ymax'])
    image = image[y1:y2, x1:x2]
    src = cv2.bilateralFilter(image,9,75,75)
    # contrast the image
    adjusted = cv2.convertScaleAbs(image, alpha=4, beta=10)
    cv2.imshow("i", adjusted)
    cv2.waitKey()

    cv2.imshow("a", src)
    cv2.waitKey()
    edges = cv2.Canny(adjusted, 50, 200,3)
    cv2.imshow("e", edges)
    cv2.waitKey()

    # Apply HoughLinesP method to
    #  directly obtain line end points
    lines = cv2.HoughLinesP(edges, # Input edge image
            1, # Distance resolution in pixels
            np.pi/180, # Angle resolution in radians
            threshold=20, # Min number of votes for valid line
            minLineLength=5, # Min allowed length of line
            maxLineGap=10 # Max allowed gap bet
                            )
    lines_list= list()
    dist =0
    # Iterate over points
    for points in lines:
        # Extracted points nested in the list
        x1, y1, x2, y2 = points[0]
        # Draw the lines join the points
        # On the original image
        cv2.line(src, (x1, y1), (x2, y2), (0, 255, 0), 2)
        # Maintain a simples lookup list for points
        lines_list.append([(x1, y1), (x2, y2)])
        dist = dist + (x2-x1 + y2-y1)


    cv2.imshow("9", src)
    cv2.waitKey()
    print("total pixels:", dist)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # read a cracked sample image
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
