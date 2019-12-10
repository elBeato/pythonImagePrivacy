import cv2
import numpy as np
import filter_Task5 as filter       #File mit allen Methoden zum Filter
import calc_diff

class myFaceDetector1(object):
    def __init__(self, imgName, boost):
        self.img_name = imgName
        self.boost = boost
        self.filter = filter.Filter()

    def load(self):
        #load the trained flies for detecting the face and eyes
        face_cascade = cv2.CascadeClassifier( 'haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

        #reading the image
        img = cv2.imread(self.img_name)
        #Convert image into grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(img, 1.1, 4)
        # blur defined areas in a picture
        for (x, y, w, h) in faces:
            # Method: apply() from class: Filter
           gray = self.filter.apply(img, [x, y, w, h], [self.boost, self.boost])

        """Eye Detector in Face Detector"""
        #face detection
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        #Draw rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

            #eye detection
            eyes = eye_cascade.detectMultiScale(roi_gray)
            #Draw rectangle around the eyes
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        #Display the image on the window
        cv2.imwrite('edited_' + self.img_name, img)
        cv2.imshow('img', img)

        # Print error
        print(calc_diff.rms(cv2.imread(self.img_name), img))
        cv2.waitKey()