import os
import numpy as np
from qtpy.QtGui import *
from qtpy.QtWidgets import *
from qtpy.QtCore import *
from .client import collection
import pyqtgraph as pg

root = '/home/sliu/beamline_data'

tag = 'feature'


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.record = None

        self.mainwidget = QWidget()
        self.setCentralWidget(self.mainwidget)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.mainwidget.setLayout(self.layout)

        self.taglbl = QLabel(tag + '? (Left=[Z], Right=[/]')
        self.layout.addWidget(self.taglbl)

        self.view = pg.ImageView()
        self.layout.addWidget(self.view)
        self.view.imageItem.setOpts(axisOrder='row-major')

        QShortcut(Qt.Key_Z, self, self.tagLeft)
        QShortcut(Qt.Key_Slash, self, self.tagRight)
        self.showNext()

    def tagLeft(self):
        print('marked False')
        self.record[tag] = False
        collection.save(self.record)
        self.showNext()

    def tagRight(self):
        print('marked True')
        self.record[tag] = True
        collection.save(self.record)
        self.showNext()

    def showNext(self):
        self.record = collection.aggregate([
            {'$match': {tag: {'$exists' : False }}},
            {'$sample': {'size': 1}}]).next()

        basename = self.record['File']

        img_path = os.path.join(root, basename + '.npy')
        data = np.load(img_path)

        self.view.setImage(data)
