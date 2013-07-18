import sys
import os
import zipfile
import gc
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from MDSupportBundle import MDSupportBundle
from PyQt4 import QtNetwork
from Ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.show_dialog)

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
        self.extract_zipped_bundle(self.droppedFile)

          
    def extract_zipped_bundle(self, file_path):
        if zipfile.is_zipfile(file_path):
            print 'is zipfile'

            with zipfile.ZipFile(str(file_path)) as tempZip:

                print 'Extract to: ' + str(file_path.split(os.sep)[len(file_path.split(os.sep)) - 1].split('.')[0])

                tempZip.extractall(str(file_path.split(os.sep)[len(file_path.split(os.sep)) - 1].split('.')[0]))
                self.load_bundle(file_path.split('.')[0])

    def show_dialog(self):
        path_dialog = QFileDialog()
        path_dialog.setFileMode(QFileDialog.ExistingFile)
        bundle_path = path_dialog.getOpenFileName(self, 'Select MD support bundle zip...', '', 'Support bundles (*.zip)')
        if bundle_path:
            self.extract_zipped_bundle(bundle_path)
            
    
    def load_bundle(self, bundle_path):
        self.textiSCSI.clear()
        self.textSAP.clear()
        self.textStateCap.clear()

        if bundle_path:
            self.labelPath.setText('Current Bundle Path: ' + bundle_path)
            self.setWindowTitle('MD TechView Alpha - ' + bundle_path)
        else:
            self.labelPath.setText('Current Bundle Path: None')
            self.setWindowTitle('MD TechView Alpha - None')

             

        support_bundle = MDSupportBundle(bundle_path)
        
        # Load Recovery Guru
        if os.path.exists(support_bundle.recovery_guru_path):
            self.webView.setUrl(QUrl('file:///' + support_bundle.recovery_guru_path))
        else:
            self.webView.setUrl(QUrl('about:blank'))

        # Load storageArrayProfile
        self.textSAP.setText(support_bundle.get_storage_array_profile())

        # Load MEL
        #self.textMEL.setText(support_bundle.get_major_event_log())
        tablemodel = MyTableModel(support_bundle.parse_mel(), self)
        self.melTable.setModel(tablemodel)

        # Load State Cap
        self.textStateCap.setText(support_bundle.get_state_capture_data())

        # Load iSCSI Sessions
        self.textiSCSI.setText(support_bundle.get_iscsi_sessions())

class MyTableModel(QAbstractTableModel):
    def __init__(self, datain, parent=None, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.listdata = datain

    def rowCount(self, parent):
        return len(self.listdata)

    def columnCount(self, parent):
        return 10 # hard coded, 10 items in mel that are relevant, needs to be implemented properly

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        elif index.column() == 0:
            return self.listdata[index.row()].date_time
        elif index.column() == 1:
            return self.listdata[index.row()].event_type
        elif index.column() == 2:
            return self.listdata[index.row()].event_category
        elif index.column() == 3:
            return self.listdata[index.row()].priority
        elif index.column() == 4:
            return self.listdata[index.row()].description
        elif index.column() == 5:
            return self.listdata[index.row()].event_specific_codes
        elif index.column() == 6:
            return self.listdata[index.row()].component_type
        elif index.column() == 7:
            return self.listdata[index.row()].component_location
        elif index.column() == 8:
            return self.listdata[index.row()].logged_by
        else:
            return ''


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
