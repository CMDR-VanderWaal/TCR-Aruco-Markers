
from ast import Index
import cv2 as cv
from cv2 import aruco
import numpy as np

cap = cv.VideoCapture(r"ArucoMarkers\WIN_20221025_21_25_39_Pro.mp4")

params = aruco.DetectorParameters_create()
marker_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = aruco.detectMarkers(frame, marker_dict, parameters=params)
    corners, ids, _ = results
    #print(corners)
    index = 0

    try:
        try:
            for index in ids.flatten():
                corner = corners[index][0]
                print(corner)
        except AttributeError:
            print("No ArucoMarker Detected in frame ! ")
            continue

        """corner - is the List of Cordinates of each Corner Pixel of an Aruco Marker"""
        for i in range(0, len(corner)):
            # print(corner)
            p1 = corner[i]
            j = i+1
            j = j % len(corner)
            p2 = corner[j]

            p1 = np.array(p1, dtype=np.int32)
            p2 = np.array(p2, dtype=np.int32)
            # print("points", p1, p2)
            cv.line(frame, p1, p2, (0, 255, 0), 5)

        cv.namedWindow("Image", cv.WINDOW_NORMAL)
        cv.imshow("Image", frame)
        key = cv.waitKey(1)
    except IndexError:
        continue
    if key == ord("q"):
        break
cap.release()
cv.destroyAllWindows()
