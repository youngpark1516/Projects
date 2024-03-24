#imports
import numpy as np
from PIL import Image

#kernels
edge_detection1 = np.array([[0, -1, 0],
                            [-1, 4, -1],
                            [0, -1, 0]])

edge_detection2 = np.array([[-1, -1, -1],
                            [-1, 8, -1],
                            [-1, -1, -1]])

bottom_sobel = np.array([[-1, -2, -1],
                         [0, 0, 0],
                         [1, 2, 1]])

top_sobel = np.array([[1, 2, 1],
                      [0, 0, 0],
                      [-1, -2, -1]])

left_sobel = np.array([[1, 0, -1],
                       [2, 0, -2],
                       [1, 0, -1]])

right_sobel = np.array([[-1, 0, 1],
                        [-2, 0, 2],
                        [-1, 0, 1]])

sharpen = np.array([[0, -1, 0],
                    [-1, 5, -1],
                    [0, -1, 0]])

emboss =  np.array([[-2, -1, 0],
                    [-1,  1, 1],
                    [ 0,  1, 2]])

box_blur = (1 / 9.0) * np.array([[1, 1, 1],
                                 [1, 1, 1],
                                 [1, 1, 1]])

gaussian_blur_3x3 = (1 / 16.0) * np.array([[1, 2, 1],
                                           [2, 4, 2],
                                           [1, 2, 1]])

gaussian_blur_5x5 = (1 / 256.0) * np.array([[1, 4, 6, 4, 1],
                                            [4, 16, 24, 16, 4],
                                            [6, 24, 36, 24, 6],
                                            [4, 16, 24, 16, 4],
                                            [1, 4, 6, 4, 1]])

unsharp_masking_5x5 = -(1 / 256.0) * np.array([[1, 4, 6, 4, 1],
                                               [4, 16, 24, 16, 4],
                                               [6, 24, -476, 24, 6],
                                               [4, 16, 24, 16, 4],
                                               [1, 4, 6, 4, 1]])

kernel_dict = {'edge_detection1': edge_detection1,\
			   'edge_detection2': edge_detection2,\
			   'bottom_sobel': bottom_sobel,\
			   'top_sobel': top_sobel,\
			   'left_sobel': left_sobel,\
			   'right_sobel': right_sobel,\
			   'sharpen': sharpen,\
			   'emboss': emboss,\
			   'box_blur': box_blur,\
			   'gaussian_blur_3x3': gaussian_blur_3x3,\
			   'gaussian_blur_5x5': gaussian_blur_5x5,\
			   'unsharp_masking_5x5': unsharp_masking_5x5}

#kernel application
def apply_kernel(image, kernel):
    """
    Takes in an image object (PIL) and a kernel array and returns an image \
    object with the kernel applied

    Args:
        image: PIL image object
        kernel: A 2d square numerical array

    Returns:
        A product of the image with kernel applied
    """
    #Changing image to np array
    im_array = np.array(image)
    #Creating empty array of same size
    im_applied = np.zeros([int(im_array.shape[0]),int(im_array.shape[1]),3]).astype('uint8')
    for row in range(len(im_applied)):
        for col in range(len(im_applied[0])):
            #Cumulating according to kernel
            r_cumulated = 0
            b_cumulated = 0
            g_cumulated = 0
            mid_coor = len(kernel)//2
            #Looping through each value of kernel
            for ker_row in range(len(kernel)):
                for ker_col in range(len(kernel[0])):
                    #Try-catch for kernel being on edge of the image
                    try:
                        r_cumulated += im_array[row+ker_row-mid_coor,col+ker_col-mid_coor,0]*kernel[ker_row,ker_col]
                        g_cumulated += im_array[row+ker_row-mid_coor,col+ker_col-mid_coor,1]*kernel[ker_row,ker_col]
                        b_cumulated += im_array[row+ker_row-mid_coor,col+ker_col-mid_coor,2]*kernel[ker_row,ker_col]
                    except:
                        pass
            #Keeping values between possible range
            r_cumulated = max(min(r_cumulated, 255),0)
            g_cumulated = max(min(g_cumulated, 255),0)
            b_cumulated = max(min(b_cumulated, 255),0)
            #Applying to each pixel
            im_applied[row,col] = np.array([r_cumulated,g_cumulated,b_cumulated])
    return Image.fromarray(im_applied)
