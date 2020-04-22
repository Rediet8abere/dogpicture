from PIL import Image

def decode_image(file_location):
    encoded_image = Image.open(file_location)
    print("encoded_image: ", encoded_image)
    red_channel = encoded_image.split()[0]
    print("red_channel: ", red_channel)
    x_size = encoded_image.size[0]
    y_size = encoded_image.size[1]
    print("x_size: ", x_size)
    print("y_size: ", y_size)
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    print("pixels", pixels[0, 0], pixels[100, 200])
    # TODO: Fill in decoding functionality
    # Loop over the range of x_size (`x`)
    for i in range(x_size):
        # Loop over the range of y_size (`y`)
        for j in range(y_size):
            # Get RGB values from red_channel via `getpixel(x, y)`
            # Convert red value in returned tuple to a binary string via `bin()`
            # Grab the LSB (right-most value) from the binary string
            if int(bin(encoded_image.getpixel((i, j))[0])[2:]) & 1 == 1:
                pixels[i, j] = (0, 0, 0)
            else:
                pixels[i, j] = (255, 255, 255)
                
        # Save the decoded image as `decoded_image.png`
    decoded_image.save("decoded_image.png")
decode_image("encoded_sample.png")
