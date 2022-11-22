# src: https://www.youtube.com/watch?v=v_raWlX7tZY
import PIL.Image

# ascii character list
# the more to the right, the more light intensity
# ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]
ASCII_CHARS = ["@", "&", "#", "$", "B", "%", "G", "P", "5", "Y", "J", "?", "7",  "*", "+", "!", ";", ":", ",", "."]

# resize image
def resize_image(image, new_w=100):
    w, h = image.size
    ratio = h / w
    new_h = int(new_w * ratio)
    resized_img = image.resize((new_w, new_h))
    return(resized_img)

# convert pixel to grayscale
def px_to_grayscale(image):
    grayscale_img = image.convert("L")
    return(grayscale_img)

# convert pixel to ascii
def px_to_ascii(image):
    pixels = image.getdata()
    chs = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(chs)

# main
def main(new_w=100):

    # input from user
    path = input("Enter the image path: ")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "is not valid! Please try again.")

    w = input("Enter image width in pixel: ")
    if int(w) > 1:
        new_w = int(w)

    rz_img = resize_image(image, new_w)
    gy_img = px_to_grayscale(rz_img)
    new_image = px_to_ascii(gy_img)

    px_count = len(new_image)
    ascii_img = "\n".join(
            new_image[i:(i+new_w)] for i in range(0, px_count, new_w)
        )

    print(ascii_img)

main()