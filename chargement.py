# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chargement(3).ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Chargement(object):
    def setupUi(self, Chargement):
        Chargement.setObjectName("Chargement")
        Chargement.resize(349, 345)
        self.centralwidget = QtWidgets.QWidget(Chargement)
        self.centralwidget.setObjectName("centralwidget")
        self.CercleChargementBase = QtWidgets.QFrame(self.centralwidget)
        self.CercleChargementBase.setGeometry(QtCore.QRect(10, 10, 320, 320))
        self.CercleChargementBase.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CercleChargementBase.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CercleChargementBase.setObjectName("CercleChargementBase")
        self.CercleChargement = QtWidgets.QFrame(self.CercleChargementBase)
        self.CercleChargement.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.CercleChargement.setStyleSheet("QFrame{\n"
"    border-radius: 150px;\n"
"    background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.775 #19232d, stop:0.776 #3C3C40);\n"
"}")
        self.CercleChargement.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CercleChargement.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CercleChargement.setObjectName("CercleChargement")
        self.CercleBg = QtWidgets.QFrame(self.CercleChargementBase)
        self.CercleBg.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.CercleBg.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.CercleBg.setStyleSheet("QFrame{\n"
"    border-radius:150px;\n"
"    background-color: rgba(105, 105, 255,100);\n"
"}")
        self.CercleBg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CercleBg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.CercleBg.setObjectName("CercleBg")
        self.container = QtWidgets.QFrame(self.CercleChargementBase)
        self.container.setEnabled(True)
        self.container.setGeometry(QtCore.QRect(25, 25, 270, 270))
        self.container.setToolTipDuration(1)
        self.container.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.container.setStyleSheet("QFrame{\n"
"    border-radius:135px;\n"
"    \n"
"    background-color:#19232d;\n"
"}")
        self.container.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")
        self.layoutWidget = QtWidgets.QWidget(self.container)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 231, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.labelTitle = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Samsung Sharp Sans")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet("background-color:none;\n"
"color: #015EEA;")
        self.labelTitle.setFrameShape(QtWidgets.QFrame.HLine)
        self.labelTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitle.setObjectName("labelTitle")
        self.gridLayout.addWidget(self.labelTitle, 1, 0, 1, 1)
        self.labelAuteur = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Amaranth")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelAuteur.setFont(font)
        self.labelAuteur.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.labelAuteur.setStyleSheet("background-color:none;color:#6699ff;")
        self.labelAuteur.setFrameShape(QtWidgets.QFrame.HLine)
        self.labelAuteur.setTextFormat(QtCore.Qt.PlainText)
        self.labelAuteur.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAuteur.setObjectName("labelAuteur")
        self.gridLayout.addWidget(self.labelAuteur, 13, 0, 1, 1)
        self.labelChargement = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Samsung Sharp Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.labelChargement.setFont(font)
        self.labelChargement.setStyleSheet("QLabel{\n"
"    border-radius: 10px;\n"
"    background-color: rgba(105, 105, 255,35);\n"
"    margin-left:30px;\n"
"    margin-right:30px;\n"
"}")
        self.labelChargement.setFrameShape(QtWidgets.QFrame.HLine)
        self.labelChargement.setAlignment(QtCore.Qt.AlignCenter)
        self.labelChargement.setObjectName("labelChargement")
        self.gridLayout.addWidget(self.labelChargement, 12, 0, 1, 1)
        self.labelProg = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Samsung Sharp Sans")
        font.setPointSize(68)
        font.setBold(False)
        font.setWeight(50)
        self.labelProg.setFont(font)
        self.labelProg.setStyleSheet("background-color:none;color:#015EEA;")
        self.labelProg.setFrameShape(QtWidgets.QFrame.HLine)
        self.labelProg.setAlignment(QtCore.Qt.AlignCenter)
        self.labelProg.setObjectName("labelProg")
        self.gridLayout.addWidget(self.labelProg, 0, 0, 1, 1)
        Chargement.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Chargement)
        self.statusbar.setObjectName("statusbar")
        Chargement.setStatusBar(self.statusbar)

        self.retranslateUi(Chargement)
        QtCore.QMetaObject.connectSlotsByName(Chargement)

    def retranslateUi(self, Chargement):
        _translate = QtCore.QCoreApplication.translate
        Chargement.setWindowTitle(_translate("Chargement", "Pc Builder Software"))
        self.labelTitle.setText(_translate("Chargement", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#6699ff;\">Pc Builder Software</span></p></body></html>"))
        self.labelAuteur.setText(_translate("Chargement", "by TEAM PBS"))
        self.labelChargement.setText(_translate("Chargement", "<html><head/><body><p><span style=\" font-size:12pt; color:#6699ff;\">Chargement...</span></p></body></html>"))
        self.labelProg.setText(_translate("Chargement", "<html><head/><body><p><span style=\" color:#6699ff;\">0</span><span style=\" font-size:58pt; color:#6699ff; vertical-align:super;\">%</span></p></body></html>"))




