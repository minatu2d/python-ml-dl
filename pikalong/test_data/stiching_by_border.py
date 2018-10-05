# import the necessary packages
from panorama import Stitcher
import argparse
import imutils
import cv2
import numpy as np
from matplotlib import pyplot as plt

def get_border(input_img, margin):
    left_border = input_img[ : , : margin]
    right_border = input_img[ : , -margin:]
    above_border = input_img[ : margin, : ]
    below_border = input_img[-margin:, : ]
    return left_border, right_border, above_border, below_border

def find_nearest_border_pair(imageA, imageB, borderless = 1):
    distances = np.zeros((4, 4,4)) + -1
    same_points = np.zeros((4, 4,4)) + -1
    for rotate in range(4):
        border_list_1 = get_border(imageA, borderless)
        if (len(imageB.shape) >= 3):
            border_list_2 = get_border(np.rot90(imageB, rotate, (1,2)), borderless)
        else:
            border_list_2 = get_border(np.rot90(imageB, rotate), borderless)

        for i in range(4):
            for j in range(4):
                border_1 = border_list_1[i]
                border_2 = border_list_2[j]
                if (i != j) and (border_1.shape == border_2.shape):
                    # Edge points
                    valid_points_1 = border_1 > 0
                    valid_points_2 = border_2 > 0
                    n_total_points = np.sum(np.logical_or(valid_points_1, valid_points_2))
                    same_edge = border_2 == border_1
                    n_same_points = np.sum(np.logical_and(same_edge, valid_points_2))
                    if (n_total_points == 0):
                        same_points[rotate, i, j] = 0
                    else:
                        same_points[rotate, i, j] = 1.0 * n_same_points / n_total_points
                    # Distance
                    distances[rotate, i, j] = np.linalg.norm(border_1 - border_2)
#                print("Rotate :", 90 * rotate,", A :", i, "B :", j, border_1.shape,
#                        border_2.shape, "Distance :",distances[rotate,i,j],
#                        "Same edge ponts :", same_points[rotate, i, j])

    return distances, same_points

def get_relative_position_with(imageA, imageB):
    distance_matrix, same_points = find_nearest_border_pair(imageA, imageB)
    #print("Distance : ", distance_matrix)
    dist_min = np.min(distance_matrix[distance_matrix != -1])
    print(dist_min)

    #print("Same point :", same_points)
    print(np.max(same_points[same_points != -1]))

    max_same_points_fract = np.max(same_points[same_points != -1])
    max_idx = np.argmax(same_points != -1)
    max_ij = np.unravel_index(np.argmax(same_points, axis=None), same_points.shape)
    print(max_ij)
    return max_ij,max_same_points_fract 

if __name__ == '__main__':
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--first", required=True,
        help="path to the first image")
    ap.add_argument("-s", "--second", required=True,
        help="path to the second image")
    args = vars(ap.parse_args())

    # load the two images and resize them to have a width of 400 pixels
    # (for faster processing)
    imageA = cv2.cvtColor(cv2.imread(args["first"]), cv2.COLOR_BGR2RGB)
    imageB = cv2.cvtColor(cv2.imread(args["second"]), cv2.COLOR_BGR2RGB)
    plt.subplot(1,2,1)
    plt.imshow(imageA)
    plt.subplot(1,2,2)
    plt.imshow(imageB)
    plt.show()
    imageA = cv2.Canny(imageA,100,200)
    imageB = cv2.Canny(imageB,100,200)
    plt.subplot(1,2,1)
    plt.imshow(imageA, cmap='gray')
    plt.subplot(1,2,2)
    plt.imshow(imageB, cmap='gray')
    plt.show()
    print(imageA.shape)
    print(imageB.shape)
    relative_pos = get_relative_position_with(imageA, imageB)
    print(relative_pos)
