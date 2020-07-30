# Convert a Color image to black & White 

from PIL import Image

img = Image.open("colorPhoto.jpg")
convertedImage = img.convert("L")
convertedImage.save("b&w_photo.jpg")
convertedImage.show()

# Find image resolution
def resolution(filename):
    with open(filename, 'rb') as img_file:                 # Open image for reading in binary mode
        img_file.seek(163)                                 # Height of image (in 2 bytes) is at 164th position
        rd = img_file.read(2)                              # Read the first 2 bytes
        height = (rd[0] << 8) + rd[1]
        rd = img_file.read(2)                              # Next 2 bytes is width
        width = (rd[0] << 8) + rd[1]
        
    print("Resolution of the image is:", width, "X", height)

resolution("sunset.jpg")
resolution("colorPhoto.jpg")
resolution("b&w_photo.jpg")