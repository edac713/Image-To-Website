import cv2
import numpy as np
from matplotlib import pyplot as plt

def enhanced_edge_detection_and_segmentation(image, edge_threshold1, edge_threshold2, min_gap):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection to pick up finer lines
    edges = cv2.Canny(gray, edge_threshold1, edge_threshold2)

    # Calculate the horizontal projection of edges
    h_projection = np.sum(edges, axis=1)

    # Find transitions in the edge projection
    transitions = np.where(np.diff(h_projection > 0))[0]

    # Determine segment boundaries with the refined edge detection
    boundaries = []
    for i in range(0, len(transitions), 2):
        if i+1 < len(transitions) and transitions[i+1] - transitions[i] > min_gap:
            boundaries.append((transitions[i], transitions[i+1]))
    return boundaries

# Load the original image (Update the path accordingly)
original_ui_image_path = 'path_to_uploaded_image'
original_image = cv2.imread(original_ui_image_path)

# Edge detection thresholds and minimum gap
edge_threshold1 = 50  # Lower threshold for finer edge detection
edge_threshold2 = 150  # Upper threshold
smaller_min_gap = 5    # Reduced gap to detect finer details

# Apply the function to find enhanced segment boundaries
enhanced_boundaries = enhanced_edge_detection_and_segmentation(original_image, edge_threshold1, edge_threshold2, smaller_min_gap)

# Visualize the enhanced segment boundaries on the image
enhanced_segmented_image = original_image.copy()
for start, end in enhanced_boundaries:
    cv2.line(enhanced_segmented_image, (0, start), (enhanced_segmented_image.shape[1], start), (0, 255, 0), 2)
    cv2.line(enhanced_segmented_image, (0, end), (enhanced_segmented_image.shape[1], end), (0, 255, 0), 2)

# Save and show the image with enhanced segments
enhanced_segmented_image_path = 'path_for_saving_enhanced_segmented_image'
cv2.imwrite(enhanced_segmented_image_path, enhanced_segmented_image)
plt.imshow(cv2.cvtColor(enhanced_segmented_image, cv2.COLOR_BGR2RGB))
plt.title('Enhanced Segmented Wireframe')
plt.axis('off')
plt.show()

# Crop the segments with padding and save them
padding = 10  # Pixels to add as padding around each segment
enhanced_cropped_segments_paths = []

plt.figure(figsize=(6, 9))  # Aspect ratio 2:3 for consistent display
for i, (start, end) in enumerate(enhanced_boundaries):
    padded_start = max(start - padding, 0)
    padded_end = min(end + padding, original_image.shape[0])
    segment = original_image[padded_start:padded_end, :]
    segment_path = 'path_for_saving_padded_segment_' + str(i)
    cv2.imwrite(segment_path, segment)
    enhanced_cropped_segments_paths.append(segment_path)

    # Display each segment
    plt.subplot(len(enhanced_boundaries), 1, i+1)
    plt.imshow(cv2.cvtColor(segment, cv2.COLOR_BGR2RGB))
    plt.title(f'Enhanced Padded Segment {i}')
    plt.axis('off')

plt.tight_layout()
plt.show()

# Output the paths of the saved enhanced segment images
enhanced_cropped_segments_paths