import os
import numpy as np
from qtpy.QtGui import *
from qtpy.QtWidgets import *
from qtpy.QtCore import *
from .client import collection
import pyqtgraph as pg

root = '/home/sliu/beamline_data'

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        record = collection.find_one()
        basename = record['File']

        img_path = os.path.join(root, basename + '.npy')
        data = np.load(img_path)

        view = pg.ImageView()
        self.setCentralWidget(view)
        view.setImage(data)

