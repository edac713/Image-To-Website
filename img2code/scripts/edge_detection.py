import cv2
import numpy as np
from PIL import Image, ImageEnhance

def enhance_and_detect_contours(image_path):
    # Load the image using PIL
    original_image = Image.open(image_path)

    # Enhance the image by increasing contrast and sharpness
    def adjust_contrast_and_sharpness(image, contrast_factor=2, sharpness_factor=2):
        contrast_enhancer = ImageEnhance.Contrast(image)
        contrast_image = contrast_enhancer.enhance(contrast_factor)
        sharpness_enhancer = ImageEnhance.Sharpness(contrast_image)
        return sharpness_enhancer.enhance(sharpness_factor)

    # Apply the enhancements
    enhanced_image = adjust_contrast_and_sharpness(original_image)

    # Convert the enhanced image to grayscale for edge detection
    gray_image = cv2.cvtColor(np.array(enhanced_image), cv2.COLOR_BGR2GRAY)

    # Detect edges with Canny edge detector
    edges = cv2.Canny(gray_image, threshold1=50, threshold2=100)

    # Apply dilation to merge edges that are close to each other
    kernel = np.ones((5,5), np.uint8)
    dilated_edges = cv2.dilate(edges, kernel, iterations=1)

    # Find contours on the dilated edge image
    contours, _ = cv2.findContours(dilated_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes around the contours on the enhanced image
    contour_image = np.array(enhanced_image).copy()
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(contour_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Save the contour image
    contour_image_path = image_path.replace('.jpeg', '_contours_updated.jpeg')
    Image.fromarray(contour_image).save(contour_image_path)

    # Calculate dimensions for each detected UI element
    ui_elements_dimensions = [cv2.boundingRect(contour) for contour in contours]

    return contour_image_path, ui_elements_dimensions

# Path to the uploaded image
image_path = '/mnt/data/IMG_9479.jpeg'

# Using the function on the provided image
output_contour_image_path, detected_elements_dimensions = enhance_and_detect_contours(image_path)

# Load the image with drawn contours to display
output_contour_image = Image.open(output_contour_image_path)

# Display the image with contours
output_contour_image.show()