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
            # print(int(bin(encoded_image.getpixel((i, j))[0])[2:]) & 1)
            # yield encoded_image.getpixel((i, j))
            if int(bin(encoded_image.getpixel((i, j))[0])[2:]) & 1 == 1:
                pixels[i, j] = (0, 0, 0)
            else:
                pixels[i, j] = (255, 255, 255)


                # Convert red value in returned tuple to a binary string via `bin()`
                # Grab the LSB (right-most value) from the binary string
                # Perform a check to see if resulting LSB value is `1`
                #   Write `pixels[x, y]` to to black `(0, 0, 0)`
                # Otherwise
                #   Write `pixels[x, y]` to white `(255, 255, 255)`
        # Save the decoded image as `decoded_image.png`
    decoded_image.save("decoded_image.png")
decode_image("encoded_sample.png")



# import base64
# with open("encoded_sample.png", "rb") as img_file:
#     my_string = base64.b64encode(img_file.read())
# # print(my_string)
# print(my_string.decode('utf-8'))
# import cv2
#
# def char_generator(message):
#   for c in message:
#     yield ord(c)
#
# def get_image(image_location):
#   img = cv2.imread(image_location)
#   # print(img)
#   return img
# # get_image("encoded_sample.png")
#
#
# def gcd(x, y):
#   while(y):
#     x, y = y, x % y
#
#   return x
#
# def encode_image(image_location, img_gen_location):
#     img = get_image(image_location)
#     img_gen = get_image(img_gen_location)
#     pattern = gcd(len(img), len(img[0]))
#     print(img, img_gen)
#     for i in range(len(img)):
#         for j in range(len(img[0])):
#             if (i+1 * j+1) % pattern == 0:
#                 try:
#                     img_gen[i][j] = img[i-1][j-1]
#                 except StopIteration:
#                     img_gen[i][j] = 0
#
#     print("breaking here")
#     print(img_gen)
#     return img_gen
# file_location = "encoded_sample.png"
# secret_message = "Hello from inside the picture!"
# encoded_image = encode_image(file_location, "decoded_image.png")
# img_gen.save('decoded_image.png')



# print("encoded_image: ", encoded_image)

# def decode_image(img_loc):
#   img = get_image(img_loc)
#   pattern = gcd(len(img), len(img[0]))
#   message = ''
#   for i in range(len(img)):
#     for j in range(len(img[0])):
#       if (i-1 * j-1) % pattern == 0:
#         if img[i-1][j-1][0] != 0:
#           message = message + chr(img[i-1][j-1][0])
#         else:
#           return message
#   print()
# decode_image(Image(encoded_image))
