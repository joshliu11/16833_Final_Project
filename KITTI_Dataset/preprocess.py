import cv2
import numpy as np
import os
import code
import argparse
from multiprocessing import Pool, cpu_count
from functools import partial


def blur_and_overwrite(img_path, filename):
    """
    Apply a blurring kernel to enhance effects of motion blur
        :img_path: base path to image
        :filename: name of the image we're blurring
    """
    # define the motion blurring kernel
    size = 30
    motion_blur_kernel = np.zeros((size, size))
    motion_blur_kernel[int((size-1)/2), :] = np.ones(size)
    motion_blur_kernel = motion_blur_kernel / size

    # read in image
    print(filename)
    img_i = img_path + '/' + filename
    image = cv2.imread(img_i)

    # applying motion blurring kernel
    grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.filter2D(image, -1, motion_blur_kernel)

    cv2.imwrite(img_i, blur)

def sharpen(img_path, filename):
    """
    Perform histogram equalization followed by sharpening kernel
        :img_path: base path to image
        :filename: name of the image we're enhancing
    """
    # define the sharpening kernel
    sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])

    # read in image
    print(filename)
    img_i = img_path + '/' + filename
    image = cv2.imread(img_i)

    # apply histogram equalization to enhance contrast 
    grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    histeq = cv2.equalizeHist(grayimg)

    # apply sharpening kernel
    sharpen = cv2.filter2D(histeq, -1, sharpen_kernel)

    # overwrite the image
    cv2.imwrite(img_i, sharpen)

def edge_enhance(img_path, filename):
    """
    Perform histogram equalization followed by edge enhancement
        :img_path: base path to image
        :filename: name of the image we're enhancing
    """
    # define the edge enhancement kernel
    edge_enhancement_kernel = np.array([[-1,-1,-1,-1,-1], [-1,2,2,2,-1], [-1,2,8,2,-1], [-1,2,2,2,-1], [-1,-1,-1,-1,-1]]) / 8.0

    # read in image
    print(filename)
    img_i = img_path + '/' + filename
    image = cv2.imread(img_i)

    # apply histogram equalization to enhance contrast 
    grayimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    histeq = cv2.equalizeHist(grayimg)

    # apply edge enhancement kernel
    edge = cv2.filter2D(histeq, -1, edge_enhancement_kernel)

    # overwrite the image
    cv2.imwrite(img_i, edge)

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("sequence_path", help="sequence folder to process")
    parser.add_argument("filtering", help="selects filtering method: edge_enhance or sharpen")
    args = parser.parse_args()
    
    sequence_path = args.sequence_path
    filtering = args.filtering
    
    if filtering == "edge_enhance":
        filter_func = edge_enhance
    elif filtering == "sharpen":
        filter_func = enhance_and_sharpen
    else:
        print("Filtering method invalid!")
        quit()
        
    # enable multiprocessing
    num_cpu = cpu_count()
    pool = Pool(num_cpu)

    # first image in stereo pair
    img_path = sequence_path + '/image_1'
    file_list = os.listdir(img_path)

    b_ov_part = partial(blur_and_overwrite, img_path)
    pool.map(b_ov_part, file_list)

    ee_ov_part = partial(filter_func, img_path)
    pool.map(ee_ov_part, file_list)

    print("Processing other camera images!")

    # second image in stereo pair
    img_path = sequence_path + '/image_0'
    file_list = os.listdir(img_path)

    b_ov_part = partial(blur_and_overwrite, img_path)
    pool.map(b_ov_part, file_list)

    ee_ov_part = partial(filter_func, img_path)
    pool.map(ee_ov_part, file_list)
    
if __name__ == "__main__":
    main()
