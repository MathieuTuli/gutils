'''Open Cash Line Detection'''
import cv2


def mouse_position(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        print(x, y)


cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse_position)
