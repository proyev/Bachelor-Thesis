# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weighing.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
class Ui_Dialog_weighing(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(421, 198)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setObjectName("textBrowser")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.textBrowser)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.quit_pushButton = QtWidgets.QPushButton(Dialog)
        self.quit_pushButton.setObjectName("quit_pushButton")
        self.verticalLayout.addWidget(self.quit_pushButton)
        self.abort_pushButton = QtWidgets.QPushButton(Dialog)
        self.abort_pushButton.setObjectName("abort_pushButton")
        self.verticalLayout.addWidget(self.abort_pushButton)
        self.again_pushButton = QtWidgets.QPushButton(Dialog)
        self.again_pushButton.setObjectName("again_pushButton")
        self.verticalLayout.addWidget(self.again_pushButton)
        self.menu_pushButton = QtWidgets.QPushButton(Dialog)
        self.menu_pushButton.setObjectName("menu_pushButton")
        self.verticalLayout.addWidget(self.menu_pushButton)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.input_label = QtWidgets.QLabel(Dialog)
        self.input_label.setObjectName("input_label")
        self.verticalLayout_2.addWidget(self.input_label)
        self.output_label = QtWidgets.QLabel(Dialog)
        self.output_label.setObjectName("output_label")
        self.verticalLayout_2.addWidget(self.output_label)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.status_label = QtWidgets.QLabel(Dialog)
        self.status_label.setObjectName("status_label")
        self.horizontalLayout.addWidget(self.status_label)
        self.verticalLayout_3.addLayout(self.horizontalLayout)

        ##setting up the buttons
        self.quit_pushButton.clicked.connect(self.leave)    
        self.menu_pushButton.clicked.connect(self.menu_popup)
        self.menu_pushButton.clicked.connect(Dialog.close)
        self.abort_pushButton.clicked.connect(self.abort_popup)
        self.abort_pushButton.clicked.connect(Dialog.close)
        self.again_pushButton.clicked.connect(self.status)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    
    def leave(self):
        QtCore.QCoreApplication.instance().quit()
    def menu_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Back to the menu")
        msg.setText("Please add the buffer to the solution before making your next step")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    def abort_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Abort")
        msg.setText("Please remove everything from the scales")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Weighing"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Please wait a second until the robot checks the scales value for you. The result will appear below shortly. For the best result, please validate the output value yourself as well.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.quit_pushButton.setText(_translate("Dialog", "Quit"))
        self.abort_pushButton.setText(_translate("Dialog", "Abort"))
        self.again_pushButton.setText(_translate("Dialog", "Run again"))
        self.menu_pushButton.setText(_translate("Dialog", "Menu"))
        f = open("value.txt", "r")
        value = f.readline()
        f.close()
        self.input_label.setText(_translate("Dialog", "Desired amount = " + value + " g"))
        self.output_label.setText(_translate("Dialog", "Current amount = 2.992 g"))
        self.status_label.setText(_translate("Dialog", "Please, add some more buffer"))
    def status(self):
        f = open("value.txt", "r")
        value = f.readline()
        f.close()
        self.output_label.setText("Current amount = " + value + " g")
        self.status_label.setText("Looks good, press menu to continue")
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_weighing()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

