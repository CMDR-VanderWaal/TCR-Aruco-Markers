from distutils import core
from email.mime import image
from tkinter.tix import Tree
import cv2 as cv
import os

CHESS_BOARD_DIM = (9, 6)

n = 0

image_dir_path = "ArucoMarkers/CallibrateImages"
CHECK_DIR = os.path.isdir(image_dir_path)


if not CHECK_DIR:
    os.makedirs(image_dir_path)
    print(f'"{image_dir_path}" Directory is created ')
else:
    print(f'"{image_dir_path}" directory already exixts ')

criteria = (cv.TERM_CRITERIA_EPS + cv.TermCriteria_MAX_ITER, 30, 0.001)


def detChecker(image, grayImage, criteria, boardDimensions):
    ret, corners = cv.findChessboardCorners(grayImage, boardDimensions)
    if ret == True:
        corners1 = cv.cornerSubPix(
            grayImage, corners, (3, 3), (-1, -1), criteria)
        image = cv.drawChessboardCorners(image, boardDimensions, corners1, ret)

    return image, ret


cap = cv.VideoCapture(1)

while True:
    _, frame = cap.read()
    copyFrame = frame.copy()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    image, board_detected = detChecker(
        frame, gray, criteria, CHESS_BOARD_DIM)
    # print(ret)
    cv.putText(
        frame,
        f"saved_img : {n}",
        (30, 40),
        cv.FONT_HERSHEY_PLAIN,
        1.4,
        (0, 255, 0),
        2,
        cv.LINE_AA,
    )

    cv.imshow("frame", frame)
    cv.imshow("copyFrame", copyFrame)

    key = cv.waitKey(1)

    if key == ord("q"):
        break
    if key == ord("s") and board_detected == True:
        # storing the checker board image
        cv.imwrite(f"ArucoMarkers/CallibrateImages/image{n}.png", copyFrame)

        print(f"saved image number {n}")
        n += 1  # incrementing the image counter
cap.release()
cv.destroyAllWindows()

print("Total saved Images:", n)
