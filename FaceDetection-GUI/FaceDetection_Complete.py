"""
Heres the command for turning the QT-Creator file into a Python-File. Make sure that you first delete the existing file.

pyuic5 mainwindow.ui -o MainWindow.py <- Enter it into the terminal here in pycharm

pyrcc5 GUI_Ressources.qrc -o GUI_Ressources_rc.py <- Enter this in terminal for the ressource file

"""

#Handle the imports

import sys
from PyQt5 import QtWidgets, uic, QtCore

from PyQt5.QtGui import *

import cv2
import numpy as np
import math

import filter_Task5 as filter

from MainWindow import Ui_MainWindow


#Start of the code
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        #Connect all the  buttons

        self.button_filter_anwenden = self.findChild(QtWidgets.QLabel, 'label_filter_anwenden')
        self.button_filter_anwenden.mousePressEvent = self.pushButton_label_filter_anwenden

        self.button_similarity_aktualisieren = self.findChild(QtWidgets.QLabel, 'label_aktualisieren')
        self.button_similarity_aktualisieren.mousePressEvent = self.pushButton_label_similarity_aktualisieren

        self.button_facedetection_anwenden = self.findChild(QtWidgets.QLabel, 'label_facedetection_anwenden')
        self.button_facedetection_anwenden.mousePressEvent = self.pushButton_label_facedetection_anwenden


        self.dropdown_type = self.findChild(QtWidgets.QComboBox, "comboBox_filetype")
        self.dropdown_type.currentIndexChanged.connect(self.dropdown_type_changed)

        self.dropdown_method = self.findChild(QtWidgets.QComboBox, "comboBox_method")
        self.dropdown_method.currentIndexChanged.connect(self.dropdown_method_changed)

        self.dropdown_facedetection = self.findChild(QtWidgets.QComboBox, "comboBox_facedetection")
        self.dropdown_facedetection.currentIndexChanged.connect(self.dropdown_facedetection_changed)

        self.radioButton_blur = self.findChild(QtWidgets.QRadioButton, "radioButton_blur")
        self.radioButton_blur.setChecked(True)
        self.radioButton_blur.toggled.connect(self.radioButton_blur_toggled)

        self.radioButton_invert = self.findChild(QtWidgets.QRadioButton, "radioButton_invert")
        self.radioButton_invert.toggled.connect(self.radioButton_invert_toggled)

        self.radioButton_preventfd = self.findChild(QtWidgets.QRadioButton, "radioButton_preventfd")
        self.radioButton_preventfd.toggled.connect(self.radioButton_preventfd_toggled)

        self.label_loadimage = self.findChild(QtWidgets.QLabel, "label_filter_loadimage")
        self.label_loadimage.mousePressEvent = self.pushButton_label_loadimage

        self.label_result_display = self.findChild(QtWidgets.QLabel, "label_result_display")

        self.label_img_before = self.findChild(QtWidgets.QLabel, "label_img_before")

        self.label_img_after = self.findChild(QtWidgets.QLabel, "label_img_after")


#Define all the functions

    def pushButton_label_facedetection_anwenden(self, event):
        global facedection_type
        global image_before

        if facedection_type == "Face Detection 1":
            m = myFaceDetector1(image_before)
            m.load()

        if facedection_type == "Face Detection 2":
            m = myFaceDetector2(image_before)
            m.load()

    def pushButton_label_filter_anwenden(self, event):
        global filter_type
        global coordinates
        global boost
        global image_before
        global image_after
        global array_before
        global array_after
        global img
        global FileName

        img = cv2.imread(image_before)
        if filter_type == "blur":
            image_after = applyBlur(img)

        if filter_type == "Invert":
            image_after = applyInvert(image_before)

        cv2.imwrite('edited_' + image_before[image_before.rfind("/") + 1:], array_after)

        image_after = image_before[:image_before.rfind("/") + 1] + "edited_" + image_before[image_before.rfind("/") + 1:]

        self.label_img_after.setPixmap(QPixmap(image_after))
        self.label_img_after.setScaledContents(True)
        self.label_img_after.setMaximumWidth(281)
        self.label_img_after.setMaximumHeight(241)

    def pushButton_label_similarity_aktualisieren(self, event):
        global result
        global similarity_type
        global similarity_method
        global image_before
        global image_after
        global array_before
        global array_after

        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        if similarity_method == "rms":
            result = round(rms(array_before, array_after, similarity_type),2)

        if similarity_method == "chebyshev":
            result = round(chebyshev(array_before, array_after, similarity_type),2)


        if similarity_method == "binary":
            result = round(binary(array_before, array_after, similarity_type),2)

        self.label_result_display.setText("{}%".format(result))


    def dropdown_type_changed(self):
        global similarity_type
        similarity_type = self.dropdown_type.currentText()

    def dropdown_method_changed(self):
        global similarity_method
        similarity_method = self.dropdown_method.currentText()

    def dropdown_facedetection_changed(self):
        global facedetection_type
        facedetection_type = self.dropdown_facedetection.currentText()

    def radioButton_blur_toggled(self):
        global filter_type
        filter_type_blur = self.sender()
        if filter_type_blur.isChecked():
            filter_type = "blur"

    def radioButton_invert_toggled(self):
        global filter_type
        filter_type_invert = self.sender()
        if filter_type_invert.isChecked():
            filter_type = "invert"

    def radioButton_preventfd_toggled(self):
        global filter_type
        filter_type_preventfd = self.sender()
        if filter_type_preventfd.isChecked():
            filter_type = "preventfd"

    def pushButton_label_loadimage(self, event):
        global image
        global image_before
        global image_after
        global FilePath
        global img


        FilePath = QtWidgets.QFileDialog.getOpenFileName(self, 'Select folder');

        image = FilePath
        image_before = image[0]
        image_after = image[0]
        LastDashInImage = image_before.rfind("/")
        image = image_before[LastDashInImage + 1:]

        img = image_before

        self.label_img_before.setPixmap(QPixmap(image_before))
        self.label_img_before.setScaledContents(True)
        self.label_img_before.setMaximumWidth(281)
        self.label_img_before.setMaximumHeight(241)

        m = Main(image, 1)
        m.load()

        self.label_img_after.setPixmap(QPixmap(image_after))
        self.label_img_after.setScaledContents(True)
        self.label_img_after.setMaximumWidth(281)
        self.label_img_after.setMaximumHeight(241)


#Introduce all the global variables

result = 100
image = None
similarity_type = "Image"
similarity_method = "rms"
facedetection_type = "Face Detection 1"
filter_type = "blur"
FilePath = None
FileName = "No File"
coordinates = None
boost = None
image_before = None
image_after = None
array_before = None
array_after = None
img = None
facedection_type = None


def convert(original, modified):

    # if the image is color, convert to grayscale
    if len(original.shape) == 3:
        original = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
        modified = cv2.cvtColor(modified, cv2.COLOR_BGR2GRAY)

    # convert to float
    original = original.astype(np.float32)
    modified = modified.astype(np.float32)

    return original, modified


def diffvector(original, modified, space):
    global array_before
    global array_after
    global similarity_type

    # calculate difference vector between original and
    # modified image in chosen space
    if similarity_type == "Image":
        difference = array_before - array_after
    elif similarity_type == "histogram":
        hist_orig = cv2.calcHist([array_before], [0], None, [256], [0, 256])
        hist_modif = cv2.calcHist([array_before], [0], None, [256], [0, 256])
        difference = hist_orig - hist_modif
    else:
        difference = 0

    return difference


def rms(original, modified, space="image"):
    global array_before
    global array_after
    global similarity_type

    '''
    this function calculates the rms error between two images
    the error calculation can either be done in image space or in histogram space
    output is scaled relative to the average input values
    output can be interpreted as a measure how much information was changed globally
    '''
    # convert image to grayscale and float
    array_before, array_after = convert(array_before, array_after)

    # calculate difference vector
    difference = diffvector(array_before, array_after, similarity_type)

    # scale difference
    if similarity_type == "Image":
        scale = np.sum(array_before) / array_before.size
        difference = difference / scale
    if similarity_type == "histogram":
        hist_orig = cv2.calcHist([array_before], [0], None, [256], [0, 256])
        scale = np.sum(hist_orig) / hist_orig.size
        difference = difference / scale

    # calculate rootmeansquare difference
    difference_squared = np.multiply(difference, difference)
    rms_error = math.sqrt(np.sum(difference_squared)/difference_squared.size)

    return rms_error

def chebyshev(original, modified, space="image"):
    global array_before
    global array_after
    global similarity_type

    '''
    this function calculates the maximal difference between two images
    the calculation can be done either in image space or in histogram space
    output is scaled relative to the input value
    output can be interpreted as a measure how much information was changed locally
    '''
    # convert image to grayscale and float
    array_before, array_after = convert(array_before, array_after)

    # calculate difference vector
    difference = abs(diffvector(array_before, array_after, similarity_type))

    # calculate chebyshev distance and where it occurs
    max_diff = np.amax(difference)
    max_diff_ind = np.unravel_index(np.argmax(difference, axis=None), difference.shape)

    # scale difference
    if similarity_type == "Image":
        scale = original[max_diff_ind]
        chebyshev_error = max_diff / scale
    if similarity_type == "Histogram":
        hist_orig = cv2.calcHist([array_before], [0], None, [256], [0, 256])
        scale = hist_orig[max_diff_ind]
        chebyshev_error = max_diff / scale

    return chebyshev_error

def binary(original, modified, space="image"):

    global array_before
    global array_after
    global similarity_type

    '''
    this function calculates the percentage of pixels that have changed
    the calculation can be done either in image space or in histogram space
    output can be interpreted as a measure of how homogenous/inhomogenous
    the image changes are.
    output close to 1 means homogenous, close to 0 means inhomogenous
    '''
    # convert image to grayscale and float
    array_before, array_after = convert(array_before, array_after)

    # calculate difference vector
    difference = diffvector(array_before, array_after, similarity_type)

    # calculate number of altered pixels
    nonzeros = np.count_nonzero(difference)

    return nonzeros / difference.size

class Main(object):
    def __init__(self, imgName, boost):
        self.boost = boost
        self.filter = filter.Filter()
        self.img_name = imgName

    def load(self):
        global FilePath
        global FileName
        global image_before
        global image_after
        global array_before
        global array_after
        global coordinates

        # Load the cascade
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        print(image_before)

        # Read the input image
        # img_name = sys.argv[1]
        print(self.img_name)
        img = cv2.imread(image_before)

        print("Test")
        print(img)
        #img = cv2.cvtColor(cv2.imread(self.img_name), cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(img, 1.1, 4)
        coordinates = faces

        # Detect faces
        faces = face_cascade.detectMultiScale(img, 1.1, 4)

        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Display the output

        cv2.imwrite('edited_' + self.img_name, img)

        image_after = image_before[:image_before.rfind("/")+1] + "edited_" + self.img_name


        """
        array_before = cv2.cvtColor(cv2.imread(image_before), cv2.COLOR_BGR2GRAY)
        array_after = cv2.cvtColor(cv2.imread(image_after), cv2.COLOR_BGR2GRAY)
        """
        cv2.waitKey()

def applyBlur(image):
    '''
    Applies a blur filter to the specified image areas
    :param image: complet image
    :param coordinates: areas to be blurred
    :param boost: intensity of the blurdness
    :return: new image with the blured areas
    '''

    global coordinates
    global boost
    global image_before
    global image_after
    global array_before
    global array_after
    global coordinates

    # self.optimum(image)
    new_image = image
    x = coordinates[0][0]
    y = coordinates[0][1]
    w = coordinates[0][2]
    h = coordinates[0][3]


    crop_img = image[y:y + h, x:x + w]
    # blur_img = self.applyInvert(crop_img, 0)
    # blur_img = self.shiftPixels(crop_img)
    # blur_img = cv2.blur(crop_img, (15, 15))
    # blur_img = self.applyPreventFD(crop_img)
    #crop_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
    a, b, c = cv2.split(crop_img)

    a = beat_Filter(a)
    b = beat_Filter(b)
    c = beat_Filter(c)

    crop_img = cv2.merge((a,b,c))


    #blur_img = beat_Filter(crop_img)
    new_image[y:y + h, x:x + w] = crop_img

    return new_image


def beat_Filter(image, dunkel=90, hell=200):
    dunkel = dunkel
    hell = hell
    levelBlack = 285
    levelWhite = 235
    newImage = image
    for i in range(1, image.shape[0] - 1):
        for j in range(1, image.shape[1] - 1):
            if i % 1 == 0 and j % 1 == 0:
                currPix = newImage[i, j]
                if currPix > hell:
                    newImage[i, j] = levelBlack - currPix
                    continue
                if int(image[i, j]) < dunkel:
                    newImage[i, j] = levelWhite - currPix
            j += 1
        i += 1
    return image


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
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
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

class myFaceDetector2(object):
    def __init__(self, imgName, boost):
        self.img_name = imgName
        self.boost = boost
        self.filter = filter.Filter()

    def load(self):
        #Built-in function to read the xml-files and load the trained flies for detecting the face and eyes
        face_cascade = cv2.CascadeClassifier( 'haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

        #reading the image
        img = cv2.imread(self.img_name)
        #Convert image into grayscale
        #Its easier to detect a face in grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(img, 1.1, 4)
        # blur defined areas in a picture
        for (x, y, w, h) in faces:
            # Method: apply() from class: Filter
            gray = self.filter.apply(img, [x, y, w, h], [self.boost, self.boost])

        #face detection
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        #Draw rectangle around the faces --> x= starting point at xlim, y= starting point at ylim, w= width, h= height
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        #eye detection
        eyes = eye_cascade.detectMultiScale(gray, 1.1, 4)
        #Draw rectangle around the eyes, only if eye are in the face area
        for (ex, ey, ew, eh) in eyes:
            if (ex + ew) < (x + w) and (ey + eh) < (y + h):
                cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            else: print("eye not in face area detected")

        #Display the image on the window
        cv2.imwrite('edited_' + self.img_name, img)
        cv2.imshow('img', img)

        # Print error
        print(calc_diff.rms(cv2.imread(self.img_name), img))
        cv2.waitKey()


#Display QT Window
app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
