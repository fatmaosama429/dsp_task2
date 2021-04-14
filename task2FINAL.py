from PyQt5.uic.properties import QtCore
from PyQt5 import QtCore,QtWidgets,QtPrintSupport
from PyQt5.uic.uiparser import WidgetStack
import numpy as np
import pandas as pd
import pyqtgraph as pg 
from os.path import dirname, realpath,join
from matplotlib.backends.backend_pdf import PdfPages
from PyQt5.uic import  loadUiType
from matplotlib.figure import Figure
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
from scipy.io.wavfile import read, write
from scipy import signal
import wave
from scipy.signal import firwin , freqz
from scipy.fft import rfft, rfftfreq ,fft, fftfreq ,ifft
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import simpleaudio as sa
import soundfile as sf


        
scriptDir=dirname(realpath(__file__))
From_Main,_ = loadUiType(join(dirname(__file__),"main.ui"))
From_Main1,_= loadUiType(join(dirname(__file__),"task1.ui"))
From_Main2,_ = loadUiType(join(dirname(__file__),"main2.ui"))

    
class WINDOW(QMainWindow,From_Main2):
    def __init__(self):
        super(WINDOW, self).__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setGeometry(0, 0, 1350, 690)
        self.create_MenuBar()
    
    def create_MenuBar(self):
        menuBar = self.menuBar()
        self.setMenuBar(menuBar)
        
        file_menu = menuBar.addMenu('Open')
        
        signal_action= QAction(QIcon("icon.png"),"SigViewer", self)
        file_menu.addAction(signal_action)
        signal_action.setShortcut("Alt+shift+n")
        signal_action.triggered.connect(self.viewsigviewer)

        equalize_action = QAction(QIcon('equalizer.png'), 'Equalizer', self)
        equalize_action.setShortcut("alt+n")
        file_menu.addAction(equalize_action)
        equalize_action.triggered.connect(self.newwindow)

    def viewsigviewer(self):
        new=sigviewer()
        new.show()
        new.setWindowTitle("Equalizer")
   
    def newwindow(self):
        new= mainwind()
        new.show()
        new.setWindowTitle("Sigviewer")
        new.setWindowIcon(QIcon("icon.png"))

     
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
        # self.timer2 = QtCore.QTimer()
        self.init_UI()
        self.x=[]
        self.x2=[]
        self.y=[]
        self.y2=[]
        self.cmap= None
        self.speed= 100

        self.l=QVBoxLayout(self.graphicsView)
        self.l.setGeometry(QtCore.QRect(10, 5, 571, 150))
        self.l2=QVBoxLayout(self.graphicsView_3)
        self.l2.setGeometry(QtCore.QRect(10, 500, 571, 150))

        self.l.addWidget(self.sc)
        self.l2.addWidget(self.sc2)    
            
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(660,120,600,280))
        self.label.setText("")

        self.sl1=self.verticalSlider
        self.sl2=self.verticalSlider_2
        self.sl3=self.verticalSlider_3
        self.sl4=self.verticalSlider_4
        self.sl5=self.verticalSlider_5
        self.sl6=self.verticalSlider_6
        self.sl7=self.verticalSlider_7
        self.sl8=self.verticalSlider_8
        self.sl9=self.verticalSlider_9
        self.sl10=self.verticalSlider_10
       
        self.min_freq=self.verticalSlider_11
        self.max_freq=self.verticalSlider_12
        self.min_freq.valueChanged.connect(self.changefreq)
        self.max_freq.valueChanged.connect(self.changefreq)

        self.sl1.valueChanged.connect(self.valuechange)
        self.sl2.valueChanged.connect(self.valuechange)
        self.sl3.valueChanged.connect(self.valuechange)
        self.sl4.valueChanged.connect(self.valuechange)
        self.sl5.valueChanged.connect(self.valuechange)
        self.sl6.valueChanged.connect(self.valuechange)
        self.sl7.valueChanged.connect(self.valuechange)
        self.sl8.valueChanged.connect(self.valuechange)
        self.sl9.valueChanged.connect(self.valuechange)
        self.sl10.valueChanged.connect(self.valuechange)

    def init_UI(self):     
        
        self.createpdf = QtWidgets.QPushButton(self.centralwidget)
        self.createpdf.setGeometry(QtCore.QRect(1270, 23, 75, 591))
        self.createpdf.setText(" Create PDF")
        self.createpdf.setObjectName("pdf")
        self.createpdf.setShortcut("Ctrl+F")
        self.createpdf.clicked.connect(lambda: self.savepdf())


        #  channel 1
        self.open3 = QtWidgets.QPushButton(self.centralwidget)
        self.open3.setGeometry(QtCore.QRect(20, 220, 61, 28))
        self.open3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open3.setIcon(icon1)
        self.open3.setObjectName("open")
        self.open3.setShortcut("Ctrl+O")
        self.open3.clicked.connect(lambda: self.OpenBrowse())

        self.play3 = QtWidgets.QPushButton(self.centralwidget)
        self.play3.setGeometry(QtCore.QRect(90, 220, 61, 28))
        self.play3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play3.setIcon(icon2)
        self.play3.setObjectName("play")
        self.play3.setShortcut("Ctrl+P")
        self.play3.clicked.connect(lambda: self.dynamicSig())

        self.pause3 = QtWidgets.QPushButton(self.centralwidget)
        self.pause3.setGeometry(QtCore.QRect(160, 220, 61, 28))
        self.pause3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause3.setIcon(icon3)
        self.pause3.setObjectName("pause")
        self.pause3.setShortcut("Ctrl+T")
        self.pause3.clicked.connect(lambda: self.pauseSignal())

        self.zoom_in3 = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_in3.setGeometry(QtCore.QRect(230, 220, 61, 28))
        self.zoom_in3.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("zoomin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_in3.setIcon(icon5)
        self.zoom_in3.setObjectName("Zoom In")
        self.zoom_in3.setShortcut("Ctrl+Num++")
        self.zoom_in3.clicked.connect(lambda: self.zoomin())

        self.zoom_out3 = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_out3.setGeometry(QtCore.QRect(300, 220, 61, 28))
        self.zoom_out3.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("zoomout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_out3.setIcon(icon6)
        self.zoom_out3.setObjectName("Zoom Out")
        self.zoom_out3.setShortcut("Ctrl+-")
        self.zoom_out3.clicked.connect(lambda: self.zoomout())

        self.scroll_left3 = QtWidgets.QPushButton(self.centralwidget)
        self.scroll_left3.setGeometry(QtCore.QRect(370, 220, 61, 28))
        self.scroll_left3.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("arrowl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scroll_left3.setIcon(icon8)
        self.scroll_left3.setObjectName("scroll left")
        self.scroll_left3.setShortcut("Ctrl+Left")
        self.scroll_left3.clicked.connect(lambda: self.scrollL())

        self.scroll_right3 = QtWidgets.QPushButton(self.centralwidget)
        self.scroll_right3.setGeometry(QtCore.QRect(440, 220, 61, 28))
        self.scroll_right3.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("arrowr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scroll_right3.setIcon(icon7)
        self.scroll_right3.setObjectName("scroll right")
        self.scroll_right3.setShortcut("Ctrl+Right")
        self.scroll_right3.clicked.connect(lambda: self.scrollR())


        self.colorPalette= QtWidgets.QComboBox()
        self.colorPalette.setGeometry(700, 40 , 500, 28)
        self.colorPalette.addItem("palette 1")
        self.colorPalette.addItem("palette 2")
        self.colorPalette.addItem("palette 3")
        self.colorPalette.addItem("palette 4")
        self.colorPalette.addItem("palette 5")
        self.layout().addWidget(self.colorPalette)
        self.colorPalette.currentIndexChanged.connect(self.combbox)        
        
        self.speedup = QtWidgets.QPushButton(self.centralwidget)
        self.speedup.setGeometry(QtCore.QRect(510, 220, 61, 28))
        self.speedup.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("speed.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speedup.setIcon(icon11)
        self.speedup.setObjectName("speedup")
        self.speedup.setShortcut("Ctrl+up")
        self.speedup.clicked.connect(lambda: self.inc_speed())

        self.slow = QtWidgets.QPushButton(self.centralwidget)
        self.slow.setGeometry(QtCore.QRect(580,220,61,28))
        self.slow.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("slow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.slow.setIcon(icon12)
        self.slow.setObjectName("slow")
        self.slow.setShortcut("Ctrl+Down")
        self.slow.clicked.connect(lambda: self.dec_speed())

    def create_MenuBar(self):
        menuBar = self.menuBar()
        self.setMenuBar(menuBar)
        # self.menuBar.setShortcut("Alt")
        #        menubar file
        file_menu = menuBar.addMenu('file')
        
        newAction=QAction(QIcon("icon.png"), "Sigviewer", self)
        file_menu.addAction(newAction)
        newAction.triggered.connect(self.viewsigviewer)
        newAction.setShortcut("Alt+shift+n")

        newwAction=QAction(QIcon("Equalizer.png"), "Equalizer", self)
        file_menu.addAction(newwAction)
        newwAction.triggered.connect(self.newwindow)
        newwAction.setShortcut("Alt+n")
        
        open_action= QAction(QIcon("open.png"),"open File", self)
        file_menu.addAction(open_action)
        open_action.setShortcut("Alt+O")
        open_action.triggered.connect(self.OpenBrowse)

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

    ##new window##
          
    def viewsigviewer(self):
        new=sigviewer()
        new.show()
        new.setWindowTitle("viewsignals")
   
    def newwindow(self):
        new= mainwind()
        new.show()
        new.setWindowTitle("Sigviewer")
        new.setWindowIcon(QIcon("icon.png"))

    ###CHANNELFUNCTIONS###
    def OpenBrowse(self):
        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)")
        if self.fileName: 
            # self.sc.clear()
            # self.sc2.clear()
            if self.fileName.endswith('.csv'):
                df=pd.read_csv(self.fileName,header=None)
                self.x=np.array(df[0])
                self.y=np.array(df[1]) 
                xrange, yrange = self.sc.viewRange()
                self.min=self.x[0]
                self.max=self.x[-1]
                # print(xrange,self.x[-1])
                self.sc.setXRange(xrange[0]/5, xrange[1]/5, padding=0)
                pen = pg.mkPen(color=(50, 50, 250))
                self.sc.plot(self.x, self.y, pen=pen)
            if self.fileName.endswith('.wav'):
                audiofile= read(self.fileName)
                self.samplingrate = audiofile[0]
                audio=audiofile[1]
                self.audio2= audio.astype(float)
                l=len(audio)
                arr= np.arange(1, (self.samplingrate/2)+1 , 1)
                self.array= arr[::-1]
                logal = 20* (np.log10(self.array/(self.samplingrate/2))*(-1))
                self.min_freq.setMinimum(int(logal[0]))
                self.min_freq.setMaximum(int(logal[-1]))
                self.max_freq.setMinimum(int(logal[0]))
                self.max_freq.setMaximum(int(logal[-1]))
                self.max_freq.setValue(int(logal[-1]))
                self.min_freq.setValue(int(logal[0]))
                # self.min_freq.setTickInterval(5)
                # self.max_freq.setTickInterval(5)
                self.min_freq.setSingleStep(int(logal[-1]/10))
                self.max_freq.setSingleStep(int(logal[-1]/10))
                self.sc.plot(self.audio2[0:l])
                self.sc2.plot(self.audio2[0:l])
                xrange, yrange = self.sc.viewRange()
                self.max=l
                self.min=0
                self.sc.setXRange(xrange[0]/50, xrange[1]/50, padding=0)
                self.sc2.setXRange(xrange[0]/50, xrange[1]/50, padding=0)
                t=1/self.samplingrate
                self.yfft=rfft(self.audio2)
                self.yfft_abs=np.abs(self.yfft)
                self.xfft=rfftfreq(l,t)
                wave_obj = sa.WaveObject.from_wave_file(self.fileName)
                play_obj = wave_obj.play()            
                # self.playaudio(self.fileName)
            self.spectrogram()

    def scrollR(self):
       
        xrange, yrange = self.sc.viewRange()
        scrollvalue = (xrange[1] - xrange[0])/10
        if xrange[1] < self.max:
            self.sc.setXRange(xrange[0]+scrollvalue, xrange[1]+scrollvalue, padding=0)
            self.sc2.setXRange(xrange[0]+scrollvalue, xrange[1]+scrollvalue, padding=0)
            # self.sc.setYrange(yrange[0],yrange[1], padding=0)
        else:
            pass
            
    def scrollL(self):
        xrange, yrange = self.sc.viewRange()
        scrollvalue = (xrange[1] - xrange[0])/10
        if xrange[0]>self.min:
            self.sc.setXRange(xrange[0]-scrollvalue, xrange[1]-scrollvalue, padding=0)
            self.sc2.setXRange(xrange[0]-scrollvalue, xrange[1]-scrollvalue, padding=0)
        else:
            pass
    
    def zoomin(self):
        xrange, yrange = self.sc.viewRange()
        # self.sc.setYRange(yrange[0]/2, yrange[1]/2, padding=0)
        self.sc.setXRange(xrange[0]/2, xrange[1]/2, padding=0)
        self.sc2.setXRange(xrange[0]/2, xrange[1]/2, padding=0)

    def zoomout(self):
        xrange, yrange = self.sc.viewRange()
        if xrange[1]<((0.5*self.max)+1):
            self.sc.setXRange(xrange[0]*2, xrange[1]*2, padding=0)
            self.sc2.setXRange(xrange[0]*2, xrange[1]*2, padding=0)
        else:
            pass
 
    def dynamicSig(self):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(self.speed)
        self.timer.timeout.connect(self.dynamicSig)
        self.timer.start()
        xrange, yrange = self.sc.viewRange()
        scrollvalue = (xrange[1] - xrange[0])/500
        if xrange[1]< self.max:
            self.sc.setXRange(xrange[0]+scrollvalue, xrange[1]+scrollvalue, padding=0)
            self.sc2.setXRange(xrange[0]+scrollvalue, xrange[1]+scrollvalue, padding=0)
        else:
            pass
    
    def inc_speed(self):
        self.speed-=50
        # print (self.speed)

    def dec_speed(self):
        self.speed+= 50
        # print(self.speed)

    def pauseSignal(self):
        self.timer.stop()

    def combbox(self):
        
        if  (self.colorPalette.currentText()=="palette 1"):
            self.cmap=None 
        elif (self.colorPalette.currentText()=="palette 2"):
            self.cmap= cm.get_cmap('copper', 8)
        elif (self.colorPalette.currentText()=="palette 3")     :
            self.cmap= cm.get_cmap('gnuplot2', 12)
        elif (self.colorPalette.currentText()=="palette 4"):
            self.cmap= cm.get_cmap('Greys', 20)
        elif (self.colorPalette.currentText()=="palette 5"):
            self.cmap= cm.get_cmap('Set2', 128)
        self.spectrogram()
        self.valuechange()

    def spectrogram(self):
        #plotting the spectrogram for csv####
        if self.fileName.endswith(".csv"):
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
            self.powerSpectrum, self.freqenciesFound, self.time, self.imageAxis = plot.specgram(self.s2, Fs=self.samplingFrequency, cmap=self.cmap)
            plot.xlabel('Time')
            plot.ylabel('Frequency')
            plot.colorbar()
            fig.savefig('plot.png')
            self.upload()
         #plotting the spectrogram for wav####
        if self.fileName.endswith(".wav"):
            fig = plot.figure()
            plot.subplot(111)
            self.powerSpectrum, self.freqenciesFound, self.time, self.imageAxis = plot.specgram(self.audio2, Fs=self.samplingrate, cmap=self.cmap)
            plot.colorbar()
            plot.xlabel('Time')
            plot.ylabel('Frequency')
            fig.savefig('plot.png')
            self.upload()
            
    def upload(self):
        self.label.setPixmap(QtGui.QPixmap("plot.png"))
        self.label.setScaledContents(True)

    def savepdf(self):
        self.newsignal
        fig=plot.figure()
        # plot.subplot(2,1,1)
        # plot.plot(self.audio2[0:],color='black',linewidth=0.005,scalex=True)
        # plot.title("before")
        plot.subplot(2,1,2)
        self.powerSpectrum, self.freqenciesFound, self.time, self.imageAxis = plot.specgram(self.signal[0:].real, Fs=self.samplingrate,cmap=self.cmap)
        plot.colorbar()
        plot.xlabel('Time')
        plot.ylabel('Frequency')
        plot.subplot(2,1,1)
        plot.plot(self.signal[0:].real ,color='blue',linewidth=0.003,scalex=True)
        plot.title("after")
        fn, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Export PDF", None, "PDF files (.pdf);;All Files()")
        if fn:
            if QtCore.QFileInfo(fn).suffix() == "": fn += ".pdf"
            fig.savefig(fn)
        
        # plot.subplot(2,2,3)
        # plot.plot(self.x2, self.y2,color='red',linewidth=2,scalex=True)
        # plot.subplot(2,2,4)
        # self.powerSpectrum2, self.freqenciesFound2, self.time2, self.imageAxis2 = plot.specgram(self.s2, Fs=self.samplingFrequency)
        # plot.xlabel('Time')
        # plot.ylabel('Frequency')
        # plot.show()
        # fig.savefig("x.pdf")   

    def valuechange(self):
        bandwidth=int(self.samplingrate/20)
        band1=self.yfft[0:bandwidth]*self.sl1.value()
        self.label_13.setText(str(bandwidth))
        band2=self.yfft[bandwidth:2*bandwidth]*self.sl2.value()
        self.label_14.setText(str(2*bandwidth))
        band3=self.yfft[2*bandwidth:3*bandwidth]*self.sl3.value()
        self.label_15.setText(str(3*bandwidth))
        band4=self.yfft[3*bandwidth:4*bandwidth]*self.sl4.value()
        self.label_16.setText(str(4*bandwidth))
        band5=self.yfft[4*bandwidth:5*bandwidth]*self.sl5.value()
        self.label_17.setText(str(5*bandwidth))
        band6=self.yfft[5*bandwidth:6*bandwidth]*self.sl6.value()
        self.label_18.setText(str(6*bandwidth))
        band7=self.yfft[6*bandwidth:7*bandwidth]*self.sl7.value()
        self.label_19.setText(str(7*bandwidth))
        band8=self.yfft[7*bandwidth:8*bandwidth]*self.sl8.value()
        self.label_20.setText(str(8*bandwidth))
        band9=self.yfft[8*bandwidth:9*bandwidth]*self.sl9.value()
        self.label_21.setText(str(9*bandwidth))
        band10=self.yfft[9*bandwidth:10*bandwidth]*self.sl10.value()
        self.label_22.setText(str(10*bandwidth))
        self.new_yfft=np.concatenate([band1,band2,band3,band4,band5,band6,band7,band8,band9,band10])
        self.newsignal()
        # print(band1,self.yfft_abs[0:bandwidth])
        # plot.subplot(2,2,1)
        # plot.plot(self.xfft,abs(self.yfft))
        # plot.title("oldfft")
        # plot.subplot(2,2,2)
        # plot.plot(self.xfft[1:],abs(self.new_yfft))
        # plot.title("newfft")
        # plot.show()
      
    def newsignal(self):
        self.signal=ifft(self.new_yfft)
        t=np.arange(len(self.signal))
        pen = pg.mkPen(color=(255, 255, 255))
        self.sc2.clear()
        self.sc.clear()
        self.sc2.plot(self.signal[0:].real, pen=pen)
        self.sc.plot(self.audio2[0:], pen=pen)
        fig = plot.figure()
        self.powerSpectrum, self.freqenciesFound, self.time, self.imageAxis = plot.specgram(self.signal[0:].real, Fs=self.samplingrate,cmap=self.cmap)
        plot.colorbar()
        plot.xlabel('Time')
        plot.ylabel('Frequency')
        fig.savefig('plot.png')
        self.upload()
        sf.write('sound.wav',self.signal.real, self.samplingrate)
        wave_obj = sa.WaveObject.from_wave_file("sound.wav")
        play_obj = wave_obj.play()

    def changefreq(self):
        if self.max_freq.value()> self.min_freq.value():
            fig = plot.figure()
            plot.subplot(111)
            self.powerSpectrum, self.freqenciesFound, self.time, self.imageAxis = plot.specgram(self.audio2, Fs=self.samplingrate, cmap=self.cmap, vmin= self.min_freq.value(), vmax=self.max_freq.value())
            # self.powerSpectrum, self.freqenciesFound, self.time, self.imageAxis = plot.specgram(self.audio2, Fs=self.samplingrate, cmap=self.cmap)
            # plot.ylim[self.min_freq.value(),self.max_freq.value()]
            plot.xlabel('Time')
            plot.ylabel('Frequency')
            plot.colorbar()
            fig.savefig('plot.png')
            self.upload()
        else:
            pass
  

class sigviewer(QMainWindow,From_Main1):

    def __init__(self):
        super(sigviewer, self).__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setGeometry(0, 0, 1350, 690)
        self.create_MenuBar()
        self.sc =pg.PlotWidget()
        self.sc1 =pg.PlotWidget()
        self.sc2=pg.PlotWidget()
        self.timer = QtCore.QTimer()
        self.timer1 = QtCore.QTimer()
        self.timer2 = QtCore.QTimer()
        self.init_UI()
        self.x=[]
        self.x1=[]
        self.x2=[]
        self.y=[]
        self.y1=[]
        self.y2=[]
        self.speed0=100      
        self.speed1=100
        self.speed2=100

        self.l=QVBoxLayout(self.graphicsView)
        self.l.setGeometry(QtCore.QRect(10, 5, 571, 150))
        self.l1=QVBoxLayout(self.graphicsView_2)
        self.l.setGeometry(QtCore.QRect(10, 210, 571, 150))
        self.l2=QVBoxLayout(self.graphicsView_3)
        self.l.setGeometry(QtCore.QRect(10, 440, 571, 150))


        self.l.addWidget(self.sc)
        self.l1.addWidget(self.sc1)
        self.l2.addWidget(self.sc2)    
            
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(660,8,600,191))
        self.label.setText("")
        
        self.label1 = QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(660,210,600,191))
        self.label1.setText("")
        
        self.label2 = QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(660,420,600,191))
        self.label2.setText("")
        
    def init_UI(self):     
        
        self.createpdf = QtWidgets.QPushButton(self.centralwidget)
        self.createpdf.setGeometry(QtCore.QRect(1270, 23, 75, 591))
        self.createpdf.setText(" Create PDF")
        self.createpdf.setObjectName("pdf")
        self.createpdf.setShortcut("Ctrl+F")
        self.createpdf.clicked.connect(lambda: self.savepdf())
        


        #  channel 1
        self.open3 = QtWidgets.QPushButton(self.centralwidget)
        self.open3.setGeometry(QtCore.QRect(20, 170, 31, 31))
        self.open3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open3.setIcon(icon1)
        self.open3.setObjectName("open")
        self.open3.setShortcut("Ctrl+O")
        self.open3.clicked.connect(lambda: self.OpenBrowse())

        self.play3 = QtWidgets.QPushButton(self.centralwidget)
        self.play3.setGeometry(QtCore.QRect(80, 170, 31, 31))
        self.play3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play3.setIcon(icon2)
        self.play3.setObjectName("play")
        self.play3.setShortcut("Ctrl+P")
        self.play3.clicked.connect(lambda: self.dynamicSig())

        self.pause3 = QtWidgets.QPushButton(self.centralwidget)
        self.pause3.setGeometry(QtCore.QRect(140, 170, 31, 31))
        self.pause3.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause3.setIcon(icon3)
        self.pause3.setObjectName("pause")
        self.pause3.setShortcut("Ctrl+T")
        self.pause3.clicked.connect(lambda: self.pauseSignal())

        self.zoom_in3 = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_in3.setGeometry(QtCore.QRect(200, 170, 31, 31))
        self.zoom_in3.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("zoomin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_in3.setIcon(icon5)
        self.zoom_in3.setObjectName("Zoom In")
        self.zoom_in3.setShortcut("Ctrl+Num++")
        self.zoom_in3.clicked.connect(lambda: self.zoomin())

        self.zoom_out3 = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_out3.setGeometry(QtCore.QRect(260, 170, 31, 31))
        self.zoom_out3.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("zoomout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_out3.setIcon(icon6)
        self.zoom_out3.setObjectName("Zoom Out")
        self.zoom_out3.setShortcut("Ctrl+-")
        self.zoom_out3.clicked.connect(lambda: self.zoomout())

        self.scroll_left3 = QtWidgets.QPushButton(self.centralwidget)
        self.scroll_left3.setGeometry(QtCore.QRect(320, 170, 31, 31))
        self.scroll_left3.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("arrowl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scroll_left3.setIcon(icon8)
        self.scroll_left3.setObjectName("scroll left")
        self.scroll_left3.setShortcut("Ctrl+Left")
        self.scroll_left3.clicked.connect(lambda: self.scrollL())

        self.scroll_right3 = QtWidgets.QPushButton(self.centralwidget)
        self.scroll_right3.setGeometry(QtCore.QRect(380, 170, 31, 31))
        self.scroll_right3.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("arrowr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scroll_right3.setIcon(icon7)
        self.scroll_right3.setObjectName("scroll right")
        self.scroll_right3.setShortcut("Ctrl+Right")
        self.scroll_right3.clicked.connect(lambda: self.scrollR())

        self.speedup1 = QtWidgets.QPushButton(self.centralwidget)
        self.speedup1.setGeometry(QtCore.QRect(440, 170, 31, 31))
        self.speedup1.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("speed.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speedup1.setIcon(icon11)
        self.speedup1.setObjectName("speedup1")
        self.speedup1.setShortcut("Ctrl+up")
        self.speedup1.clicked.connect(lambda: self.inc_speed1())

        self.slow1 = QtWidgets.QPushButton(self.centralwidget)
        self.slow1.setGeometry(QtCore.QRect(500,170,31,31))
        self.slow1.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("slow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.slow1.setIcon(icon12)
        self.slow1.setObjectName("slow1")
        self.slow1.setShortcut("Ctrl+Down")
        self.slow1.clicked.connect(lambda: self.dec_speed1())
        
        self.channel1box = QCheckBox("",self)
        self.channel1box.move(560,190)
        self.channel1box.resize(16,17)
        self.channel1box.setChecked(True)
        self.channel1box.setShortcut("Ctrl+H")
        self.channel1box.stateChanged.connect(self.show1)

        #  channel 2
        self.open1 = QtWidgets.QPushButton(self.centralwidget)
        self.open1.setGeometry(QtCore.QRect(20, 380, 31, 31))
        self.open1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open1.setIcon(icon1)
        self.open1.setObjectName("open")
        self.open1.setShortcut("Shift+O")
        self.open1.clicked.connect(lambda: self.OpenBrowse1())

        self.play1 = QtWidgets.QPushButton(self.centralwidget)
        self.play1.setGeometry(QtCore.QRect(80, 380, 31, 31))
        self.play1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play1.setIcon(icon2)
        self.play1.setObjectName("play")
        self.play1.setShortcut("Shift+P")
        self.play1.clicked.connect(lambda: self.dynamicSig1())

        self.pause1 = QtWidgets.QPushButton(self.centralwidget)
        self.pause1.setGeometry(QtCore.QRect(140, 380,31, 31))
        self.pause1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause1.setIcon(icon3)
        self.pause1.setObjectName("pause")
        self.pause1.setShortcut("Shift+T")
        self.pause1.clicked.connect(lambda: self.pauseSignal1())

        self.zoom_in1 = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_in1.setGeometry(QtCore.QRect(200, 380, 31, 31))
        self.zoom_in1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("zoomin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_in1.setIcon(icon5)
        self.zoom_in1.setObjectName("zoom in")
        self.zoom_in1.setShortcut("Shift+Num++")
        self.zoom_in1.clicked.connect(lambda: self.zoomin1())

        self.zoom_out1 = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_out1.setGeometry(QtCore.QRect(260, 380, 31, 31))
        self.zoom_out1.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("zoomout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_out1.setIcon(icon6)
        self.zoom_out1.setObjectName("zoom out")
        self.zoom_out1.setShortcut("Shift+-")
        self.zoom_out1.clicked.connect(lambda: self.zoomout1())


        self.scroll_left1 = QtWidgets.QPushButton(self.centralwidget)
        self.scroll_left1.setGeometry(QtCore.QRect(320, 380, 31, 31))
        self.scroll_left1.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("arrowl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scroll_left1.setIcon(icon8)
        self.scroll_left1.setObjectName("scroll left")
        self.scroll_left1.setShortcut("Shift+Left")
        self.scroll_left1.clicked.connect(lambda: self.scrollL1())

        self.scroll_right1 = QtWidgets.QPushButton(self.centralwidget)
        self.scroll_right1.setGeometry(QtCore.QRect(380, 380, 31, 31))
        self.scroll_right1.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("arrowr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scroll_right1.setIcon(icon7)
        self.scroll_right1.setObjectName("scroll right")
        self.scroll_right1.setShortcut("Shift+Right")
        self.scroll_right1.clicked.connect(lambda: self.scrollR1())


        self.speedup2 = QtWidgets.QPushButton(self.centralwidget)
        self.speedup2.setGeometry(QtCore.QRect(440, 380, 31, 31))
        self.speedup2.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("speed.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speedup2.setIcon(icon11)
        self.speedup2.setObjectName("speedup2")
        self.speedup2.setShortcut("Shift+up")
        self.speedup2.clicked.connect(lambda: self.inc_speed2())

        self.slow2 = QtWidgets.QPushButton(self.centralwidget)
        self.slow2.setGeometry(QtCore.QRect(500,380,31,31))
        self.slow2.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("slow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.slow2.setIcon(icon12)
        self.slow2.setObjectName("slow2")
        self.slow2.setShortcut("Shift+Down")
        self.slow2.clicked.connect(lambda: self.dec_speed2())
        
        self.channel2box = QCheckBox("",self)
        self.channel2box.move(560,390)
        self.channel2box.resize(16,17)
        self.channel2box.setChecked(True)
        self.channel2box.setShortcut("Shift+H")
        self.channel2box.stateChanged.connect(self.show2)
       
        # channel 3 
        self.open2 = QtWidgets.QPushButton(self.centralwidget)
        self.open2.setGeometry(QtCore.QRect(20, 590, 31, 31))
        self.open2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.open2.setIcon(icon1)
        self.open2.setObjectName("open")
        self.open2.setShortcut("Alt+O")
        self.open2.clicked.connect(lambda: self.OpenBrowse2())

        self.play2 = QtWidgets.QPushButton(self.centralwidget)
        self.play2.setGeometry(QtCore.QRect(80, 590, 31, 31))
        self.play2.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.play2.setIcon(icon2)
        self.play2.setObjectName("play")
        self.play2.setShortcut("Alt+P")
        self.play2.clicked.connect(lambda: self.dynamicSig2())

        self.pause2 = QtWidgets.QPushButton(self.centralwidget)
        self.pause2.setGeometry(QtCore.QRect(140, 590, 31, 31))
        self.pause2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("pause.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pause2.setIcon(icon3)
        self.pause2.setObjectName("pause")
        self.pause2.setShortcut("Alt+T")
        self.pause2.clicked.connect(lambda: self.pauseSignal2())

        self.zoom_in2 = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_in2.setGeometry(QtCore.QRect(200, 590, 31, 31))
        self.zoom_in2.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("zoomin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_in2.setIcon(icon5)
        self.zoom_in2.setObjectName("zoom in")
        self.zoom_in2.setShortcut("Alt+Num++")
        self.zoom_in2.clicked.connect(lambda: self.zoomin2())

        self.zoom_out2 = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_out2.setGeometry(QtCore.QRect(260, 590, 31, 31))
        self.zoom_out2.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("zoomout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_out2.setIcon(icon6)
        self.zoom_out2.setObjectName("zoom out")
        self.zoom_out2.setShortcut("Alt+-")
        self.zoom_out2.clicked.connect(lambda: self.zoomout2())

        self.scroll_left2 = QtWidgets.QPushButton(self.centralwidget)
        self.scroll_left2.setGeometry(QtCore.QRect(320, 590, 31, 31))
        self.scroll_left2.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("arrowl.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scroll_left2.setIcon(icon8)
        self.scroll_left2.setObjectName("scroll left")
        self.scroll_left2.setShortcut("Alt+Left")
        self.scroll_left2.clicked.connect(lambda: self.scrollL2())

        self.scroll_right2 = QtWidgets.QPushButton(self.centralwidget)
        self.scroll_right2.setGeometry(QtCore.QRect(380, 590, 31, 31))
        self.scroll_right2.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("arrowr.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scroll_right2.setIcon(icon7)
        self.scroll_right2.setObjectName("scroll right")
        self.scroll_right2.setShortcut("Alt+Right")
        self.scroll_right2.clicked.connect(lambda: self.scrollR2())

        self.speedup3 = QtWidgets.QPushButton(self.centralwidget)
        self.speedup3.setGeometry(QtCore.QRect(440, 590, 31, 31))
        self.speedup3.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("speed.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.speedup3.setIcon(icon11)
        self.speedup3.setObjectName("speedup3")
        self.speedup3.setShortcut("Alt+up")
        self.speedup3.clicked.connect(lambda: self.inc_speed3())

        self.slow3 = QtWidgets.QPushButton(self.centralwidget)
        self.slow3.setGeometry(QtCore.QRect(500,590,31,31))
        self.slow3.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("slow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.slow3.setIcon(icon12)
        self.slow3.setObjectName("slow3")
        self.slow3.setShortcut("Alt+Down")
        self.slow3.clicked.connect(lambda: self.dec_speed3())
                
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

        newAction=QAction(QIcon("icon.png"), "SigViewer", self)
        file_menu.addAction(newAction)
        newAction.triggered.connect(mainwind.viewsigviewer)
        newAction.setShortcut("Alt+shift+n")

        newwAction=QAction(QIcon("Equalizer.png"), "Equalizer", self)
        file_menu.addAction(newwAction)
        newwAction.triggered.connect(self.newwindow)
        newwAction.setShortcut("Alt+n")
        
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

    ###newwindow###
    def viewsigviewer(self):
        new=sigviewer()
        new.show()
        new.setWindowTitle("viewsignals")

    def newwindow(self):
        new= mainwind()
        new.show()
        new.setWindowTitle("Sigviewer")
        new.setWindowIcon(QIcon("icon.png"))

    ###CHANNEL 1 FUNCTIONS###

    def OpenBrowse(self):
        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*)")
        if self.fileName: 
            if self.fileName.endswith('.csv'):
                df=pd.read_csv(self.fileName,header=None)
                self.x=np.array(df[0])
                self.y=np.array(df[1]) 
                xrange, yrange = self.sc.viewRange()
                self.min=self.x[0]
                self.max=self.x[-1]
                self.sc.setXRange(xrange[0]/5, xrange[1]/5, padding=0)
                pen = pg.mkPen(color=(50, 50, 250))
                self.sc.plot(self.x, self.y, pen=pen)
        self.spectrogram()

    def scrollR(self):
        xrange, yrange = self.sc.viewRange()
        scrollvalue = (xrange[1] - xrange[0])/10
        if xrange[1] < self.max:
            self.sc.setXRange(xrange[0]+scrollvalue, xrange[1]+scrollvalue, padding=0)
        else:
            pass

    def scrollL(self):
        xrange, yrange = self.sc.viewRange()
        scrollvalue = (xrange[1] - xrange[0])/10
        if xrange[0]>self.min:
            self.sc.setXRange(xrange[0]-scrollvalue, xrange[1]-scrollvalue, padding=0)
        else:
            pass

    def zoomin(self):
        xrange, yrange = self.sc.viewRange()
        self.sc.setXRange(xrange[0]/2, xrange[1]/2, padding=0)

    def zoomout(self): 
        xrange, yrange = self.sc.viewRange()
        if xrange[1]<((0.5*self.max)+1):
            self.sc.setXRange(xrange[0]*2, xrange[1]*2, padding=0)
        else:
            pass

    def dynamicSig(self):
        self.timer = QtCore.QTimer()
        self.timer.setInterval(self.speed0)
        self.timer.timeout.connect(self.dynamicSig)
        self.timer.start()
        xrange, yrange = self.sc.viewRange()
        scrollvalue = (xrange[1] - xrange[0])/500
        if xrange[1]< self.max:
            self.sc.setXRange(xrange[0]+scrollvalue, xrange[1]+scrollvalue, padding=0)
        else:
            pass

    def inc_speed1():
        self.speed0-=50

    def dec_speed1():
        self.speed0+=50
            
    def pauseSignal(self):
        self.timer.stop()

    def spectrogram(self):
        #plotting the spectrogram####
        if self.fileName.endswith(".csv"):
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
        if self.fileName.endswith(".wav"):
            fig = plot.figure()
            plot.subplot(111)
            self.powerSpectrum, self.freqenciesFound, self.time, self.imageAxis = plot.specgram(self.audio2, Fs=self.samplingrate)
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
            self.zoom_in3.show()
            self.zoom_out3.show()
            self.scroll_right3.show()
            self.scroll_left3.show()
            self.speedup1.show()
            self.slow1()
        else:    
            self.graphicsView.hide()
            self.label.hide()
            self.open3.hide()
            self.play3.hide()
            self.pause3.hide()
            self.zoom_in3.hide()
            self.zoom_out3.hide()
            self.scroll_right3.hide()
            self.scroll_left3.hide()
            self.speedup1.hide()
            self.slow1.hide()

    ##CHANNEL 2 FUNCTIONS###
    def scrollR1(self):
        xrange, yrange = self.sc1.viewRange()
        scrollvalue = (xrange[1] - xrange[0])/10
        if xrange[1] < self.max1:
            self.sc1.setXRange(xrange[0]+scrollvalue, xrange[1]+scrollvalue, padding=0)
        else:
            pass
    
    def scrollL1(self):
        xrange, yrange = self.sc1.viewRange()
        scrollvalue = (xrange[1] - xrange[0])/10
        if xrange[0]>self.min1:
            self.sc1.setXRange(xrange[0]-scrollvalue, xrange[1]-scrollvalue, padding=0)
        else:
            pass
        
    def zoomin1(self):
        xrange, yrange = self.sc1.viewRange()
        self.sc1.setXRange(xrange[0]/2, xrange[1]/2, padding=0)

    def zoomout1(self):
        xrange, yrange = self.sc1.viewRange()
        if xrange[1]<((0.5*self.max1)+1):
            self.sc1.setXRange(xrange[0]*2, xrange[1]*2, padding=0)
        else:
            pass

    def OpenBrowse1(self):
        self.fileName1, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","CSV Files (*.csv)")
        if self.fileName1: 
            df=pd.read_csv(self.fileName1,header=None)
            self.x1=np.array(df[0])
            self.y1=np.array(df[1]) 
            xrange, yrange = self.sc1.viewRange()
            self.min1=self.x1[0]
            self.max1=self.x1[-1]
            self.sc1.setXRange(xrange[0]/5, xrange[1]/5, padding=0)
            pen = pg.mkPen(color=(50, 50, 250))
            self.sc1.plot(self.x1, self.y1, pen=pen)
        self.spectrogram1()

    def inc_speed2(self):
        self.speed1-=50

    def dec_speed2(self):
        self.speed1+=50

    def dynamicSig1(self):
        # self.clear()
        self.timer1 = QtCore.QTimer()
        self.timer1.setInterval(self.speed1)
        self.timer1.timeout.connect(self.dynamicSig1)
        self.timer1.start()
        xrange, yrange = self.sc1.viewRange()
        scrollvalue = (xrange[1] - xrange[0])/500
        if xrange[1]< self.max1:
            self.sc1.setXRange(xrange[0]+scrollvalue, xrange[1]+scrollvalue, padding=0)
        else:
            pass

    def pauseSignal1(self):
        self.timer1.stop()
    
    def spectrogram1(self):
        #plotting the spectrogram####
        # Define the list of frequencies
        self.frequencies = np.arange(5,105,5)

        # Sampling Frequency
        self.data=pd.DataFrame(pd.read_csv(self.fileName1, delimiter =None))
        self.Data=self.data.iloc[1:][1: ]
        self.sub2 = self.Data.values.tolist()
        self.samplingFrequency   = 2*(len(self.sub2))+1
 
        # Create two ndarrays
        self.s1 = np.empty([0]) # For samples
        self.s2 = np.empty([0]) # For signal
        
        # Start Value of the sample
        self.start = 1

        # Stop Value of the sample
        self.stop = self.samplingFrequency
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
        fig.savefig('plot1.png')
        self.upload1()
        
    def upload1(self):
        self.label1.setPixmap(QtGui.QPixmap("plot1.png"))
        self.label1.setScaledContents(True)    

    def show2(self):
        if(self.channel2box.isChecked()==True):
            self.graphicsView_2.show()
            self.label1.show()
            self.open1.show()
            self.play1.show()
            self.pause1.show()
            self.zoom_in1.show()
            self.zoom_out1.show()
            self.scroll_right1.show()
            self.scroll_left1.show()
            self.speedup2.show()
            self.slow2.show()

        else:    
            self.graphicsView_2.hide()
            self.label1.hide()
            self.open1.hide()
            self.play1.hide()
            self.pause1.hide()
            self.zoom_in1.hide()
            self.zoom_out1.hide()
            self.scroll_right1.hide()
            self.scroll_left1.hide()
            self.speedup2.hide()
            self.slow2.hide()

    ###CHANNEL 3 FUNCTIONS###
    def scrollR2(self):
        xrange, yrange = self.sc2.viewRange()
        scrollvalue = (xrange[1] - xrange[0])/10
        if xrange[1] < self.max2:
            self.sc2.setXRange(xrange[0]+scrollvalue, xrange[1]+scrollvalue, padding=0)
        else:
            pass

    def scrollL2(self):
        xrange, yrange = self.sc2.viewRange()
        scrollvalue = (xrange[1] - xrange[0])/10
        if xrange[0]>self.min2:
            self.sc2.setXRange(xrange[0]-scrollvalue, xrange[1]-scrollvalue, padding=0)
        else:
            pass

    def zoomin2(self):
        xrange, yrange = self.sc2.viewRange()
        self.sc2.setXRange(xrange[0]/2, xrange[1]/2, padding=0)

    def zoomout2(self):
        xrange, yrange = self.sc2.viewRange()
        if xrange[1]<((0.5*self.max2)+1):
            self.sc2.setXRange(xrange[0]*2, xrange[1]*2, padding=0)
        else:
            pass

    def OpenBrowse2(self):
        self.fileName2, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","CSV Files (*.csv)")
        if self.fileName2: 
            df=pd.read_csv(self.fileName2,header=None)
            self.x2=np.array(df[0])
            self.y2=np.array(df[1]) 
            self.min2=self.x2[0]
            self.max2=self.x2[-1]
            xrange, yrange = self.sc2.viewRange()
            self.sc2.setXRange(xrange[0]/5, xrange[1]/5, padding=0)
            pen = pg.mkPen(color=(50, 50, 250))
            self.sc2.plot(self.x2, self.y2, pen=pen)
        self.spectrogram2()
    
    def inc_speed3(self):
        self.speed2-=50

    def dec_speed3(self):
        self.speed2+=50

    def dynamicSig2(self):
        # self.clear()
        self.timer2 = QtCore.QTimer()
        self.timer2.setInterval(self.speed2)
        self.timer2.timeout.connect(self.dynamicSig2)
        self.timer2.start()
        xrange, yrange = self.sc2.viewRange()
        scrollvalue = (xrange[1] - xrange[0])/500
        if xrange[1]< self.max2:
            self.sc2.setXRange(xrange[0]+scrollvalue, xrange[1]+scrollvalue, padding=0)
        else:
            pass

    def pauseSignal2(self):
        self.timer2.stop()

    def spectrogram2(self):
        #plotting the spectrogram####
        # Define the list of frequencies
        self.frequencies = np.arange(5,105,5)

        # Sampling Frequency
        self.data=pd.DataFrame(pd.read_csv(self.fileName2, delimiter =None))
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
        fig.savefig('plot2.png')
        self.upload2()

    def upload2(self):
        self.label2.setPixmap(QtGui.QPixmap("plot2.png"))
        self.label2.setScaledContents(True)

    def show3(self):
        if(self.channel3box.isChecked()==True):
            self.graphicsView_3.show()
            self.label2.show()
            self.open2.show()
            self.play2.show()
            self.pause2.show()
            self.zoom_in2.show()
            self.zoom_out2.show()
            self.scroll_right2.show()
            self.scroll_left2.show()
            self.speedup3.show()
            self.slow3.show()

        else:   
            self.graphicsView_3.hide()
            self.label2.hide()
            self.open2.hide()
            self.play2.hide()
            self.pause2.hide()
            self.zoom_in2.hide()
            self.zoom_out2.hide()
            self.scroll_right2.hide()
            self.scroll_left2.hide()
            self.speedup3.hide()
            self.slow3.hide()

     ##save to pdf function##

    def savepdf(self):
        fig=plot.figure()

        if(self.channel1box.isChecked()==True):
            if len(self.x)==0:
               pass    
            else:
                plot.subplot(6,1,1)
                plot.plot(self.x, self.y,color='red',linewidth=0.5,scalex=True)
                plot.subplot(6,1,2)
                self.powerSpectrum, self.freqenciesFound, self.time, self.imageAxis = plot.specgram(self.s2, Fs=self.samplingFrequency)
                plot.xlabel('Time')
                plot.ylabel('Frequency')
        if(self.channel2box.isChecked()==True):
            if len(self.x1) ==0 :
                pass
            else:
                plot.subplot(6,1,3)
                plot.plot(self.x1,self.y1,color='orange',linewidth=0.5,scalex=True)
                plot.subplot(6,1,4)
                self.powerSpectrum1, self.freqenciesFound1, self.time1, self.imageAxis1 = plot.specgram(self.s2, Fs=self.samplingFrequency)
                plot.xlabel('Time')
                plot.ylabel('Frequency')
        if(self.channel3box.isChecked()==True):
            if len(self.x2) ==0 :
                pass
            else:
                plot.subplot(6,1,5)
                plot.plot(self.x2, self.y2,color='green',linewidth=0.5,scalex=True)
                plot.subplot(6,1,6)
                self.powerSpectrum2, self.freqenciesFound2, self.time2, self.imageAxis2 = plot.specgram(self.s2, Fs=self.samplingFrequency)
                plot.xlabel('Time')
                plot.ylabel('Frequency')   
        fn, _ = QtWidgets.QFileDialog.getSaveFileName(
            self, "Export PDF", None, "PDF files (.pdf);;All Files()")
        if fn:
            if QtCore.QFileInfo(fn).suffix() == "": fn += ".pdf"
            fig.savefig(fn)
                
 

app = QApplication(sys.argv)
sheet= WINDOW()
sheet.show()
sheet.setWindowTitle("Sigviewer")
sheet.setWindowIcon(QIcon("icon.png"))
sys.exit(app.exec_())

