# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'str_heat.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
class Ui_Dialog_str_heat(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(357, 93)
        self.formLayout = QtWidgets.QFormLayout(Dialog)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.inst_label = QtWidgets.QLabel(Dialog)
        self.inst_label.setObjectName("inst_label")
        self.verticalLayout_3.addWidget(self.inst_label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.status_label = QtWidgets.QLabel(Dialog)
        self.status_label.setObjectName("status_label")
        self.verticalLayout.addWidget(self.status_label)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.quit_pushButton = QtWidgets.QPushButton(Dialog)
        self.quit_pushButton.setObjectName("quit_pushButton")
        self.verticalLayout_2.addWidget(self.quit_pushButton)
        self.abort_pushButton = QtWidgets.QPushButton(Dialog)
        self.abort_pushButton.setObjectName("abort_pushButton")
        self.verticalLayout_2.addWidget(self.abort_pushButton)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_2)
        ##setting msg boxes
        self.quit_pushButton.clicked.connect(self.leave)
        self.abort_pushButton.clicked.connect(Dialog.close)
        self.abort_pushButton.clicked.connect(self.show_popup)


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Abort")
        msg.setText("Before running the process again, please return everything to the default state - tools inside of the changing stations, set the temperature and the rpm on the device to zero")
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
    def leave(self):
        QtCore.QCoreApplication.instance().quit()
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Stirring&heating"))
        self.inst_label.setText(_translate("Dialog", "Process is running, please wait..."))
        self.status_label.setText(_translate("Dialog", "Setting the temperature and rpm..."))
        self.quit_pushButton.setText(_translate("Dialog", "Quit"))
        self.abort_pushButton.setText(_translate("Dialog", "Abort"))
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_str_heat()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

