from PIL import Image, ImageEnhance, ImageFilter
import matplotlib.pyplot as plt

# Load the input image and convert to RGB format
img = Image.open("PE05-input.jpg").convert("RGB")

# Step 1: Slightly increase brightness (not too much to avoid overexposure)
img = ImageEnhance.Brightness(img).enhance(1.5)

# Step 2: Slightly increase contrast to enhance the difference between light and dark areas
img = ImageEnhance.Contrast(img).enhance(1.2)

# Step 3: Apply detail filter to enhance fine textures and structures
img = img.filter(ImageFilter.DETAIL)

# Step 4: Apply a moderate sharpness enhancement
img = ImageEnhance.Sharpness(img).enhance(1.5)

# Step 5: Apply smoothing filter to reduce minor noise and make image cleaner
img = img.filter(ImageFilter.SMOOTH_MORE)

# Display the enhanced image
plt.imshow(img)
plt.axis("off")
plt.show()

# Save the output image
img.save("PE05-output.jpg")

# --------------------------------------------------------------------
# Observation Questions and Detailed Answers:

# 1. How many people do you see in the output image?
# Answer: There are two people visible in the output image.
# They are walking on the sidewalk on the left side of the image, slightly ahead of each other.

# 2. How many trees can you identify?
# Answer: Two trees can be identified.
# One is located near the sidewalk on the left, and the second is further behind, partially visible.

# 3. How many windows can you identify on the 2nd floor of the first building (labelled as “1”) on the right-hand side of the road?
# Answer: There are three windows visible on the second floor of the first building labeled as "1", located on the right side of the road.

# 4. How many windows can you identify in the second building (labeled as “2”) on the right-hand side of the road facing you?
# Answer: Six windows can be clearly identified on the building labeled "2", which is on the right side of the road and faces the viewer.
