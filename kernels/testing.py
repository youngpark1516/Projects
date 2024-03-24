import kernels
from PIL import Image
image = Image.open('images/bird_image.jpg')
edge_image1 = kernels.apply_kernel(image, kernels.edge_detection1)
edge_image1.save('images/bird_image_edge1.jpg')

edge_image2 = kernels.apply_kernel(image, kernels.edge_detection2)
edge_image2.save('images/bird_image_edge2.jpg')

top_sobel_image = kernels.apply_kernel(image, kernels.top_sobel)
top_sobel_image.save('images/bird_image_top_sobel.jpg')

bottom_sobel_image = kernels.apply_kernel(image, kernels.bottom_sobel)
bottom_sobel_image.save('images/bird_image_bottom_sobel.jpg')

left_sobel_image = kernels.apply_kernel(image, kernels.left_sobel)
left_sobel_image.save('images/bird_image_left_sobel.jpg')

right_sobel_image = kernels.apply_kernel(image, kernels.right_sobel)
right_sobel_image.save('images/bird_image_right_sobel.jpg')

sharpen_image = kernels.apply_kernel(image, kernels.sharpen)
sharpen_image.save('images/bird_image_sharpen.jpg')

emboss_image = kernels.apply_kernel(image, kernels.emboss)
emboss_image.save('images/bird_image_emboss.jpg')

box_blur_image = kernels.apply_kernel(image, kernels.box_blur)
box_blur_image.save('images/bird_image_box_blur.jpg')

gaussian_blur_3x3_image = kernels.apply_kernel(image, kernels.gaussian_blur_3x3)
gaussian_blur_3x3_image.save('images/bird_image_gaussian_blur_3x3.jpg')

gaussian_blur_5x5_image = kernels.apply_kernel(image, kernels.gaussian_blur_5x5)
gaussian_blur_5x5_image.save('images/bird_image_gaussian_blur_5x5.jpg')

unsharp_masking_5x5_image = kernels.apply_kernel(image, kernels.unsharp_masking_5x5)
unsharp_masking_5x5_image.save('images/bird_image_unsharp_masking_5x5.jpg')