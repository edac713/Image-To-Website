from PIL import Image, ImageDraw, ImageFont, ImageColor

# Function to add an overlay with annotations to an image
def add_overlay(image, overlay_info, position_y, annotation_font):
    # Calculate the height of the overlay
    overlay_height = int(image.height * overlay_info["height_ratio"])
    
    # Create the overlay image with an alpha channel (RGBA)
    overlay_image = Image.new('RGBA', (image.width, overlay_height), color=0)
    draw = ImageDraw.Draw(overlay_image)
    
    # Fill the overlay with the color and opacity
    color = ImageColor.getrgb(overlay_info["color"]) + (int(255 * overlay_info["opacity"]),)
    draw.rectangle([(0, 0), (image.width, overlay_height)], fill=color)
    
    # Add the annotation with full opacity
    text_color = ImageColor.getrgb(overlay_info["color"])
    text_position = (10, 10)  # Small padding from the top-left corner
    draw.text(text_position, overlay_info["annotation"], font=annotation_font, fill=text_color)
    
    # Composite the overlay onto the original image at the correct position
    image.paste(overlay_image, (0, position_y), overlay_image)

# Load the original UI image
original_ui_image_path = '/mnt/data/original_ui_image.png'
original_ui_image = Image.open(original_ui_image_path)

# Define the overlay information with height ratios, colors, and opacities
overlays_info = [
    {"height_ratio": 0.1, "color": "#D14D41", "opacity": 0.2, "annotation": "1"},
    {"height_ratio": 0.225, "color": "#DA702C", "opacity": 0.2, "annotation": "2"},
    {"height_ratio": 0.225, "color": "#F2C12E", "opacity": 0.2, "annotation": "3"},
    {"height_ratio": 0.225, "color": "#2E7D32", "opacity": 0.2, "annotation": "4"},
    {"height_ratio": 0.225, "color": "#2E7DBF", "opacity": 0.2, "annotation": "5"},
]

# Load a font for the annotations at a larger size
# We check for DejaVuSans-Bold, but you may replace it with the path to any other .ttf file if needed
dejavu_font_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
if os.path.exists(dejavu_font_path):
    annotation_font = ImageFont.truetype(dejavu_font_path, 40)
else:
    print("DejaVuSans-Bold font not found. Using default font at a larger size.")
    annotation_font = ImageFont.load_default()

# Create a fresh image copy to work with
image_to_process = original_ui_image.copy()

# Apply each overlay to the fresh image copy
current_position_y = 0
for overlay in overlays_info:
    add_overlay(image_to_process, overlay, current_position_y, annotation_font)
    current_position_y += int(image_to_process.height * overlay["height_ratio"])

# Display the final processed UI image with overlays and larger annotations
image_to_process.show()
