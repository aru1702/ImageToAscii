import ImageToAscii as ITA
import VideoFrameExtract as VFE
import cv2
import PIL
from os import system, name
import time

# define our clear function
# src: https://www.geeksforgeeks.org/clear-screen-python/
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def main():
    # video path
    path = input("Enter video path: ")
    try:
        video = cv2.VideoCapture(path)
    except:
        print("Error opening video stream")
        return
    
    # desire image size
    w = input("Enter image width in pixel: ")
    if int(w) > 0:
        new_w = int(w)
    else:
        print("Minimum width is 1")
        return

    while(True):
        # get image from video
        frame = VFE.video_to_frame(video)

        # convert into PIL format
        pil_img = PIL.Image.fromarray(frame)

        # into ascii
        rz_img = ITA.resize_image(pil_img, new_w)
        gy_img = ITA.px_to_grayscale(rz_img)
        new_image = ITA.px_to_ascii(gy_img)

        px_count = len(new_image)
        ascii_img = "\n".join(
                new_image[i:(i+new_w)] for i in range(0, px_count, new_w)
            )

        # print into terminal
        print(ascii_img)

        # sleep
        time.sleep(0.025)

        # clear screen
        clear()

        # break video in the middle
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

main()