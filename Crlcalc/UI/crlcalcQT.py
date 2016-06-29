'''
Created on 18.04.2016

@author: Woehnert
'''

import qt_builder
from PyQt4 import QtGui
import sys



class CrlcalcQT(QtGui.QMainWindow, qt_builder.Ui_ScrollArea):
    '''
    Graphical interface between python code and User.
    Based in qt
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(self.__class__, self).__init__()
        self.setupUi(self)
        