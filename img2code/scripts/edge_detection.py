import cv2
import numpy as np
from PIL import Image, ImageEnhance
import os

def enhance_and_detect_contours(image_path):
    # Load the image using PIL
    original_image = Image.open(image_path)

    def adjust_contrast_and_sharpness(image, contrast_factor=2, sharpness_factor=2):
        contrast_enhancer = ImageEnhance.Contrast(image)
        contrast_image = contrast_enhancer.enhance(contrast_factor)
        sharpness_enhancer = ImageEnhance.Sharpness(contrast_image)
        return sharpness_enhancer.enhance(sharpness_factor)

    enhanced_image = adjust_contrast_and_sharpness(original_image)
    gray_image = cv2.cvtColor(np.array(enhanced_image), cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_image, threshold1=50, threshold2=100)
    kernel = np.ones((5,5), np.uint8)
    dilated_edges = cv2.dilate(edges, kernel, iterations=1)
    contours, _ = cv2.findContours(dilated_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contour_image = np.array(enhanced_image).copy()
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(contour_image, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Neon green bounding boxes

    # Convert the image back to RGB to display correctly in Jupyter Notebook
    contour_image_rgb = cv2.cvtColor(contour_image, cv2.COLOR_BGR2RGB)

    # Determine the file format from the original image
    file_name, file_ext = os.path.splitext(image_path)
    if not file_ext:
        file_ext = '.jpeg'  # Default format if not specified

    # Save the contour image in the same format as the original image
    contour_image_path = f"{file_name}_contours_updated{file_ext}"
    Image.fromarray(contour_image_rgb).save(contour_image_path)

    ui_elements_dimensions = [cv2.boundingRect(contour) for contour in contours]
    return contour_image_path, ui_elements_dimensions

# Example usage
# The image_path variable will be set here with the actual uploaded image path
image_path = 'path_to_uploaded_image'  # This should be replaced by the actual path of the uploaded image
output_contour_image_path, detected_elements_dimensions = enhance_and_detect_contours(image_path)

# Load and display the output image with neon green bounding boxes
output_contour_image = Image.open(output_contour_image_path)
output_contour_image.show()
