# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/home.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomeWindow(object):
    def setupUi(self, HomeWindow):
        HomeWindow.setObjectName("HomeWindow")
        HomeWindow.resize(1147, 885)
        HomeWindow.setStyleSheet("HomeWindow {\n"
"    background-color: rgb(255, 248, 210);\n"
"    background:rgb(255, 252, 219)\n"
"} ")
        self.centralwidget = QtWidgets.QWidget(HomeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 101, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("ui/../resources/images/docify-high-resolution-logo-black-transparent.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(880, 100, 67, 17))
        self.label_4.setStyleSheet("QLabel {\n"
"    color: rgb(0, 170, 127);\n"
"}")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 220, 151, 211))
        font = QtGui.QFont()
        font.setPointSize(67)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"border-radius: 15px;\n"
"    background-color: rgb(142, 255, 151);\n"
"    color: rgb(0, 141, 0);\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 201, 17))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 60, 711, 41))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"border-radius: 20px;\n"
"border: 1px solid black; \n"
"padding:10px;\n"
"background-color: rgb(187, 210, 231);\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 490, 920, 351))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutDocs = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayoutDocs.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutDocs.setObjectName("horizontalLayoutDocs")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 460, 201, 17))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(880, 50, 54, 50))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("ui/../resources/images/user.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 210, 430, 231))
        self.frame.setStyleSheet("QFrame {\n"
"    border-radius: 15px;\n"
"    background-color: rgb(189, 212, 238);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(520, 180, 240, 17))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(510, 210, 430, 231))
        self.frame_2.setStyleSheet("QFrame {\n"
"    border-radius: 15px;\n"
"    background-color: rgb(189, 212, 238);\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEditAccess = QtWidgets.QLineEdit(self.frame_2)
        self.lineEditAccess.setGeometry(QtCore.QRect(20, 30, 390, 70))
        self.lineEditAccess.setStyleSheet("QLineEdit {\n"
"border-radius: 20px;\n"
"border: 1px solid black; \n"
"padding:10px;\n"
"background-color: white;\n"
"}")
        self.lineEditAccess.setObjectName("lineEditAccess")
        self.pushButtonAccess = QtWidgets.QPushButton(self.frame_2)
        self.pushButtonAccess.setGeometry(QtCore.QRect(150, 130, 130, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButtonAccess.setFont(font)
        self.pushButtonAccess.setStyleSheet("QPushButton {\n"
"border-radius: 15px;\n"
"    background-color: rgb(142, 255, 151);\n"
"    color: rgb(0, 141, 0);\n"
"}\n"
"")
        self.pushButtonAccess.setObjectName("pushButtonAccess")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(20, 490, 920, 350))
        self.frame_3.setStyleSheet("QFrame {\n"
"    border-radius: 15px;\n"
"    background-color: rgb(189, 212, 238);\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButtonLogout = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonLogout.setGeometry(QtCore.QRect(900, 0, 40, 30))
        self.pushButtonLogout.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 148, 177);\n"
"    border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-radius: 30px;\n"
"    background-color: rgb(255, 85, 127);\n"
"}")
        self.pushButtonLogout.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui/../resources/images/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLogout.setIcon(icon)
        self.pushButtonLogout.setObjectName("pushButtonLogout")
        self.pushButtonRefresh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRefresh.setGeometry(QtCore.QRect(0, 0, 40, 30))
        self.pushButtonRefresh.setStyleSheet("QPushButton {\n"
"    \n"
"    background-color: rgb(170, 255, 127);\n"
"    border-radius: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-radius: 30px;\n"
"    \n"
"    background-color: rgb(85, 255, 127);\n"
"}")
        self.pushButtonRefresh.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("ui/../resources/images/Refresh_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonRefresh.setIcon(icon1)
        self.pushButtonRefresh.setObjectName("pushButtonRefresh")
        self.frame_3.raise_()
        self.frame.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.pushButton.raise_()
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.horizontalLayoutWidget.raise_()
        self.label_6.raise_()
        self.label.raise_()
        self.label_7.raise_()
        self.frame_2.raise_()
        self.pushButtonLogout.raise_()
        self.pushButtonRefresh.raise_()
        HomeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(HomeWindow)
        self.statusbar.setObjectName("statusbar")
        HomeWindow.setStatusBar(self.statusbar)
        self.actionLogout = QtWidgets.QAction(HomeWindow)
        self.actionLogout.setIcon(icon)
        self.actionLogout.setObjectName("actionLogout")

        self.retranslateUi(HomeWindow)
        QtCore.QMetaObject.connectSlotsByName(HomeWindow)

    def retranslateUi(self, HomeWindow):
        _translate = QtCore.QCoreApplication.translate
        HomeWindow.setWindowTitle(_translate("HomeWindow", "HomeWindow"))
        self.label_4.setText(_translate("HomeWindow", "Hello XYZ"))
        self.pushButton.setText(_translate("HomeWindow", "+"))
        self.label_3.setText(_translate("HomeWindow", "Create new Document"))
        self.lineEdit.setPlaceholderText(_translate("HomeWindow", "Search Docs"))
        self.label_6.setText(_translate("HomeWindow", "My Documents"))
        self.label_7.setText(_translate("HomeWindow", "Open Documents with Link"))
        self.lineEditAccess.setPlaceholderText(_translate("HomeWindow", "Enter the access link"))
        self.pushButtonAccess.setText(_translate("HomeWindow", "Open Doc"))
        self.actionLogout.setText(_translate("HomeWindow", "Logout"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HomeWindow = QtWidgets.QMainWindow()
    ui = Ui_HomeWindow()
    ui.setupUi(HomeWindow)
    HomeWindow.show()
    sys.exit(app.exec_())
