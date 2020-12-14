import cv2
import numpy as np
import os
import code
from multiprocessing import Pool, cpu_count
from functools import partial
from PIL import Image


def convert_to_RGB(img_path, filename):
	
	print(filename)
	img_i = img_path + '/' + filename

	im = Image.open(img_i, 'r').convert('L')
	im = np.stack((im,)*3, axis=-1)
	im = Image.fromarray(im)
	im.save(img_i)


def main():

	num_cpu = cpu_count()
	pool = Pool(num_cpu)

	img_path = ('./image_1')
	file_list = os.listdir(img_path)
	print(len(file_list))
	db_ov_part = partial(convert_to_RGB, img_path)
	pool.map(db_ov_part, file_list)

	print("Processing other camera images!")

	img_path = ('./image_0')
	file_list = os.listdir(img_path)

	db_ov_part = partial(convert_to_RGB, img_path)
	pool.map(db_ov_part, file_list)
	
if __name__ == "__main__":
	main()
