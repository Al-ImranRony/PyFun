# Convert a Color image to black & White 

from PIL import Image

img = Image.open("colorPhoto.jpg")
convertedImage = img.convert("L")
convertedImage.save("b&w_photo.jpg")
convertedImage.show()