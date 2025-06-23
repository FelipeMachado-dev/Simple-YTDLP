# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InterfaceTKfNDi.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPlainTextEdit,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 600)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.titleLabel = QLabel(self.centralwidget)
        self.titleLabel.setObjectName(u"titleLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(24)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)

        self.horizontalLayout.addWidget(self.titleLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.urlTextBox = QPlainTextEdit(self.centralwidget)
        self.urlTextBox.setObjectName(u"urlTextBox")
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        self.urlTextBox.setFont(font1)

        self.gridLayout_2.addWidget(self.urlTextBox, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pathLabel = QLabel(self.centralwidget)
        self.pathLabel.setObjectName(u"pathLabel")
        self.pathLabel.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pathLabel)

        self.downloadPath = QLineEdit(self.centralwidget)
        self.downloadPath.setObjectName(u"downloadPath")

        self.horizontalLayout_2.addWidget(self.downloadPath)

        self.pathButton = QPushButton(self.centralwidget)
        self.pathButton.setObjectName(u"pathButton")
        self.pathButton.setFont(font1)

        self.horizontalLayout_2.addWidget(self.pathButton)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.videoQualities = QComboBox(self.frame)
        self.videoQualities.addItem("")
        self.videoQualities.addItem("")
        self.videoQualities.addItem("")
        self.videoQualities.addItem("")
        self.videoQualities.addItem("")
        self.videoQualities.addItem("")
        self.videoQualities.setObjectName(u"videoQualities")
        self.videoQualities.setFont(font1)
        self.videoQualities.setEditable(False)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.videoQualities)

        self.isPlaylist = QCheckBox(self.frame)
        self.isPlaylist.setObjectName(u"isPlaylist")
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.isPlaylist.setFont(font2)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.isPlaylist)

        self.isAudioOnly = QCheckBox(self.frame)
        self.isAudioOnly.setObjectName(u"isAudioOnly")
        self.isAudioOnly.setFont(font2)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.isAudioOnly)


        self.gridLayout.addLayout(self.formLayout, 2, 0, 1, 1)


        self.horizontalLayout_4.addLayout(self.gridLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.downloadButton = QPushButton(self.frame)
        self.downloadButton.setObjectName(u"downloadButton")
        self.downloadButton.setMinimumSize(QSize(200, 100))
        self.downloadButton.setSizeIncrement(QSize(0, 0))
        font3 = QFont()
        font3.setFamilies([u"Consolas"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.downloadButton.setFont(font3)
        self.downloadButton.setMouseTracking(False)
        self.downloadButton.setToolTipDuration(-1)
        self.downloadButton.setIconSize(QSize(16, 16))
        self.downloadButton.setFlat(False)

        self.horizontalLayout_3.addWidget(self.downloadButton)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_5)


        self.gridLayout_2.addWidget(self.frame, 3, 0, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy2)
        self.progressBar.setMinimumSize(QSize(400, 25))
        font4 = QFont()
        font4.setFamilies([u"Consolas"])
        font4.setBold(True)
        self.progressBar.setFont(font4)
        self.progressBar.setValue(50)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)

        self.gridLayout_2.addWidget(self.progressBar, 4, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 500, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Simple YT-DLP", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"SIMPLE YT-DLP", None))
#if QT_CONFIG(statustip)
        self.urlTextBox.setStatusTip(QCoreApplication.translate("MainWindow", u"Insert URLs here.", None))
#endif // QT_CONFIG(statustip)
        self.urlTextBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Paste your URLs here. Exemple: <URL_1> <URL_2> <URL_3>...", None))
        
        self.pathLabel.setText(QCoreApplication.translate("MainWindow", u"Download Folder", None))
#if QT_CONFIG(statustip)
        self.downloadPath.setStatusTip(QCoreApplication.translate("MainWindow", u"Destination where the videos are gona be downloaded", None))
#endif // QT_CONFIG(statustip)
        self.downloadPath.setText(QCoreApplication.translate("MainWindow", u"Download Path", None))

        self.pathButton.setText(QCoreApplication.translate("MainWindow", u"Change", None))

        self.videoQualities.setItemText(0, QCoreApplication.translate("MainWindow", u"360p", None))
        self.videoQualities.setItemText(1, QCoreApplication.translate("MainWindow", u"480p", None))
        self.videoQualities.setItemText(2, QCoreApplication.translate("MainWindow", u"720p", None))
        self.videoQualities.setItemText(3, QCoreApplication.translate("MainWindow", u"1080p", None))
        self.videoQualities.setItemText(4, QCoreApplication.translate("MainWindow", u"1440p", None))
        self.videoQualities.setItemText(5, QCoreApplication.translate("MainWindow", u"2160p", None))
        self.videoQualities.setCurrentIndex(-1)
        self.videoQualities.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Video Quality", None))
#if QT_CONFIG(tooltip)
        self.isPlaylist.setToolTip(QCoreApplication.translate("MainWindow", u"Select to download all the playlist that the video is part of.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.isPlaylist.setStatusTip(QCoreApplication.translate("MainWindow", u"Select to download all the playlist that the video is part of.", None))
#endif // QT_CONFIG(statustip)
        self.isPlaylist.setText(QCoreApplication.translate("MainWindow", u"PLAYLIST", None))
#if QT_CONFIG(tooltip)
        self.isAudioOnly.setToolTip(QCoreApplication.translate("MainWindow", u"Select to download only the audio from a video in a MP3 format.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.isAudioOnly.setStatusTip(QCoreApplication.translate("MainWindow", u"Select to download only the audio from a video in a MP3 format.", None))
#endif // QT_CONFIG(statustip)
        self.isAudioOnly.setText(QCoreApplication.translate("MainWindow", u"AUDIO ONLY", None))
#if QT_CONFIG(tooltip)
        self.downloadButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.downloadButton.setStatusTip(QCoreApplication.translate("MainWindow", u"Download all the URLs present above.", None))
#endif // QT_CONFIG(statustip)
        self.downloadButton.setText(QCoreApplication.translate("MainWindow", u"DOWNLOAD", None))
    # retranslateUi
        
        #Teste para pegar valor de caminho de download
        #print (self.downloadPath.text())

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())