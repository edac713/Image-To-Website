from PIL import Image
import matplotlib.pyplot as plt

# Replace these paths with the actual image paths
original_image_path = 'path_to_original_image.jpg'
rendered_code_screenshot_path = 'path_to_rendered_code_image.jpg'

# Load images and display them with titles
images = [Image.open(path) for path in [original_image_path, rendered_code_screenshot_path]]
titles = ['Original Image', 'Rendered Code Screenshot']
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
for i, (img, title) in enumerate(zip(images, titles)):
    ax[i].imshow(img)
    ax[i].set_title(title)
    ax[i].axis('off')
plt.show()