# -*- coding: utf-8 -*-
# =============================================================================
#                                                                             #
#                       GRAND PROJET NSI TERMINALE                            #
#                                                                             #
#                       - Pierre-Louis                                        #
#                       - Julien                                              #
#                       - Marius                                              #
#                       - Matis                                               #
#                                                                             #
# =============================================================================

#--------------Importation des modules-----------------------------------------

import Pc_Builder_Software as PBS
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from random import randint
#GUI File
from chargement import Ui_Chargement
 
class Chargement(QMainWindow):
    def __init__(self):
        """Creation d'un chargement"""
        self.app_icon = QtGui.QIcon()
        self.app_icon.addFile('logo.ico')
        
        self.cpt = 0
        self.saut = 0
        
        QMainWindow.__init__(self)
        self.ui = Ui_Chargement()
        self.ui.setupUi(self)
        
        self.chargementValeur(0)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.CercleBg.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.chargement)

        self.timer.start(25)
        self.show()


    def chargement(self):
        """Fonction permettant d'augmenter le pourcentage"""
        value =self.cpt
        
        htmlText = """<p><span style=" font-size:68pt;">{VALUE}</span><span style=" font-size:58pt; vertical-align:super;">%</span></p>"""
        newHtml = htmlText.replace("{VALUE}", str(self.saut))

        if(value > self.saut):

            self.ui.labelProg.setText(newHtml)
            self.saut += randint(1,10)

        if value >= 100: value = 1.000
        self.chargementValeur(value)
        
        #A la fin du Timer, on lance l'application
        if self.cpt > 100:
            self.timer.stop()
            self.close()
            App = PBS.App()
            App.main()
            App.root.resizable(False, False)
            App.root.mainloop()

        self.cpt += 0.5
    
    def chargementValeur(self,value):
        """Permet d'animer le chargement"""
        styleSheet = """
        QFrame{
            border-radius: 150px;
            background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} #3C3C40, stop:{STOP_2} #19232d);
        }"""

        progress = (100 - value) / 100.0

        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        self.ui.CercleChargement.setStyleSheet(newStylesheet)

        
if __name__=="__main__":
    app = QApplication(sys.argv)
    window = Chargement()
    app.setWindowIcon(window.app_icon)
    sys.exit(app.exec_())