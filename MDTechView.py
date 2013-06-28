import sys
import os
import zipfile
from PyQt4.QtCore import QString
from MDSupportBundle import MDSupportBundle
from PyQt4.QtGui import QApplication, QMainWindow, QFontMetrics, QFont, QColor, QFileDialog, QAction, QIcon
from PyQt4 import QtNetwork
from PyQt4.QtCore import QUrl
from Ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.show_dialog)

        self.textMEL.SendScintilla(self.textMEL.SCI_SETHSCROLLBAR, 0)
        self.textiSCSI.SendScintilla(self.textiSCSI.SCI_SETHSCROLLBAR, 0)
        self.textSAP.SendScintilla(self.textSAP.SCI_SETHSCROLLBAR, 0)
        self.textStateCap.SendScintilla(self.textStateCap.SCI_SETHSCROLLBAR, 0)

        self.setAcceptDrops(True)
        self.droppedFile = None

    def dragEnterEvent(self, event):
        self.droppedFile = None
        if event.mimeData().hasUrls():
            url = event.mimeData().urls()[0]
            if url.isValid():
                if url.scheme() == "file":
                    self.droppedFile = url.toLocalFile()
                    event.accept()
 
    def dropEvent(self, event):
        print 'Dropped file: ' + self.droppedFile # displays the file name   
        if zipfile.is_zipfile(self.droppedFile):
            print 'is zipfile'
            with zipfile.ZipFile(str(self.droppedFile)) as tempZip:
                print 'Extract to: ' + str(self.droppedFile.split(os.sep)[len(self.droppedFile.split(os.sep)) - 1].split('.')[0])
                tempZip.extractall(str(self.droppedFile.split(os.sep)[len(self.droppedFile.split(os.sep)) - 1].split('.')[0]))
                self.load_bundle(self.droppedFile.split('.')[0])

            

    def show_dialog(self):
        path_dialog = QFileDialog()
        path_dialog.setFileMode(QFileDialog.Directory)
        bundle_path = path_dialog.getExistingDirectory(self, 'Select support bundle folder...', '')
        if bundle_path:
            self.labelPath.setText('Current Bundle Path: ' + bundle_path)
            self.load_bundle(bundle_path)
            
    
    def load_bundle(self, bundle_path):
        self.textiSCSI.clear()
        self.textSAP.clear()
        self.textMEL.clear()
        self.textStateCap.clear()

        if bundle_path:
            self.labelPath.setText('Current Bundle Path: ' + bundle_path)
        else:
            self.labelPath.setText('Current Bundle Path: None')
             

        support_bundle = MDSupportBundle(bundle_path)
        
        # Load Recovery Guru
        if os.path.exists(support_bundle.recovery_guru_path):
            self.webView.setUrl(QUrl('file:///' + support_bundle.recovery_guru_path))
        else:
            self.webView.setUrl(QUrl('about:blank'))

        # Load storageArrayProfile
        self.textSAP.setText(support_bundle.get_storage_array_profile())

        # Load MEL
        self.textMEL.setText(support_bundle.get_major_event_log())

        # Load State Cap
        self.textStateCap.setText(support_bundle.get_state_capture_data())

        # Load iSCSI Sessions
        self.textiSCSI.setText(support_bundle.get_iscsi_sessions())



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
