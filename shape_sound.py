from playsound import playsound

from main import ShapeDetector
import imutils
import cv2
from os.path import dirname, join, realpath

FIND_FOLDER = join(dirname(realpath(__file__)), 'static/images/')
SHAPE_OUTPUT = join(dirname(realpath(__file__)), 'static/shape_output/')



def sound(filename):

    image = cv2.imread(FIND_FOLDER + filename)

    resized = imutils.resize(image, width=300)
    ratio = image.shape[0] / float(resized.shape[0])
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    sd = ShapeDetector()
    for c in cnts:
        M = cv2.moments(c)
        cX = int((M["m10"] / M["m00"]) * ratio)
        cY = int((M["m01"] / M["m00"]) * ratio)
        shape = sd.detect(c)

        c = c.astype("float")
        c *= ratio
        c = c.astype("int")


    if shape == "TRIANGLE":
        # playsound('/Users/sayalvaidya/PycharmProjects/ShapesColors/static/audio/Triangle1.m4a')
        filename='Triangle1.m4a'
    elif shape == "SQUARE":
        filename='Square.m4a'
        # playsound('/Users/sayalvaidya/PycharmProjects/ShapesColors/static/audio/Square.m4a')
    elif shape == "RECTANGLE":
        filename = 'Rectangle.m4a'
        # playsound('/Users/sayalvaidya/PycharmProjects/ShapesColors/static/audio/Rectangle.m4a')
    elif shape == "PENTAGON":
        filename = 'Pentagon.m4a'
        # playsound('/Users/sayalvaidya/PycharmProjects/ShapesColors/static/audio/Pentagon.m4a')
    elif shape == "CIRCLE":
        # playsound('/Users/sayalvaidya/PycharmProjects/ShapesColors/static/audio/Circle.m4a')
        filename = 'Circle.m4a'
    return filename