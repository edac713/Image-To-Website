import cv2
import numpy as np
from matplotlib import pyplot as plt

def enhanced_edge_detection_and_segmentation(image, edge_threshold1, edge_threshold2):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Canny edge detection
    edges = cv2.Canny(gray, edge_threshold1, edge_threshold2)
    # Calculate horizontal projection of edges
    h_projection = np.sum(edges, axis=1)
    # Find transitions in the edge projection
    transitions = np.where(np.diff(h_projection > 0))[0]
    return transitions

def calculate_whitespace_and_merge_segments(image, boundaries, whitespace_threshold):
    # Calculate whitespace and merge segments accordingly
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
original_image = cv2.imread('/mnt/data/IMG_0030.jpeg')
edge_threshold1 = 50
edge_threshold2 = 150

# Find initial segments
transitions = enhanced_edge_detection_and_segmentation(original_image, edge_threshold1, edge_threshold2)
initial_boundaries = [(transitions[i], transitions[i+1]) for i in range(0, len(transitions), 2)]

# Merge segments based on calculated whitespace
whitespace_threshold = 20  # Set the whitespace threshold
merged_boundaries = calculate_whitespace_and_merge_segments(original_image, initial_boundaries, whitespace_threshold)

# Visualize and save the segments
enhanced_segmented_image = original_image.copy()
for start, end in merged_boundaries:
    cv2.line(enhanced_segmented_image, (0, start), (enhanced_segmented_image.shape[1], start), (0, 255, 0), 2)
    cv2.line(enhanced_segmented_image, (0, end), (enhanced_segmented_image.shape[1], end), (0, 255, 0), 2)
plt.imshow(cv2.cvtColor(enhanced_segmented_image, cv2.COLOR_BGR2RGB))
plt.title('Merged Segmented Wireframe Based on Whitespace')
plt.axis('off')
plt.show()

# Crop, save, and display the merged segments
padding = 10
plt.figure(figsize=(6, 9))
for i, (start, end) in enumerate(merged_boundaries):
    padded_start = max(start - padding, 0)
    padded_end = min(end + padding, original_image.shape[0])
    segment = original_image[padded_start:padded_end, :]
    segment_path = f'/mnt/data/whitespace_merged_segment_{i}.png'
    cv2.imwrite(segment_path, segment)
    plt.subplot(len(merged_boundaries), 1, i+1)
    plt.imshow(cv2.cvtColor(segment, cv2.COLOR_BGR2RGB))
    plt.title(f'Whitespace Merged Segment {i}')
    plt.axis('off')
plt.tight_layout()
plt.show()
