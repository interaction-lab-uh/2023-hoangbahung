from PIL import Image
import os

# Set the directory where your images are located
input_dir = 'frame_2'

# Set the directory where you want to save the resized images
output_dir = 'resize_frame'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
# Set the desired size (width, height) for your images
desired_size = (360,640 )  # Change this to your preferred size

# Loop through all files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(('.jpg', '.jpeg', '.png', '.gif')):  # You can add more file extensions if needed
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)

        # Open the image using Pillow
        image = Image.open(input_path)

        # Resize the image to the desired size
        image = image.resize(desired_size, Image.ANTIALIAS)

        # Save the resized image to the output directory
        image.save(output_path)

        print(f"Resized and saved: {output_path}")
