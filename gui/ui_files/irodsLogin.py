# Form implementation generated from reading ui file 'D:\Christine_irods\iBridges-Gui\gui\ui_files\irodsLogin.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_irodsLogin(object):
    def setupUi(self, irodsLogin):
        irodsLogin.setObjectName("irodsLogin")
        irodsLogin.resize(770, 332)
        irodsLogin.setMinimumSize(QtCore.QSize(770, 320))
        irodsLogin.setStyleSheet("QWidget\n"
"{\n"
"    background-color: rgb(54, 54, 54);\n"
"    color: rgb(86, 184, 139);\n"
"    border-color: rgb(217, 174, 23);\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: rgb(85, 87, 83);\n"
"    border-color: rgb(217, 174, 23);\n"
"}\n"
"\n"
"QRadioButton\n"
"{\n"
"    border-bottom-color: rgb(206, 92, 0);\n"
"}\n"
"\n"
"QLabel#passError, QLabel#envError, QLabel#icommandsError\n"
"{\n"
"    color: rgb(217, 174, 23);\n"
"}\n"
"\n"
"QRadioButton\n"
"{ \n"
"    selection-color: rgb(217, 174, 23);\n"
"}\n"
"")
        self.gridLayoutWidget = QtWidgets.QWidget(irodsLogin)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 741, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.labelTitle = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        self.gridLayout.addWidget(self.labelTitle, 0, 0, 1, 1)
        self.selectIcommandsButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.selectIcommandsButton.setFont(font)
        self.selectIcommandsButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.selectIcommandsButton.setStyleSheet("")
        self.selectIcommandsButton.setObjectName("selectIcommandsButton")
        self.gridLayout.addWidget(self.selectIcommandsButton, 2, 0, 1, 1)
        self.passError = QtWidgets.QLabel(self.gridLayoutWidget)
        self.passError.setStyleSheet("")
        self.passError.setText("")
        self.passError.setObjectName("passError")
        self.gridLayout.addWidget(self.passError, 10, 2, 1, 1)
        self.envFileLable = QtWidgets.QLabel(self.gridLayoutWidget)
        self.envFileLable.setObjectName("envFileLable")
        self.gridLayout.addWidget(self.envFileLable, 6, 0, 1, 1)
        self.passwordLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.gridLayout.addWidget(self.passwordLabel, 9, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.envError = QtWidgets.QLabel(self.gridLayoutWidget)
        self.envError.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.envError.setStyleSheet("")
        self.envError.setText("")
        self.envError.setObjectName("envError")
        self.gridLayout.addWidget(self.envError, 8, 2, 1, 1)
        self.standardButton = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.standardButton.setFont(font)
        self.standardButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.standardButton.setStyleSheet("")
        self.standardButton.setChecked(True)
        self.standardButton.setObjectName("standardButton")
        self.gridLayout.addWidget(self.standardButton, 4, 0, 1, 1)
        self.icommandsError = QtWidgets.QLabel(self.gridLayoutWidget)
        self.icommandsError.setStyleSheet("")
        self.icommandsError.setText("")
        self.icommandsError.setObjectName("icommandsError")
        self.gridLayout.addWidget(self.icommandsError, 2, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 1)
        self.envbox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.envbox.setObjectName("envbox")
        self.gridLayout.addWidget(self.envbox, 6, 1, 1, 2)
        self.passwordField = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.passwordField.setStyleSheet("background-color: rgb(85, 87, 83);")
        self.passwordField.setText("")
        self.passwordField.setClearButtonEnabled(True)
        self.passwordField.setObjectName("passwordField")
        self.gridLayout.addWidget(self.passwordField, 9, 1, 1, 2)
        self.horizontalLayoutWidget = QtWidgets.QWidget(irodsLogin)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 260, 741, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ticketButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.ticketButton.setObjectName("ticketButton")
        self.horizontalLayout.addWidget(self.ticketButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.connectButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.connectButton.setFont(font)
        self.connectButton.setAutoDefault(True)
        self.connectButton.setDefault(True)
        self.connectButton.setObjectName("connectButton")
        self.horizontalLayout.addWidget(self.connectButton)

        self.retranslateUi(irodsLogin)
        QtCore.QMetaObject.connectSlotsByName(irodsLogin)

    def retranslateUi(self, irodsLogin):
        _translate = QtCore.QCoreApplication.translate
        irodsLogin.setWindowTitle(_translate("irodsLogin", "Dialog"))
        self.labelTitle.setText(_translate("irodsLogin", "iRODS Login"))
        self.selectIcommandsButton.setText(_translate("irodsLogin", "Up-/Download with icommands (linux only.):"))
        self.envFileLable.setText(_translate("irodsLogin", "      iRODS environment file:"))
        self.passwordLabel.setText(_translate("irodsLogin", "      Password"))
        self.standardButton.setText(_translate("irodsLogin", "Standard Up-/Download"))
        self.ticketButton.setText(_translate("irodsLogin", "Login with ticket"))
        self.connectButton.setText(_translate("irodsLogin", "Connect"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    irodsLogin = QtWidgets.QDialog()
    ui = Ui_irodsLogin()
    ui.setupUi(irodsLogin)
    irodsLogin.show()
    sys.exit(app.exec())
