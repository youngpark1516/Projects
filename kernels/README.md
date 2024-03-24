# Kernels
## Introduction
This small project is an extension of the data science classes I took at UCSD in the second quarter of freshman year, DSC20 and DSC96, in which the final projects involved manipulating images through kernels. 

The project of DSC20 involved creating class methods applying edge detection and blurring on images, while the project of DSC96 involved using the sharpening kernel. Having developed a light interest in these methods of manipulating images through kernels for various purposes, the following project was thought of and executed.

The objective of this project is to create a simple module that provides several commonly used kernels for image manipulation and a simple function that is capable of applying the kernels to an image.

## Imports
Two existing libraries will be used.

NumPy: NumPy is a third-party open-source library specializing in arrays and matrices. The library was chosen for its superior performance compared to standard Python lists, especially in image data that are generally large in size and numeric.

PIL: A standard Python library used for tasks involving images. There are other libraries such as openCV but the performance difference is arguable, so PIL was arbitrarily chosen.

## Kernels included
Following are the kernels that will be provided in the module:

**3x3**
- Edge detection - two variations, one involving corners, one not
- Sobel operators - four variations, one from each side
- Sharpen
- Emboss
- Box blur
- Gaussian blur

**5x5**
- Gaussian blur
- Unsharp masking 

## Kernel applying function
The function takes in two parameters, the image to be modified and a 2d NumPy array containing the kernel, and returns the modified image. The code is fully explained through comments.

Try-catch was used in a relatively unconventional way. This was simply because try-catch uses little extra memory compared to a series of if-else statements to check the kernel being on the edge of the image.

The resulting images of each kernel can be found in the images folder, the original being 'bird_image.jpg'.

The image modification process took an average of 50 seconds per 875520 pixels (1024x855) or 57 microseconds per pixel. While this is seemingly a decent speed, a total of 50 seconds is a rather disappointing performance for a task that is often done in mere seconds on any photo editing application on a standard phone.

## Conclusion
This was a quick project on modifying images through kernels. While the intended functionality of the module was fully implemented, the efficiency of the process was likely lacking either due to the code or the fundamental limit of Python loops.
