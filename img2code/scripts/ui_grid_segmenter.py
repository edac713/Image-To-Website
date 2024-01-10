import cv2
import numpy as np
from matplotlib import pyplot as plt

def enhanced_edge_detection_and_segmentation(image, edge_threshold1, edge_threshold2):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, edge_threshold1, edge_threshold2)
    h_projection = np.sum(edges, axis=1)
    transitions = np.where(np.diff(h_projection > 0))[0]
    return transitions

def calculate_whitespace_and_merge_segments(image, boundaries, whitespace_threshold):
    merged_segments = []
    prev_end = 0
    for start, end in boundaries:
        if start - prev_end <= whitespace_threshold:
            if merged_segments:
                merged_segments[-1] = (merged_segments[-1][0], end)
            else:
                merged_segments.append((start, end))
        else:
            merged_segments.append((start, end))
        prev_end = end
    return merged_segments

# Load and process the image
original_image = cv2.imread('path_to_uploaded_image')  # Update path as needed
edge_threshold1 = 50
edge_threshold2 = 150

# Find initial segments using edge detection
transitions = enhanced_edge_detection_and_segmentation(original_image, edge_threshold1, edge_threshold2)
initial_boundaries = [(transitions[i], transitions[i+1]) for i in range(0, len(transitions), 2)]

# Merge segments based on whitespace threshold
whitespace_threshold = 30  # Set the desired whitespace threshold
merged_boundaries = calculate_whitespace_and_merge_segments(original_image, initial_boundaries, whitespace_threshold)

# Visualize and save the segments with merged boundaries
enhanced_segmented_image = original_image.copy()
for start, end in merged_boundaries:
    cv2.line(enhanced_segmented_image, (0, start), (enhanced_segmented_image.shape[1], start), (0, 255, 0), 2)
    cv2.line(enhanced_segmented_image, (0, end), (enhanced_segmented_image.shape[1], end), (0, 255, 0), 2)

# Display the image with merged segments
plt.imshow(cv2.cvtColor(enhanced_segmented_image, cv2.COLOR_BGR2RGB))
plt.title('Segmented Wireframe')
plt.axis('off')
plt.show()

# Crop, save, and display the merged segments with dynamic aspect ratio
for i, (start, end) in enumerate(merged_boundaries):
    segment = original_image[start:end, :]
    segment_height, segment_width, _ = segment.shape
    aspect_ratio = segment_width / segment_height if segment_height > 0 else 1
    plt.figure(figsize=(6 * aspect_ratio, 6))
    plt.imshow(cv2.cvtColor(segment, cv2.COLOR_BGR2RGB))
    plt.title(f'Segment {i}')
    plt.axis('off')
    plt.show()
    segment_path = f'/mnt/data/segment_{i}.png'
    cv2.imwrite(segment_path, segment)
