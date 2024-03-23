import kernels
from PIL import Image
image = Image.open("bird_image.jpg")
edge_image = kernels.apply_kernel(image, kernels.edge_detection1)
edge_image.save('bird_image_edge.jpg')