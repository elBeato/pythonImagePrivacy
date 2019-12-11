# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(802, 728)
        MainWindow.setStyleSheet("#label_logo{\n"
"background:white;\n"
"}\n"
"\n"
"#frame{\n"
"background:rgba(255,255,255,200);\n"
"border-radius:25px;\n"
"border-style:solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"}\n"
"\n"
"#frame_similarity{\n"
"background:white;\n"
"border-radius:10px;\n"
"border-style:solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"}\n"
"\n"
"#frame_filter{\n"
"background:white;\n"
"border-radius:10px;\n"
"border-style:solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"}\n"
"\n"
"#frame_facedetection{\n"
"background:white;\n"
"border-radius:10px;\n"
"border-style:solid;\n"
"border-width: 1px;\n"
"border-color:black;\n"
"}\n"
"\n"
"\n"
"#label_line_1{\n"
"background:rgba(14,11,101,220);\n"
"color: white;\n"
"vertical-align: middle;\n"
"border-radius:13px;\n"
"}\n"
"\n"
"#label_line_2{\n"
"background:rgba(14,11,101,220);\n"
"color: white;\n"
"vertical-align: middle;\n"
"border-radius:13px;\n"
"}\n"
"\n"
"#label_title_before{\n"
"background:rgba(137,136,191,250);\n"
"color: white;\n"
"vertical-align: middle;\n"
"border-radius:5px;\n"
"padding-left: 10 px;\n"
"}\n"
"\n"
"\n"
"#label_title_after{\n"
"background:rgba(137,136,191,250);\n"
"color: white;\n"
"vertical-align: middle;\n"
"border-radius:5px;\n"
"padding-right: 10 px;\n"
"}\n"
"\n"
"#label_title_similarity{\n"
"background:rgba(14,11,101,220);\n"
"color: white;\n"
"vertical-align: middle;\n"
"border-radius:3px;\n"
"}\n"
"\n"
"#label_title_filter{\n"
"background:rgba(14,11,101,220);\n"
"color: white;\n"
"vertical-align: middle;\n"
"border-radius:3px;\n"
"}\n"
"\n"
"#label_title_facedetection{\n"
"background:rgba(14,11,101,220);\n"
"color: white;\n"
"vertical-align: middle;\n"
"border-radius:3px;\n"
"}\n"
"\n"
"QWidget{\n"
"background:url(:/GUI_Ressources/image_background3.png);\n"
"}\n"
"\n"
"#label_choose_filetype{\n"
"background:rgba(27,27,27,30);\n"
"border-radius:3px;\n"
"color: black;\n"
"padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"#label_choose_filter{\n"
"background:rgba(27,27,27,30);\n"
"border-radius:3px;\n"
"color: black;\n"
"padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"#label_choose_facedetection{\n"
"background:rgba(27,27,27,30);\n"
"border-radius:3px;\n"
"color: black;\n"
"border-color:black;\n"
"border-width:1px;\n"
"padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"#label_result{\n"
"background:rgba(27,27,27,30);\n"
"border-radius:3px;\n"
"color: black;\n"
"padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"#label_result_display{\n"
"background:transparent;\n"
"border-style:solid;\n"
"border-width:1.2px;\n"
"border-color:rgba(27,27,27,100);\n"
"border-radius:3px;\n"
"color: black;\n"
"}\n"
"\n"
"\n"
"#label_aktualisieren{\n"
"background:rgba(137,136,191,250);\n"
"border-radius:3px;\n"
"color: white;\n"
"}\n"
"\n"
"#label_aktualisieren:hover{\n"
"background:white;\n"
"border-radius:3px;\n"
"border-style:solid;\n"
"border-width:1.5px;\n"
"border-color:rgba(137,136,191,250);\n"
"color: black;\n"
"}\n"
"\n"
"#label_filter_anwenden{\n"
"background:rgba(137,136,191,250);\n"
"border-radius:3px;\n"
"color: white;\n"
"}\n"
"\n"
"#label_filter_anwenden:hover{\n"
"background:white;\n"
"border-radius:3px;\n"
"border-style:solid;\n"
"border-width:1.5px;\n"
"border-color:rgba(137,136,191,250);\n"
"color: black;\n"
"}\n"
"\n"
"#label_facedetection_anwenden{\n"
"background:rgba(137,136,191,250);\n"
"border-radius:3px;\n"
"color: white;\n"
"}\n"
"\n"
"#label_facedetection_anwenden:hover{\n"
"background:white;\n"
"border-radius:3px;\n"
"border-style:solid;\n"
"border-width:1.5px;\n"
"border-color:rgba(137,136,191,250);\n"
"color: black;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"#label_filter_loadimage{\n"
"background:#03013A;\n"
"border-radius:5px;\n"
"border-style:solid;\n"
"border-width:1.5px;\n"
"border-color:black;\n"
"color: white;\n"
"}\n"
"\n"
"#label_filter_loadimage:hover{\n"
"background:white;\n"
"border-radius:5px;\n"
"border-style:solid;\n"
"border-width:1.5px;\n"
"border-color:#03013A;\n"
"color: #03013A;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"#label_change_display{\n"
"background:transparent;\n"
"border-style:solid;\n"
"border-color:black;\n"
"color: white;\n"
"}\n"
"\n"
"#comboBox_filter{}\n"
"\n"
"\n"
"#label_img_before{\n"
"background:white;\n"
"border-style:solid;\n"
"border-color:black;\n"
"border-width:3px;\n"
"}\n"
"\n"
"\n"
"#label_img_after{\n"
"background:white;\n"
"border-style:solid;\n"
"border-color:black;\n"
"border-width:3px;\n"
"}\n"
"\n"
"QComboBox{\n"
"border-style:solid;\n"
"border-color:black;\n"
"border-width:0.5px;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"border-width:0px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"color:green;\n"
"}\n"
"\n"
"QRadioButton{\n"
"background: rgba(27,27,27,30);\n"
"border-style:solid;\n"
"border-width:0.5 px;\n"
"border-color:grey;\n"
"\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 10, 761, 621))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_line_1 = QtWidgets.QLabel(self.frame)
        self.label_line_1.setGeometry(QtCore.QRect(53, 70, 649, 2))
        font = QtGui.QFont()
        font.setFamily(".Farah PUA")
        font.setPointSize(28)
        self.label_line_1.setFont(font)
        self.label_line_1.setText("")
        self.label_line_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_line_1.setObjectName("label_line_1")
        self.label_img_before = QtWidgets.QLabel(self.frame)
        self.label_img_before.setGeometry(QtCore.QRect(53, 110, 281, 241))
        self.label_img_before.setText("")
        self.label_img_before.setPixmap(QtGui.QPixmap(":/GUI_Ressources/image_test_before.png"))
        self.label_img_before.setScaledContents(True)
        self.label_img_before.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img_before.setObjectName("label_img_before")
        self.label_img_after = QtWidgets.QLabel(self.frame)
        self.label_img_after.setGeometry(QtCore.QRect(420, 110, 281, 241))
        self.label_img_after.setText("")
        self.label_img_after.setPixmap(QtGui.QPixmap(":/GUI_Ressources/image_test_after.png"))
        self.label_img_after.setScaledContents(True)
        self.label_img_after.setAlignment(QtCore.Qt.AlignCenter)
        self.label_img_after.setObjectName("label_img_after")
        self.label_title_before = QtWidgets.QLabel(self.frame)
        self.label_title_before.setGeometry(QtCore.QRect(30, 100, 191, 21))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(12)
        self.label_title_before.setFont(font)
        self.label_title_before.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_title_before.setObjectName("label_title_before")
        self.label_title_after = QtWidgets.QLabel(self.frame)
        self.label_title_after.setGeometry(QtCore.QRect(540, 100, 191, 21))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(12)
        self.label_title_after.setFont(font)
        self.label_title_after.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_title_after.setObjectName("label_title_after")
        self.frame_similarity = QtWidgets.QFrame(self.frame)
        self.frame_similarity.setGeometry(QtCore.QRect(500, 420, 241, 181))
        self.frame_similarity.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_similarity.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_similarity.setObjectName("frame_similarity")
        self.comboBox_method = QtWidgets.QComboBox(self.frame_similarity)
        self.comboBox_method.setGeometry(QtCore.QRect(90, 80, 141, 21))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(11)
        font.setKerning(True)
        self.comboBox_method.setFont(font)
        self.comboBox_method.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_method.setMaxVisibleItems(20)
        self.comboBox_method.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox_method.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox_method.setObjectName("comboBox_method")
        self.comboBox_method.addItem("")
        self.comboBox_method.addItem("")
        self.comboBox_method.addItem("")
        self.label_result_display = QtWidgets.QLabel(self.frame_similarity)
        self.label_result_display.setGeometry(QtCore.QRect(90, 110, 141, 22))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_result_display.setFont(font)
        self.label_result_display.setText("")
        self.label_result_display.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result_display.setObjectName("label_result_display")
        self.label_choose_filter = QtWidgets.QLabel(self.frame_similarity)
        self.label_choose_filter.setGeometry(QtCore.QRect(10, 80, 61, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_choose_filter.setFont(font)
        self.label_choose_filter.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_choose_filter.setObjectName("label_choose_filter")
        self.label_result = QtWidgets.QLabel(self.frame_similarity)
        self.label_result.setGeometry(QtCore.QRect(10, 110, 61, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_result.setFont(font)
        self.label_result.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_result.setObjectName("label_result")
        self.label_aktualisieren = QtWidgets.QLabel(self.frame_similarity)
        self.label_aktualisieren.setGeometry(QtCore.QRect(10, 140, 221, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_aktualisieren.setFont(font)
        self.label_aktualisieren.setAlignment(QtCore.Qt.AlignCenter)
        self.label_aktualisieren.setObjectName("label_aktualisieren")
        self.label_choose_filetype = QtWidgets.QLabel(self.frame_similarity)
        self.label_choose_filetype.setGeometry(QtCore.QRect(10, 50, 61, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_choose_filetype.setFont(font)
        self.label_choose_filetype.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_choose_filetype.setObjectName("label_choose_filetype")
        self.comboBox_filetype = QtWidgets.QComboBox(self.frame_similarity)
        self.comboBox_filetype.setGeometry(QtCore.QRect(90, 50, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_filetype.setFont(font)
        self.comboBox_filetype.setObjectName("comboBox_filetype")
        self.comboBox_filetype.addItem("")
        self.comboBox_filetype.addItem("")
        self.label_title_similarity = QtWidgets.QLabel(self.frame_similarity)
        self.label_title_similarity.setGeometry(QtCore.QRect(10, 10, 221, 31))
        font = QtGui.QFont()
        font.setFamily(".Farah PUA")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_title_similarity.setFont(font)
        self.label_title_similarity.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_similarity.setObjectName("label_title_similarity")
        self.frame_filter = QtWidgets.QFrame(self.frame)
        self.frame_filter.setGeometry(QtCore.QRect(290, 420, 181, 181))
        self.frame_filter.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_filter.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_filter.setObjectName("frame_filter")
        self.label_filter_anwenden = QtWidgets.QLabel(self.frame_filter)
        self.label_filter_anwenden.setGeometry(QtCore.QRect(10, 140, 161, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_filter_anwenden.setFont(font)
        self.label_filter_anwenden.setAlignment(QtCore.Qt.AlignCenter)
        self.label_filter_anwenden.setObjectName("label_filter_anwenden")
        self.label_title_filter = QtWidgets.QLabel(self.frame_filter)
        self.label_title_filter.setGeometry(QtCore.QRect(10, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily(".Farah PUA")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_title_filter.setFont(font)
        self.label_title_filter.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_filter.setObjectName("label_title_filter")
        self.radioButton_blur = QtWidgets.QRadioButton(self.frame_filter)
        self.radioButton_blur.setGeometry(QtCore.QRect(10, 50, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_blur.setFont(font)
        self.radioButton_blur.setObjectName("radioButton_blur")
        self.radioButton_invert = QtWidgets.QRadioButton(self.frame_filter)
        self.radioButton_invert.setGeometry(QtCore.QRect(10, 80, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_invert.setFont(font)
        self.radioButton_invert.setObjectName("radioButton_invert")
        self.radioButton_preventfd = QtWidgets.QRadioButton(self.frame_filter)
        self.radioButton_preventfd.setGeometry(QtCore.QRect(10, 110, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.radioButton_preventfd.setFont(font)
        self.radioButton_preventfd.setObjectName("radioButton_preventfd")
        self.label_logo = QtWidgets.QLabel(self.frame)
        self.label_logo.setGeometry(QtCore.QRect(255, 10, 271, 81))
        self.label_logo.setText("")
        self.label_logo.setPixmap(QtGui.QPixmap(":/GUI_Ressources/Facedetect_logo2.png"))
        self.label_logo.setScaledContents(True)
        self.label_logo.setObjectName("label_logo")
        self.frame_facedetection = QtWidgets.QFrame(self.frame)
        self.frame_facedetection.setGeometry(QtCore.QRect(20, 420, 241, 181))
        self.frame_facedetection.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_facedetection.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_facedetection.setObjectName("frame_facedetection")
        self.label_title_facedetection = QtWidgets.QLabel(self.frame_facedetection)
        self.label_title_facedetection.setGeometry(QtCore.QRect(10, 10, 221, 31))
        font = QtGui.QFont()
        font.setFamily(".Farah PUA")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(False)
        self.label_title_facedetection.setFont(font)
        self.label_title_facedetection.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title_facedetection.setObjectName("label_title_facedetection")
        self.label_choose_facedetection = QtWidgets.QLabel(self.frame_facedetection)
        self.label_choose_facedetection.setGeometry(QtCore.QRect(10, 50, 61, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_choose_facedetection.setFont(font)
        self.label_choose_facedetection.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_choose_facedetection.setObjectName("label_choose_facedetection")
        self.comboBox_facedetection = QtWidgets.QComboBox(self.frame_facedetection)
        self.comboBox_facedetection.setGeometry(QtCore.QRect(90, 51, 141, 21))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(11)
        font.setKerning(True)
        self.comboBox_facedetection.setFont(font)
        self.comboBox_facedetection.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_facedetection.setMaxVisibleItems(20)
        self.comboBox_facedetection.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox_facedetection.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox_facedetection.setObjectName("comboBox_facedetection")
        self.comboBox_facedetection.addItem("")
        self.comboBox_facedetection.addItem("")
        self.comboBox_facedetection.addItem("")
        self.label_facedetection_anwenden = QtWidgets.QLabel(self.frame_facedetection)
        self.label_facedetection_anwenden.setGeometry(QtCore.QRect(10, 140, 221, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_facedetection_anwenden.setFont(font)
        self.label_facedetection_anwenden.setAlignment(QtCore.Qt.AlignCenter)
        self.label_facedetection_anwenden.setObjectName("label_facedetection_anwenden")
        self.label_filter_loadimage = QtWidgets.QLabel(self.frame)
        self.label_filter_loadimage.setGeometry(QtCore.QRect(305, 370, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_filter_loadimage.setFont(font)
        self.label_filter_loadimage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_filter_loadimage.setObjectName("label_filter_loadimage")
        self.label_line_2 = QtWidgets.QLabel(self.frame)
        self.label_line_2.setGeometry(QtCore.QRect(40, 385, 649, 2))
        font = QtGui.QFont()
        font.setFamily(".Farah PUA")
        font.setPointSize(28)
        self.label_line_2.setFont(font)
        self.label_line_2.setText("")
        self.label_line_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_line_2.setObjectName("label_line_2")
        self.label_logo.raise_()
        self.frame_similarity.raise_()
        self.label_img_before.raise_()
        self.label_img_after.raise_()
        self.label_title_before.raise_()
        self.label_title_after.raise_()
        self.frame_filter.raise_()
        self.label_line_1.raise_()
        self.frame_facedetection.raise_()
        self.label_line_2.raise_()
        self.label_filter_loadimage.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 802, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.comboBox_method.setCurrentIndex(0)
        self.comboBox_filetype.setCurrentIndex(0)
        self.comboBox_facedetection.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title_before.setText(_translate("MainWindow", "Before"))
        self.label_title_after.setText(_translate("MainWindow", "After"))
        self.comboBox_method.setItemText(0, _translate("MainWindow", "rms"))
        self.comboBox_method.setItemText(1, _translate("MainWindow", "chebyshev"))
        self.comboBox_method.setItemText(2, _translate("MainWindow", "binary"))
        self.label_choose_filter.setText(_translate("MainWindow", "Method:"))
        self.label_result.setText(_translate("MainWindow", "Result:"))
        self.label_aktualisieren.setText(_translate("MainWindow", "Aktualisieren"))
        self.label_choose_filetype.setText(_translate("MainWindow", "Type:"))
        self.comboBox_filetype.setItemText(0, _translate("MainWindow", "Image"))
        self.comboBox_filetype.setItemText(1, _translate("MainWindow", "Histogram"))
        self.label_title_similarity.setText(_translate("MainWindow", "Similarity"))
        self.label_filter_anwenden.setText(_translate("MainWindow", "Anwenden"))
        self.label_title_filter.setText(_translate("MainWindow", "Filter"))
        self.radioButton_blur.setText(_translate("MainWindow", "Blur"))
        self.radioButton_invert.setText(_translate("MainWindow", "Invert"))
        self.radioButton_preventfd.setText(_translate("MainWindow", "Prevent FD"))
        self.label_title_facedetection.setText(_translate("MainWindow", "Face Detection"))
        self.label_choose_facedetection.setText(_translate("MainWindow", "Method:"))
        self.comboBox_facedetection.setItemText(0, _translate("MainWindow", "Face Detection 1"))
        self.comboBox_facedetection.setItemText(1, _translate("MainWindow", "Face Detection 2"))
        self.comboBox_facedetection.setItemText(2, _translate("MainWindow", "Face Detection 3"))
        self.label_facedetection_anwenden.setText(_translate("MainWindow", "Anwenden"))
        self.label_filter_loadimage.setText(_translate("MainWindow", "Load Image"))

import GUI_Ressources_rc
