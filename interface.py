# Functionality Imports
from PySide6.QtCore import QThread, Signal, QSettings
from PySide6.QtWidgets import QFileDialog
import yt_dlp

# Interface Imports
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
    # setupUi
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(569, 600)
        MainWindow.setToolTipDuration(-1)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pathLabel = QLabel(self.centralwidget)
        self.pathLabel.setObjectName(u"pathLabel")
        font = QFont()
        font.setFamilies([u"Consolas"])
        self.pathLabel.setFont(font)

        self.horizontalLayout_2.addWidget(self.pathLabel)

        self.downloadPath = QLineEdit(self.centralwidget)
        self.downloadPath.setObjectName(u"downloadPath")

        self.horizontalLayout_2.addWidget(self.downloadPath)

        self.pathButton = QPushButton(self.centralwidget)
        self.pathButton.setObjectName(u"pathButton")
        self.pathButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.pathButton)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)

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
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.titleLabel.setFont(font1)
        self.titleLabel.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)

        self.horizontalLayout.addWidget(self.titleLabel)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.urlTextBox = QPlainTextEdit(self.centralwidget)
        self.urlTextBox.setObjectName(u"urlTextBox")
        self.urlTextBox.setFont(font)

        self.gridLayout_2.addWidget(self.urlTextBox, 1, 0, 1, 1)

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
        self.videoQualities.setFont(font)
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


        self.gridLayout_2.addWidget(self.frame, 3, 0, 1, 2)

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
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setValue(50)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)

        self.gridLayout_2.addWidget(self.progressBar, 5, 0, 1, 2)

        self.downloadProgressLabel = QLabel(self.centralwidget)
        self.downloadProgressLabel.setObjectName(u"downloadProgressLabel")
        self.downloadProgressLabel.setEnabled(True)
        sizePolicy.setHeightForWidth(self.downloadProgressLabel.sizePolicy().hasHeightForWidth())
        self.downloadProgressLabel.setSizePolicy(sizePolicy)
        self.downloadProgressLabel.setMinimumSize(QSize(0, 0))
        self.downloadProgressLabel.setTabletTracking(False)
        self.downloadProgressLabel.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.downloadProgressLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.downloadProgressLabel.setWordWrap(False)

        self.gridLayout_2.addWidget(self.downloadProgressLabel, 6, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 569, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # retranslateUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Simple YT-DLP", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.pathLabel.setText(QCoreApplication.translate("MainWindow", u"Download Folder", None))
#if QT_CONFIG(statustip)
        self.downloadPath.setStatusTip(QCoreApplication.translate("MainWindow", u"Destination where the videos are gona be downloaded", None))
#endif // QT_CONFIG(statustip)
        self.downloadPath.setText("")
        self.downloadPath.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Download Path", None))
        self.pathButton.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"SIMPLE YT-DLP", None))
#if QT_CONFIG(statustip)
        self.urlTextBox.setStatusTip(QCoreApplication.translate("MainWindow", u"Insert URLs here.", None))
#endif // QT_CONFIG(statustip)
        self.urlTextBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Paste your URLs here. Exemple: <URL_1> <URL_2> <URL_3>...", None))
        self.videoQualities.setItemText(0, QCoreApplication.translate("MainWindow", u"360p", None))
        self.videoQualities.setItemText(1, QCoreApplication.translate("MainWindow", u"480p", None))
        self.videoQualities.setItemText(2, QCoreApplication.translate("MainWindow", u"720p", None))
        self.videoQualities.setItemText(3, QCoreApplication.translate("MainWindow", u"1080p", None))
        self.videoQualities.setItemText(4, QCoreApplication.translate("MainWindow", u"1440p", None))
        self.videoQualities.setItemText(5, QCoreApplication.translate("MainWindow", u"2160p", None))

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
        self.downloadProgressLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    
    # Setup Functions
    def setupFunctions(self):
        # Make buttons work
        self.downloadButton.clicked.connect(self.startDownload)
        self.pathButton.clicked.connect(self.downloadDirectory)

        # Show placeholder text
        self.videoQualities.setCurrentIndex(-1)

    # Message Box    
    def show_message(self, message, sucess):
        from PySide6.QtWidgets import QMessageBox
        if sucess:
            QMessageBox.information(None, "Sucess", message)
        else:
            QMessageBox.information(None, "Error", message)

    # Select and save download directory
    def downloadDirectory(self):
        directory = QFileDialog.getExistingDirectory(None, "Select Directory")
        if directory:
            self.downloadPath.setText(directory)

            settings = QSettings("YourCompany","Simple YT-DLP")
            settings.setValue("download_directory", directory)
    
    # Load download directory
    def loadDownloadDirectory(self):
        settings = QSettings("YourCompany","Simple YT-DLP")
        directory = settings.value("download_directory", "")
        self.downloadPath.setText(directory)
            
    # Download Button Function
    def startDownload(self):
        url_text = self.urlTextBox.toPlainText().strip()
        if not url_text:
            self.show_message("Please paste at least one URL.", False)
            return
        
        url = url_text.split()
        qUrl = url_text.count("youtube")
        audio_only = self.isAudioOnly.isChecked()
        playlist = self.isPlaylist.isChecked()
        quality = self.videoQualities.currentText()
        dPath = self.downloadPath.text()

        self.progressBar.setValue(0)
        self.progressBar.setHidden(False)
        self.downloadProgressLabel.setHidden(False)
        

        self.thread = downloadThread(url, qUrl,audio= audio_only, playlist= playlist, quality= quality, dPath= dPath)
        self.thread.progress_changed.connect(self.progressBar.setValue)
        self.thread.finished.connect(self.show_message)
        self.thread.pBarDisplay.connect(self.progressBar.setHidden)
        self.thread.pLabelDisplay.connect(self.downloadProgressLabel.setHidden)
        self.thread.start()

# Download Class
class downloadThread(QThread):
    progress_changed = Signal(int)
    finished = Signal(str, bool)
    pBarDisplay = Signal(bool)
    pLabelDisplay = Signal(bool)
    dCount = 0

    def __init__(self, url, qUrl,audio=True, quality="best", playlist=False, dPath=''):
        super().__init__()
        self.url = url
        self.qUrl = qUrl
        self.audio = audio
        self.quality = quality
        self.playlist = playlist
        self.dPath = dPath

    def run(self):
        def progress_hook(d):
            if d['status'] == 'downloading':
                total = d.get('total_bytes') or d.get('total_bytes_estimated')
                downloaded = d.get('downloaded_bytes', 0)
                if total:
                    percent = int((downloaded/total)*100)
                    self.progress_changed.emit(percent)
            elif d['status'] == 'finished':
                self.progress_changed.emit(100)
                self.dCount += 1

        try:        
            if self.audio:
                path = self.dPath + '/%(title)s'

                ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                }],
                'outtmpl': path,
                'noplaylist': not self.playlist,
                'progress_hooks': [progress_hook]
                }
            else:
                quality_options ={
                '360p': 'bestvideo[height<=360]+bestaudio/best',
                '480p': 'bestvideo[height<=480]+bestaudio/best',
                '720p': 'bestvideo[height<=720]+bestaudio/best',
                '1080p': 'bestvideo[height<=1080]+bestaudio/best',
                '1440p': 'bestvideo[height<=1440]+bestaudio/best',
                }
                
                quality = quality_options.get(self.quality, 'bestvideo+bestaudio')

                path = self.dPath + '/%(title)s'
                ydl_opts = {
                'format': quality,
                'outtmpl': path,
                'noplaylist': not self.playlist,
                'progress_hooks': [progress_hook]
                }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download(self.url)
            self.finished.emit("Download Completed!", True)
            self.pBarDisplay.emit(True)
            self.pLabelDisplay.emit(True)
        except Exception as e:
            self.finished.emit(str(e), False)

# App Inicialization
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.setupFunctions()
    ui.loadDownloadDirectory()
    ui.progressBar.setHidden(True)
    ui.downloadProgressLabel.setHidden(True)
    MainWindow.show()
    sys.exit(app.exec())