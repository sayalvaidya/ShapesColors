import cv2
from playsound import playsound

class ShapeDetector:
    def __init__(self):
        pass

    def detect(self, c):

        shape = "unidentified"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)


        if len(approx) == 3:
            shape = "TRIANGLE"
            # if shape=="TRIANGLE":
            #     playsound('/Users/sayalvaidya/PycharmProjects/ShapesColors/static/audio/Triangle1.m4a')




        elif len(approx) == 4:

            (x, y, w, h) = cv2.boundingRect(approx)
            ar = w / float(h)


            shape = "SQUARE" if ar >= 0.95 and ar <= 1.05 else "RECTANGLE"
            # if shape=="SQUARE":
            #     playsound('/Users/sayalvaidya/PycharmProjects/ShapesColors/static/audio/Square.m4a')
            # else:
            #     playsound('/Users/sayalvaidya/PycharmProjects/ShapesColors/static/audio/Rectangle.m4a')



        elif len(approx) == 5:
            shape = "PENTAGON"
            # if shape == "PENTAGON":
            #  playsound('/Users/sayalvaidya/PycharmProjects/ShapesColors/static/audio/Pentagon.m4a')


        # elif len(approx)==6:
        #     shape = "CIRCLE"
        #
        # elif len(approx)==7:
        #     shape = "SEPTAGON"
        #
        # elif len(approx)==8:
        #     shape = "OCTAGON"
        #
        # # elif len(approx)==9:
        # #     shape = "UNKNOWN SHAPE"

        else:
            shape ="CIRCLE"
            # if shape=="CIRCLE":
            #     playsound('/Users/sayalvaidya/PycharmProjects/ShapesColors/static/audio/Circle.m4a')
            #



        return shape