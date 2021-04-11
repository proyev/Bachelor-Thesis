# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from str_heat import Ui_Dialog_str_heat
from weighing import Ui_Dialog_weighing
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(539, 432)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.deg_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.deg_spinBox.setMaximum(300)
        self.deg_spinBox.setSingleStep(25)
        self.deg_spinBox.setObjectName("deg_spinBox")
        self.verticalLayout.addWidget(self.deg_spinBox)
        self.rpm_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.rpm_spinBox.setMaximum(1400)
        self.rpm_spinBox.setSingleStep(125)
        self.rpm_spinBox.setObjectName("rpm_spinBox")
        self.verticalLayout.addWidget(self.rpm_spinBox)
        self.sec_spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.sec_spinBox.setMinimum(5)
        self.sec_spinBox.setMaximum(500)
        self.sec_spinBox.setSingleStep(5)
        self.sec_spinBox.setProperty("value", 5)
        self.sec_spinBox.setObjectName("sec_spinBox")
        self.verticalLayout.addWidget(self.sec_spinBox)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.str_label1 = QtWidgets.QLabel(self.centralwidget)
        self.str_label1.setObjectName("str_label1")
        self.verticalLayout_3.addWidget(self.str_label1)
        self.str_label3 = QtWidgets.QLabel(self.centralwidget)
        self.str_label3.setObjectName("str_label3")
        self.verticalLayout_3.addWidget(self.str_label3)
        self.str_label5 = QtWidgets.QLabel(self.centralwidget)
        self.str_label5.setObjectName("str_label5")
        self.verticalLayout_3.addWidget(self.str_label5)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_3)
        self.gridLayout.addLayout(self.formLayout, 7, 0, 2, 1)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.str_label7 = QtWidgets.QLabel(self.centralwidget)
        self.str_label7.setObjectName("str_label7")
        self.gridLayout.addWidget(self.str_label7, 6, 1, 1, 1)
        self.weight_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.weight_pushButton.setObjectName("weight_pushButton")
        self.gridLayout.addWidget(self.weight_pushButton, 3, 1, 1, 1)
        self.titel1_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.titel1_label.setFont(font)
        self.titel1_label.setObjectName("titel1_label")
        self.gridLayout.addWidget(self.titel1_label, 1, 0, 1, 1)
        self.titel2_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.titel2_label.setFont(font)
        self.titel2_label.setObjectName("titel2_label")
        self.gridLayout.addWidget(self.titel2_label, 5, 0, 1, 1)
        self.h_str_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.h_str_pushButton.setObjectName("h_str_pushButton")
        self.gridLayout.addWidget(self.h_str_pushButton, 9, 1, 1, 1)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName("formLayout_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_8.addWidget(self.lineEdit)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.ph_label1 = QtWidgets.QLabel(self.centralwidget)
        self.ph_label1.setObjectName("ph_label1")
        self.verticalLayout_9.addWidget(self.ph_label1)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_9)
        self.gridLayout.addLayout(self.formLayout_2, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.deg_dial = QtWidgets.QDial(self.centralwidget)
        self.deg_dial.setMaximum(300)
        self.deg_dial.setSingleStep(25)
        self.deg_dial.setProperty("value", 0)
        self.deg_dial.setWrapping(False)
        self.deg_dial.setNotchesVisible(True)
        self.deg_dial.setObjectName("deg_dial")
        self.verticalLayout_4.addWidget(self.deg_dial)
        self.str_label2 = QtWidgets.QLabel(self.centralwidget)
        self.str_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.str_label2.setObjectName("str_label2")
        self.verticalLayout_4.addWidget(self.str_label2)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.rpm_dial = QtWidgets.QDial(self.centralwidget)
        self.rpm_dial.setMaximum(1400)
        self.rpm_dial.setSingleStep(125)
        self.rpm_dial.setNotchesVisible(True)
        self.rpm_dial.setObjectName("rpm_dial")
        self.verticalLayout_5.addWidget(self.rpm_dial)
        self.str_label4 = QtWidgets.QLabel(self.centralwidget)
        self.str_label4.setAlignment(QtCore.Qt.AlignCenter)
        self.str_label4.setObjectName("str_label4")
        self.verticalLayout_5.addWidget(self.str_label4)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.sec_dial = QtWidgets.QDial(self.centralwidget)
        self.sec_dial.setMaximum(500)
        self.sec_dial.setSingleStep(5)
        self.sec_dial.setNotchesVisible(True)
        self.sec_dial.setObjectName("sec_dial")
        self.verticalLayout_6.addWidget(self.sec_dial)
        self.str_label6 = QtWidgets.QLabel(self.centralwidget)
        self.str_label6.setAlignment(QtCore.Qt.AlignCenter)
        self.str_label6.setObjectName("str_label6")
        self.verticalLayout_6.addWidget(self.str_label6)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.gridLayout.addLayout(self.horizontalLayout, 9, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 4, 0, 1, 3)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.big_radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.big_radioButton.setGeometry(QtCore.QRect(0, 10, 115, 22))
        self.big_radioButton.setChecked(True)
        self.big_radioButton.setObjectName("big_radioButton")
        self.small_radioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.small_radioButton.setGeometry(QtCore.QRect(0, 40, 115, 22))
        self.small_radioButton.setObjectName("small_radioButton")
        self.verticalLayout_7.addWidget(self.groupBox_2)
        self.gridLayout.addLayout(self.verticalLayout_7, 7, 1, 2, 1)
        self.quit_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.quit_pushButton.setObjectName("quit_pushButton")
        self.gridLayout.addWidget(self.quit_pushButton, 0, 1, 1, 1)
        self.line.raise_()
        self.titel2_label.raise_()
        self.h_str_pushButton.raise_()
        self.weight_pushButton.raise_()
        self.titel1_label.raise_()
        self.str_label7.raise_()
        self.textBrowser.raise_()
        self.quit_pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        ##connecting spinboxes and dial between one another
        self.deg_dial.valueChanged.connect(self.deg_spinBox.setValue)
        self.deg_spinBox.valueChanged.connect(self.deg_dial.setValue)
        self.rpm_dial.valueChanged.connect(self.rpm_spinBox.setValue)
        self.rpm_spinBox.valueChanged.connect(self.rpm_dial.setValue)
        self.sec_dial.valueChanged.connect(self.sec_spinBox.setValue)
        self.sec_spinBox.valueChanged.connect(self.sec_dial.setValue)
        ##setting the buttons
        self.quit_pushButton.clicked.connect(self.leave)
        self.h_str_pushButton.clicked.connect(self.open_h_str)
        self.weight_pushButton.clicked.connect(self.in_weight)
        self.weight_pushButton.clicked.connect(self.open_weighing)
        #weight = self.in_weight()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def in_weight(self, text):
        weight = float(self.lineEdit.text())
        weight = str(weight)
        f = open("value.txt", "w")
        f.write(weight)
        f.close()
        return
    def open_h_str(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog_str_heat()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
    def open_weighing(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog_weighing()
        ui.setupUi(Dialog)
        Dialog.show()
        Dialog.exec_()
        ui.input_label.setText("Desired amount = 15g")
    def leave(self):
        QtCore.QCoreApplication.instance().quit()
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Menu"))
        self.str_label1.setText(_translate("MainWindow", "deg C"))
        self.str_label3.setText(_translate("MainWindow", "rpm"))
        self.str_label5.setText(_translate("MainWindow", "sec"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1)<span style=\" font-weight:600; text-decoration: underline;\">Weighing:</span> Please give the amount of buffer in grams you would like to add to the solution</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2)<span style=\" font-weight:600; text-decoration: underline;\">Stirring&amp;heating:</span> Please set the temperature, the rpm and the timer you would like the whole process to be performed with</p></body></html>"))
        self.str_label7.setText(_translate("MainWindow", "Mixing core size"))
        self.weight_pushButton.setText(_translate("MainWindow", "Run weighing"))
        self.titel1_label.setText(_translate("MainWindow", "Weighing"))
        self.titel2_label.setText(_translate("MainWindow", "Stirring&heating"))
        self.h_str_pushButton.setText(_translate("MainWindow", "Run stirring and heating"))
        self.ph_label1.setText(_translate("MainWindow", "Enter the weight"))
        self.str_label2.setText(_translate("MainWindow", "temperature"))
        self.str_label4.setText(_translate("MainWindow", "rpm"))
        self.str_label6.setText(_translate("MainWindow", "seconds"))
        self.big_radioButton.setText(_translate("MainWindow", "big one"))
        self.small_radioButton.setText(_translate("MainWindow", "small one"))
        self.quit_pushButton.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

