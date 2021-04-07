from PyQt5.uic.properties import QtCore
from PyQt5 import QtCore,QtWidgets,QtPrintSupport
from PyQt5.uic.uiparser import WidgetStack
import numpy as np
import pandas as pd
import pyqtgraph as pg 
from os.path import dirname, realpath,join
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import  QApplication, QMainWindow,QVBoxLayout,QAction,QFileDialog, QPushButton, QLabel, QCheckBox
from PyQt5.QtCore import pyqtSlot
from matplotlib.backends.backend_pdf import PdfPages
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.uic import  loadUiType
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QMenu
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtCore import QAbstractEventDispatcher, QFileInfo
from PyQt5 import QtWidgets, QtCore, uic,QtGui
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from pyqtgraph import PlotWidget, plot
import numpy as np
from random import randint
import csv 
import pandas as pd
import os
from os import path
import sys
import matplotlib.pyplot as plot
import pyautogui
from PIL import Image

        
scriptDir=dirname(realpath(__file__))
From_Main,_= loadUiType(join(dirname(__file__),"main (1).ui"))


class mainwind(QMainWindow,From_Main):

    def __init__(self):
        super(mainwind, self).__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setGeometry(0, 0, 1350, 690)
        self.create_MenuBar()
        self.sc =pg.PlotWidget()
        self.sc2=pg.PlotWidget()
        self.timer = QtCore.QTimer()
        self.timer2 = QtCore.QTimer()
        self.init_UI()
        self.x=[]
        self.x2=[]
        self.y=[]
        self.y2=[]

        self.l=QVBoxLayout(self.graphicsView)
        self.l.setGeometry(QtCore.QRect(10, 5, 571, 150))
        self.l2=QVBoxLayout(self.graphicsView_3)
        self.l2.setGeometry(QtCore.QRect(10, 440, 571, 150))


        self.l.addWidget(self.sc)
        self.l2.addWidget(self.sc2)    
            
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(660,8,600,191))
        self.label.setText("")
        self.label.setStyleSheet("background-color: white")
        
        
        self.label2 = QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(660,420,600,191))
        self.label2.setText("")
        self.label2.setStyleSheet("background-color: white")  


    def init_UI(self):     
        
        self.createpdf = QtWidgets.QPushButton(self.centralwidget)
        self.createpdf.setGeometry(QtCore.QRect(1270, 23, 75, 591))
        self.createpdf.setText(" Create PDF")
        self.createpdf.setObjectName("pdf")
        self.createpdf.setShortcut("Ctrl+F")
        self.createpdf.clicked.connect(lambda: self.savepdf())


        #  channel 1
        self.open3 = QtWidgets.QPushButton(self.centralwidget)
        self.open3.setGeometry(QtCore.QRect(20, 170, 41, 23))
        self.open3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open3.setIcon(icon1)
        self.open3.setObjectName("open")
        self.open3.setShortcut("Ctrl+O")
        self.open3.clicked.connect(lambda: self.OpenBrowse())

        self.play3 = QtWidgets.QPushButton(self.centralwidget)
        self.play3.setGeometry(QtCore.QRect(80, 170, 41, 23))
        self.play3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play3.setIcon(icon2)
        self.play3.setObjectName("play")
        self.play3.setShortcut("Ctrl+P")
        self.play3.clicked.connect(lambda: self.dynamicSig())

        self.pause3 = QtWidgets.QPushButton(self.centralwidget)
        self.pause3.setGeometry(QtCore.QRect(140, 170, 41, 23))
        self.pause3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause3.setIcon(icon3)
        self.pause3.setObjectName("pause")
        self.pause3.setShortcut("Ctrl+T")
        self.pause3.clicked.connect(lambda: self.pauseSignal())

        self.clear3 = QtWidgets.QPushButton(self.centralwidget)
        self.clear3.setGeometry(QtCore.QRect(200, 170, 41, 23))
        self.clear3.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear3.setIcon(icon4)
        self.clear3.setObjectName("clear")
        self.clear3.setShortcut("Ctrl+L")
        self.clear3.clicked.connect(lambda: self.clear())

        self.zoom_in3 = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_in3.setGeometry(QtCore.QRect(260, 170, 41, 23))
        self.zoom_in3.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("zoomin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_in3.setIcon(icon5)
        self.zoom_in3.setObjectName("Zoom In")
        self.zoom_in3.setShortcut("Ctrl+Num++")
        self.zoom_in3.clicked.connect(lambda: self.zoomin())

        self.zoom_out3 = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_out3.setGeometry(QtCore.QRect(320, 170, 41, 23))
        self.zoom_out3.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("zoomout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_out3.setIcon(icon6)
        self.zoom_out3.setObjectName("Zoom Out")
        self.zoom_out3.setShortcut("Ctrl+-")
        self.zoom_out3.clicked.connect(lambda: self.zoomout())

        self.scroll_right3 = QtWidgets.QPushButton(self.centralwidget)
        self.scroll_right3.setGeometry(QtCore.QRect(380, 170, 41, 23))
        self.scroll_right3.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("arrowr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scroll_right3.setIcon(icon7)
        self.scroll_right3.setObjectName("scroll right")
        self.scroll_right3.setShortcut("Ctrl+Right")
        self.scroll_right3.clicked.connect(lambda: self.scrollR())

        self.scroll_left3 = QtWidgets.QPushButton(self.centralwidget)
        self.scroll_left3.setGeometry(QtCore.QRect(440, 170, 41, 23))
        self.scroll_left3.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("arrowl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scroll_left3.setIcon(icon8)
        self.scroll_left3.setObjectName("scroll left")
        self.scroll_left3.setShortcut("Ctrl+Left")
        self.scroll_left3.clicked.connect(lambda: self.scrollL())

        self.spectrogram3 = QtWidgets.QPushButton(self.centralwidget)
        self.spectrogram3.setGeometry(QtCore.QRect(500, 170, 41, 23))
        self.spectrogram3.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("spectro.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.spectrogram3.setIcon(icon9)
        self.spectrogram3.setObjectName("spectrogram")
        self.spectrogram3.setShortcut("Ctrl+M")
        self.spectrogram3.clicked.connect(lambda: self.spectrogram())

        self.channel1box = QCheckBox("",self)
        self.channel1box.move(560,190)
        self.channel1box.resize(16,17)
        self.channel1box.setChecked(True)
        self.channel1box.setShortcut("Ctrl+H")
        self.channel1box.stateChanged.connect(self.show1)
      
        # channel 3 
        self.channel3box = QCheckBox("",self)
        self.channel3box.move(560,610)
        self.channel3box.resize(16,17)
        self.channel3box.setChecked(True)
        self.channel3box.setShortcut("Alt+H")
        self.channel3box.stateChanged.connect(self.show3)
        

    def create_MenuBar(self):
        menuBar = self.menuBar()
        self.setMenuBar(menuBar)
        # self.menuBar.setShortcut("Alt")
        #        menubar file
        file_menu = menuBar.addMenu('file')
        
        open_action= QAction(QIcon("open.png"),"open File", self)
        file_menu.addAction(open_action)

        saveAction= QAction(QIcon("save.png"), "save", self)
        file_menu.addAction(saveAction)

        gdfAction=QAction("Export GDF...", self)
        file_menu.addAction(gdfAction)

        eventsAction=QAction("Export Events...", self)
        file_menu.addAction(eventsAction)

        importAction=QAction("Import Events...", self)
        file_menu.addAction(importAction)

        infoAction=QAction(QIcon("info.png"), "Info...", self)
        file_menu.addAction(infoAction)

        closeAction=QAction(QIcon("close.png"), "Close", self)
        file_menu.addAction(closeAction)
        closeAction.triggered.connect(self.close)
        closeAction.setShortcut("Ctrl+Q")
        
        # menubar  edit
        edit_menu = menuBar.addMenu('edit')
                
        undoAction=QAction(QIcon("undo.png"), "Undo", self)
        edit_menu.addAction(undoAction)

        redoAction =QAction(QIcon("redo.png"), "Redo", self)
        edit_menu.addAction(redoAction)

        toallAction =QAction(QIcon("to_all.png"), "to All Channels", self)
        edit_menu.addAction(toallAction)
                
        copyAction =QAction(QIcon("copy.png"), "Copy to Channels...", self)
        edit_menu.addAction(copyAction)

        deleteAction =QAction(QIcon("delete.png"), "Delete", self)
        edit_menu.addAction(deleteAction)
        
        changeAction =QAction(QIcon("change.png"), "Change Channel...", self)
        edit_menu.addAction(changeAction)

        typeAction =QAction(QIcon("color.png"), "Change Type", self)
        edit_menu.addAction(typeAction)

        insertAction =QAction(QIcon("add.png"), "Insert Over", self)
        edit_menu.addAction(insertAction)

        edit_menu.addAction('Quit',self.close)
                
        # menubar  mode
        mode_menu = menuBar.addMenu('mode')

        newAction =QAction(QIcon("new event.png"), "New Event", self)
        mode_menu.addAction(newAction)

        editAction =QAction(QIcon("edit.png"), "Edit Event", self)
        mode_menu.addAction(editAction)
        scrollAction =QAction(QIcon("scroll.png"), "Scroll", self)
        mode_menu.addAction(scrollAction)

        viewAction =QAction(QIcon("view.png"), "View Options", self)
        mode_menu.addAction(viewAction)

        
        # menubar  view
        view_menu = menuBar.addMenu('view')

        toolbarAction =QAction("Toolbars", self)
        view_menu.addAction(toolbarAction)

        statusAction =QAction( "Statusbar", self)
        view_menu.addAction(statusAction)

        animationAction =QAction( "Animation", self)
        view_menu.addAction(animationAction)

        eveAction =QAction(QIcon("favourite.png"), "Events...", self)
        view_menu.addAction(eveAction)

        channAction =QAction(QIcon("channels.png"), "Channels...", self)
        view_menu.addAction(channAction)        

        scaleAction =QAction("Scale All", self)
        view_menu.addAction(scaleAction)

        zoominvAction =QAction(QIcon("zoomin.png"), "Zoom In Vertical", self)
        view_menu.addAction(zoominvAction)

        zoomoutvAction =QAction(QIcon("zoom out.png"), "Zoom Out Vertical", self)
        view_menu.addAction(zoomoutvAction)

        zoominhAction =QAction(QIcon("zoomin.png"), "Zoom In Horizontal", self)
        view_menu.addAction(zoominhAction)

        zoomouthAction =QAction(QIcon("zoom out.png"), "Zoom Out Horizontal", self)
        view_menu.addAction(zoomouthAction)

        gotoAction =QAction(QIcon("goto.png"), "Go to...", self)
        view_menu.addAction(gotoAction)

        gonextAction =QAction( "Goto and Select Next Event", self)
        view_menu.addAction(gonextAction)

        goprevAction =QAction("Goto and Select Previos Evenet", self)
        view_menu.addAction(goprevAction)

        fitAction =QAction("Fit View to selected Event", self)
        view_menu.addAction(fitAction)

        hideAction =QAction("Hide Events of Other Type", self)
        view_menu.addAction(hideAction)

        showAction =QAction("Show All Events", self)
        view_menu.addAction(showAction)    

        
        # menubar  tools
        tools_menu = menuBar.addMenu('tools')
        
        calcAction =QAction("Calculate Mean...", self)
        tools_menu.addAction(calcAction)

        powerAction =QAction("Power Spectrum...", self)
        tools_menu.addAction(powerAction)

        
        # menubar  help
        help_menu = menuBar.addMenu('help')
        help_menu.addAction('Quit',self.close)       


    ###CHANNEL 1 FUNCTIONS###

    def OpenBrowse(self):
        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","CSV Files (*.csv)")
        if self.fileName: 
            df=pd.read_csv(self.fileName,header=None)
            self.x=np.array(df[0])
            self.y=np.array(df[1]) 
            xrange, yrange = self.sc.viewRange()
            self.sc.setXRange(xrange[0]/5, xrange[1]/5, padding=0)
            pen = pg.mkPen(color=(50, 50, 250))
            self.sc.plot(self.x, self.y, pen=pen)

    def scrollR(self):
        xrange, yrange = self.sc.viewRange()
        scrollvalue = (xrange[1] - xrange[0])/10
        self.sc.setXRange(xrange[0]+scrollvalue, xrange[1]+scrollvalue, padding=0)
        # self.sc.setYrange(yrange[0],yrange[1], padding=0)

    def scrollL(self):
        xrange, yrange = self.sc.viewRange()
        scrollvalue = (xrange[1] - xrange[0])/10
        self.sc.setXRange(xrange[0]-scrollvalue, xrange[1]-scrollvalue, padding=0)
        # self.sc.setYrange(yrange[0],yrange[1], padding=0)

    def zoomin(self):
        xrange, yrange = self.sc.viewRange()
        # self.sc.setYRange(yrange[0]/2, yrange[1]/2, padding=0)
        self.sc.setXRange(xrange[0]/2, xrange[1]/2, padding=0)

    def zoomout(self):
        xrange, yrange = self.sc.viewRange()
        # self.sc.setYRange(yrange[0]*2, yrange[1]*2, padding=0)
        self.sc.setXRange(xrange[0]*2, xrange[1]*2, padding=0)

    def clear(self):
        self.sc.clear()
    
    def dynamicSig(self):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.dynamicSig)
        self.timer.start()
        xrange, yrange = self.sc.viewRange()
        scrollvalue = (xrange[1] - xrange[0])/500
        self.sc.setXRange(xrange[0]+scrollvalue, xrange[1]+scrollvalue, padding=0)

    def pauseSignal(self):
        self.timer.stop()

    def spectrogram(self):
        #plotting the spectrogram####
        # Define the list of frequencies
        self.frequencies = np.arange(5,105,5)

        # Sampling Frequency
        self.data=pd.DataFrame(pd.read_csv(self.fileName, delimiter =None))
        self.Data=self.data.iloc[1:][1: ]
        self.sub2 = self.Data.values.tolist()
        self.samplingFrequency   = 2*(len(self.sub2))+1
 
        # Create two ndarrays
        self.s1 = np.empty([0]) # For samples
        self.s2 = np.empty([0]) # For signal
        
        # Start Value of the sample
        self.start   = 1

        # Stop Value of the sample
        self.stop    = self.samplingFrequency
        for self.frequency in self.frequencies:

            self.sub1 = np.arange(self.start, self.stop, 1)

        self.s1      = np.append(self.s1, self.sub1)
        self.s2      = np.append(self.s2, self.sub2)
        self.start   = self.stop+1
        self.stop    = self.start+self.samplingFrequency

        # Plot the spectrogram
        fig = plot.figure()
        plot.subplot(111)
        self.powerSpectrum, self.freqenciesFound, self.time, self.imageAxis = plot.specgram(self.s2, Fs=self.samplingFrequency)
        plot.xlabel('Time')
        plot.ylabel('Frequency')
        fig.savefig('plot.png')
        self.upload()
        
    def upload(self):
        self.label.setPixmap(QtGui.QPixmap("plot.png"))
        self.label.setScaledContents(True)

    def show1(self):
        if(self.channel1box.isChecked()==True):
            self.graphicsView.show()
            self.label.show()
            self.open3.show()
            self.play3.show()
            self.pause3.show()
            self.clear3.show()
            self.zoom_in3.show()
            self.zoom_out3.show()
            self.scroll_right3.show()
            self.scroll_left3.show()
            self.spectrogram3.show()

        else:    
            self.graphicsView.hide()
            self.label.hide()
            self.open3.hide()
            self.play3.hide()
            self.pause3.hide()
            self.clear3.hide()
            self.zoom_in3.hide()
            self.zoom_out3.hide()
            self.scroll_right3.hide()
            self.scroll_left3.hide()
            self.spectrogram3.hide()
    # channel 3
    def show3(self):
        if(self.channel3box.isChecked()==True):
            self.graphicsView_3.show()
            self.label2.show()
            # self.open2.show()
            # self.play2.show()
            # self.pause2.show()
            # self.clear_2.show()
            # self.zoom_in2.show()
            # self.zoom_out2.show()
            # self.scroll_right2.show()
            # self.scroll_left2.show()
            # self.spectrogram_2.show()

        else:   
            self.graphicsView_3.hide()
            self.label2.hide()
            # self.open2.hide()
            # self.play2.hide()
            # self.pause2.hide()
            # self.clear_2.hide()
            # self.zoom_in2.hide()
            # self.zoom_out2.hide()
            # self.scroll_right2.hide()
            # self.scroll_left2.hide()
            # self.spectrogram_2.hide()

    ##save to pdf function##

    def savepdf(self):
        fig=plot.figure()

        if(self.channel1box.isChecked()==True):
            if len(self.x)==0:
               pass    
            else:
                plot.subplot(3,2,1)
                plot.plot(self.x, self.y,color='red',linewidth=2,scalex=True)
                plot.subplot(3,2,2)
                self.powerSpectrum, self.freqenciesFound, self.time, self.imageAxis = plot.specgram(self.s2, Fs=self.samplingFrequency)
                plot.xlabel('Time')
                plot.ylabel('Frequency')
        # if(self.channel2box.isChecked()==True):
        #     if len(self.x1) ==0 :
        #         pass
        #     else:
        #         plot.subplot(3,2,3)
        #         plot.plot(self.x1,self.y1,color='red',linewidth=2,scalex=True)
        #         plot.subplot(3,2,4)
        #         self.powerSpectrum1, self.freqenciesFound1, self.time1, self.imageAxis1 = plot.specgram(self.s2, Fs=self.samplingFrequency)
        #         plot.xlabel('Time')
                plot.ylabel('Frequency')
        if(self.channel3box.isChecked()==True):
            if len(self.x2) ==0 :
                pass
            else:
                plot.subplot(3,2,5)
                plot.plot(self.x2, self.y2,color='red',linewidth=2,scalex=True)
                plot.subplot(3,2,6)
                self.powerSpectrum2, self.freqenciesFound2, self.time2, self.imageAxis2 = plot.specgram(self.s2, Fs=self.samplingFrequency)
                plot.xlabel('Time')
                plot.ylabel('Frequency')
        # plot.show()
        fig.savefig("x.pdf")   


app = QApplication(sys.argv)
sheet= mainwind()
sheet.show()
sheet.setWindowTitle("Sigviewer")
sheet.setWindowIcon(QIcon("icon.png"))
sys.exit(app.exec_())

