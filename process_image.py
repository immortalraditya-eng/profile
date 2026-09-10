import sys
from rembg import remove
from PIL import Image

input_path = "profile.png"
output_path = "profile-red.png"

print("Reading image...")
image = Image.open(input_path).convert("RGBA")

print("Removing background...")
output_image = remove(image)

print("Applying red background...")
red_bg = Image.new("RGBA", output_image.size, (205, 255, 0, 255)) # wait, the prompt said 'ganti background merah', so it should be red.
# Red in hex is #FF3B00 based on the css: --red: #FF3B00;
# (255, 59, 0, 255)
red_bg = Image.new("RGBA", output_image.size, (255, 59, 0, 255))

red_bg.paste(output_image, (0, 0), output_image)
red_bg.save(output_path)
print("Image processed successfully.")
