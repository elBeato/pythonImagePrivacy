"""
Heres the command for turning the QT-Creator file into a Python-File. Make sure that you first delete the existing file.

pyuic5 mainwindow.ui -o MainWindow.py <- Enter it into the terminal here in pycharm

pyrcc5 GUI_Ressources.qrc -o GUI_Ressources_rc.py <- Enter this in terminal for the ressource file

"""

#Handle the imports

import sys
from PyQt5 import QtWidgets, uic, QtCore
#from PyQt5.QtWidgets import QApplication

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import PIL
from PIL import Image

import glob, os


from MainWindow import Ui_MainWindow


#Start of the code
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        #Connect all the push buttons


        self.button_filter_anwenden = self.findChild(QtWidgets.QLabel, 'label_filter_anwenden')
        self.button_filter_anwenden.mousePressEvent = self.pushButton_label_filter_anwenden

        self.button_similarity_aktualisieren = self.findChild(QtWidgets.QLabel, 'label_aktualisieren')
        self.button_similarity_aktualisieren.mousePressEvent = self.pushButton_label_similarity_aktualisieren

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







        """
        self.button_copy = self.findChild(QtWidgets.QPushButton, 'pushButton_2')
        self.button_copy.clicked.connect(self.pushButtonCopyPressed)

        self.button_filebrowser = self.findChild(QtWidgets.QPushButton, 'pushButton_filebrowser')
        self.button_filebrowser.clicked.connect(self.pushButtonFilebrowserPressed)

        self.button_grab = self.findChild(QtWidgets.QPushButton, 'pushButton_grab')
        self.button_grab.clicked.connect(self.pushButtonGrabPressed)

        #Connect the label that displays the file name
        self.label_filename = self.findChild(QtWidgets.QLabel, "label_filename")
        self.label_filename.setText(FileName)
        self.label_filename.setMargin(5)

        #Connect the input text fields
        self.input_name = self.findChild(QtWidgets.QLineEdit, 'lineEdit')

        self.input_domain = self.findChild(QtWidgets.QLineEdit, 'lineEdit_2')

        self.input_company = self.findChild(QtWidgets.QLineEdit, 'lineEdit_company')

        self.input_function = self.findChild(QtWidgets.QLineEdit, 'lineEdit_function')

        #Connect the text edit field that displays the result
        self.result_window = self.findChild(QtWidgets.QTextEdit, "textEdit")

        #Connect the combo box for the different modes
        self.mode = self.findChild(QtWidgets.QComboBox, "comboBox")
        self.mode.currentIndexChanged.connect(self.modeChanged)

        #Connect the combo box for the different API-Keys
        self.API_Key = self.findChild(QtWidgets.QComboBox, "comboBox_2")
        self.API_Key.currentIndexChanged.connect(self.API_KeyChanged)
        """




#Define all the functions

    def pushButton_label_filter_anwenden(self, event):
        print("OK")

    def pushButton_label_similarity_aktualisieren(self, event):
        global result
        result = 100
        self.label_result_display.setText("{}%".format(result))
        print("OK")

    def dropdown_type_changed(self):
        global similarity_type
        similarity_type = self.dropdown_type.currentText()
        print(similarity_type)

    def dropdown_method_changed(self):
        global similarity_method
        similarity_method = self.dropdown_method.currentText()
        print(similarity_method)

    def dropdown_facedetection_changed(self):
        facedetection_type = self.dropdown_facedetection.currentText()
        print(facedetection_type)

    def radioButton_blur_toggled(self):
        filter_type_blur = self.sender()
        if filter_type_blur.isChecked():
            print("Filter Type: Blur")

    def radioButton_invert_toggled(self):
        filter_type_invert = self.sender()
        if filter_type_invert.isChecked():
            print("Filter Type: Invert")

    def radioButton_preventfd_toggled(self):
        filter_type_preventfd = self.sender()
        if filter_type_preventfd.isChecked():
            print("Filter Type: preventfd")

    def pushButton_label_loadimage(self, event):
        global image
        self.FilePath = QtWidgets.QFileDialog.getOpenFileName(self, 'Select folder');
        image = self.FilePath
        image = image[0]
        #LastDashInImage = image.rfind("/")
        #image = image[LastDashInImage + 1:]

        im = Image.open(image)
        size = 200,200
        pixmap = QPixmap(im.thumbnail(size))

        print(image)
        """

        size = 200,200
        file, ext = os.path.splitext(image)
        pixmap = Image.open(image)
        pixmap = pixmap.thumbnail(size)
        print(pixmap)

        result = 100
        self.label_result_display.setText("{}%".format(result))
        
        """

        #pixmap = QPixmap(image)

        self.label_img_before.setPixmap(pixmap)
        self.label_img_before.setScaledContents(True)
        self.label_img_before.setMaximumWidth(281)
        self.label_img_before.setMaximumHeight(241)

        self.label_img_after.setPixmap(pixmap)
        self.label_img_after.setScaledContents(True)
        self.label_img_after.setMaximumWidth(281)
        self.label_img_after.setMaximumHeight(241)



        print(image)


#Introduce all the global variables

result = 100
image = None
similarity_type = "Image"
similarity_method = "rms"

name_input = None
domain_input = None
result = None
text = None
history = []
color = "green"
access_key = "d33822ae1aaa9387c5355338c15aff5e"
mail = None
FilePath = None
FileName = "No File"
Company = ""
Function = ""



#Display QT Window
app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()

