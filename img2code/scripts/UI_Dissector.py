from PIL import Image, ImageDraw, ImageFont, ImageColor

# Load the original UI image
# Replace 'path_to_uploaded_image' with the actual path of the uploaded UI image
original_ui_image_path = 'path_to_uploaded_image'
original_ui_image = Image.open(original_ui_image_path)

# Define the overlay information with height ratios, colors, and opacities
overlays_info = [
    {"height_ratio": 0.1, "color": "#D14D41", "opacity": 0.2, "annotation": "1"},
    {"height_ratio": 0.225, "color": "#DA702C", "opacity": 0.2, "annotation": "2"},
    {"height_ratio": 0.225, "color": "#F2C12E", "opacity": 0.2, "annotation": "3"},
    {"height_ratio": 0.225, "color": "#2E7D32", "opacity": 0.2, "annotation": "4"},
    {"height_ratio": 0.225, "color": "#2E7DBF", "opacity": 0.2, "annotation": "5"},
]

# Function to add overlays to the image
def add_overlay(image, overlay_info, position_y, font):
    draw = ImageDraw.Draw(image, 'RGBA')
    overlay_height = int(image.height * overlay_info["height_ratio"])
    # Draw the overlay rectangle
    draw.rectangle(
        [(0, position_y), (image.width, position_y + overlay_height)],
        fill=ImageColor.getrgb(overlay_info["color"]) + (int(overlay_info["opacity"] * 255),)
    )
    # Annotate the overlay
    text_position = (10, position_y + 10)  # Position the text 10 pixels from the top and left of the overlay
    draw.text(text_position, overlay_info["annotation"], font=font")

# Load or define a font for the annotations
annotation_font = ImageFont.load_default()

# Apply each overlay to the original image
current_position_y = 0
for overlay in overlays_info:
    add_overlay(original_ui_image, overlay, current_position_y, annotation_font)
    current_position_y += int(original_ui_image.height * overlay["height_ratio"])

# Display the final processed UI image with overlays and annotations
original_ui_image.show()
