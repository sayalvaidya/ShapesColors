
import cap as cap
import cv2
import numpy as np


def live_Color():
    cam = cv2.VideoCapture(0)
    while (1):

        _, img = cam.read()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # definig the range of red color
        red_lower = np.array([136, 87, 111], np.uint8)
        red_upper = np.array([180, 255, 255], np.uint8)

        # defining the Range of Blue color
        blue_lower = np.array([99, 115, 150], np.uint8)
        blue_upper = np.array([110, 255, 255], np.uint8)

        # defining the Range of yellow color
        yellow_lower = np.array([22, 60, 200], np.uint8)
        yellow_upper = np.array([60, 255, 255], np.uint8)

        green_lower = np.array([65, 60, 60], np.uint8)
        green_upper = np.array([80, 255, 255], np.uint8)

        white_lower = np.array([255, 255, 255], np.uint8)
        white_upper = np.array([255, 255, 255], np.uint8)

        # finding the range  of red,blue, green and yellow color in the image
        red = cv2.inRange(hsv, red_lower, red_upper)
        blue = cv2.inRange(hsv, blue_lower, blue_upper)
        yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)
        green = cv2.inRange(hsv, green_lower, green_upper)
        white = cv2.inRange(hsv, white_lower, white_upper)

        # Morphological transformation, Dilation
        kernal = np.ones((5, 5), "uint8")

        red = cv2.dilate(red, kernal)
        res = cv2.bitwise_and(img, img, mask=red)

        blue = cv2.dilate(blue, kernal)
        res1 = cv2.bitwise_and(img, img, mask=blue)

        yellow = cv2.dilate(yellow, kernal)
        res2 = cv2.bitwise_and(img, img, mask=yellow)

        green = cv2.dilate(green, kernal)
        res2 = cv2.bitwise_and(img, img, mask=green)

        white = cv2.dilate(white, kernal)
        res2 = cv2.bitwise_and(img, img, mask=white)

        # Tracking the Red Color
        (ti, contours, hierarchy) = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE[, contours[, hierarchy[, offset]]])
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(img, "RED", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

                # Tracking the Blue Color
        (ti, contours, hierarchy) = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(img, "BLUE", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

                # Tracking the yellow Color
        (ti, contours, hierarchy) = cv2.findContours(yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 255), 2)
                cv2.putText(img, "YELLOW", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        (ti, contours, hierarchy) = cv2.findContours(green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(img, "GREEN", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        (ti, contours, hierarchy) = cv2.findContours(white, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if (area > 300):
                x, y, w, h = cv2.boundingRect(contour)
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(img, "WHITE", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # cv2.imshow("Redcolour",red)
        cv2.imshow("Color Tracking", img)
        # # cv2.imwrite(UPLOAD_OUTPUT + filename, img)
        # # cv2.imshow("red",res)
        #
        if cv2.waitKey(10) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()

            break



    # def __del__(self):
    #     self.cam.release()
    #
    # def get_frame(self):
    #     success, img = self.cam.read()
    #     # We are using Motion JPEG, but OpenCV defaults to capture raw images,
    #     # so we must encode it into JPEG in order to correctly display the
    #     # video stream.
    #     ret, jpeg = cv2.imencode('.jpg', img)
    #     return jpeg.tobytes()







