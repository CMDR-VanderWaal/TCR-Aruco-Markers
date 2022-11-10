import cv2 as cv
from cv2 import aruco
import numpy as np

marker_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

param_markers = aruco.DetectorParameters_create()

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
<<<<<<< HEAD
    gray_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    marker_corners, marker_IDs, reject = aruco.detectMarkers(
        gray_frame, marker_dict, parameters=param_markers
    )
    if marker_corners:
        for ids, corners in zip(marker_IDs, marker_corners):
            cv.polylines(
                frame, [corners.astype(np.int32)], True, (0,
                                                          255, 255), 4, cv.LINE_AA
            )
            corners = corners.reshape(4, 2)
            corners = corners.astype(int)
            top_right = corners[0].ravel()
            top_left = corners[1].ravel()
            bottom_right = corners[2].ravel()
            bottom_left = corners[3].ravel()
            cv.putText(
                frame,
                f"id: {ids[0]}",
                top_right,
                cv.FONT_HERSHEY_PLAIN,
                1.3,
                (200, 100, 0),
                2,
                cv.LINE_AA,
            )
            # print(ids, "  ", corners)
    cv.imshow("frame", frame)
    key = cv.waitKey(1)
=======

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
>>>>>>> ce7d1df54a3204173e45cd916e1424e869ccd0ef
    if key == ord("q"):
        break
cap.release()
cv.destroyAllWindows()
