# import the necessary packages
from panorama import Stitcher
import argparse
import imutils
import cv2
import numpy as np

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--first", required=True,
	help="path to the first image")
ap.add_argument("-s", "--second", required=True,
	help="path to the second image")
args = vars(ap.parse_args())

# load the two images and resize them to have a width of 400 pixels
# (for faster processing)
imageA = cv2.imread(args["first"])
imageB = cv2.imread(args["second"])
print(imageA.shape)
print(imageB.shape)
imageA = imutils.resize(imageA, width=400)
imageB = imutils.resize(imageB, width=400)

def get_border(input_img, margin):
    left_border = input_img[ : , : margin]
    right_border = input_img[ : , -margin:]
    above_border = input_img[ : margin, : ]
    below_border = input_img[-margin:, : ]
    print(left_border.shape)
    return left_border, right_border, above_border, below_border

def find_nearest_border_pair(border_list_1, border_list_2):
    distance = np.zeros((4,4)) + -1
    for i in range(4):
        for j in range(4):
            border_1 = border_list_1[i]
            border_2 = border_list_2[j]
            if (border_1.shape == border_2.shape):
                distance[i][j] = np.linalg.norm(border_1 - border_2)
            print("A :", i, "B :", j, border_1.shape, border_2.shape, "Distance :",distance[i,j])
    return distance

#border_list_a = get_border(imageA, 1)
#border_list_b = get_border(imageB, 1)
#
#distance_matrix = find_nearest_border_pair(border_list_a, border_list_b)
#print(distance_matrix)
#print(np.unravel_index(np.argmin(distance_matrix != 0),distance_matrix.shape))


# stitch the images together to create a panorama
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

# show the images
#cv2.imshow("Image A", imageA)
#cv2.imshow("Image B", imageB)
#cv2.imshow("Keypoint Matches", vis)
cv2.imwrite("Keypoint_Matches.png", vis)
#cv2.imshow("Result", result)
cv2.imwrite("Result.png", result)
#cv2.waitKey(0)
