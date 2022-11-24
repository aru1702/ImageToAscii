# src: https://www.youtube.com/watch?v=Ay6Nlb3KJog
import cv2
import sys


# extract video per frame from cv2
def video_to_frame(video):
    success, frame = video.read()
    if success:
        return frame

# main
def main():
    # input
    path = input("Enter video path: ")

    try:
        video = cv2.VideoCapture(path)
    except:
        print("Error opening video stream")
        sys.exit()

    while(True):
        # get image from video
        frame = video_to_frame(video)

        # show image
        cv2.imshow("Output", frame)

        # break video in the middle
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # finish video
    cv2.destroyAllWindows()

# main()