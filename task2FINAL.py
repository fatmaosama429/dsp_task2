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
        # self.menuBar.setShortcut("Alt")
        #        menubar file
        file_menu = menuBar.addMenu('file')
        
        # newAction=QAction(QIcon("icon.png"), "Sigviewer", self)
        # file_menu.addAction(newAction)
        # newAction.triggered.connect(self.viewsigviewer)
        # newAction.setShortcut("Alt+shift+n")

        newwAction=QAction(QIcon("Equalizer.png"), "Equalizer", self)
        file_menu.addAction(newwAction)
        newwAction.triggered.connect(self.newwindow)
        newwAction.setShortcut("Alt+n")
        
        open_action= QAction(QIcon("open.png"),"open File", self)
        file_menu.addAction(open_action)
        open_action.setShortcut("Alt+O")
        # open_action.triggered.connect(self.OpenBrowse)

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

        self.slider_band1=self.verticalSlider
        self.slider_band2=self.verticalSlider_2
        self.slider_band3=self.verticalSlider_3
        self.slider_band4=self.verticalSlider_4
        self.slider_band5=self.verticalSlider_5
        self.slider_band6=self.verticalSlider_6
        self.slider_band7=self.verticalSlider_7
        self.slider_band8=self.verticalSlider_8
        self.slider_band9=self.verticalSlider_9
        self.slider_band10=self.verticalSlider_10
       
        self.min_freq_slider=self.verticalSlider_11
        self.max_freq_slider=self.verticalSlider_12
        self.min_freq_slider.valueChanged.connect(self.changefreq)
        self.max_freq_slider.valueChanged.connect(self.changefreq)

        self.slider_band1.valueChanged.connect(self.valuechange)
        self.slider_band2.valueChanged.connect(self.valuechange)
        self.slider_band3.valueChanged.connect(self.valuechange)
        self.slider_band4.valueChanged.connect(self.valuechange)
        self.slider_band5.valueChanged.connect(self.valuechange)
        self.slider_band6.valueChanged.connect(self.valuechange)
        self.slider_band7.valueChanged.connect(self.valuechange)
        self.slider_band8.valueChanged.connect(self.valuechange)
        self.slider_band9.valueChanged.connect(self.valuechange)
        self.slider_band10.valueChanged.connect(self.valuechange)

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
        self.pause3.setShortcut("Ctrl+shift+p")
        self.pause3.clicked.connect(lambda: self.pauseSignal())

        self.zoom_in3 = QtWidgets.QPushButton(self.centralwidget)
        self.zoom_in3.setGeometry(QtCore.QRect(230, 220, 61, 28))
        self.zoom_in3.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("zoomin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.zoom_in3.setIcon(icon5)
        self.zoom_in3.setObjectName("Zoom In")
        self.zoom_in3.setShortcut("Ctrl++")
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
        self.colorPalette.addItem("virdis")
        self.colorPalette.addItem('Spectral_r')
        self.colorPalette.addItem("gnuplot2")
        self.colorPalette.addItem("Greys")
        self.colorPalette.addItem("Set2")

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
        
        # newAction=QAction(QIcon("icon.png"), "Sigviewer", self)
        # file_menu.addAction(newAction)
        # newAction.triggered.connect(self.viewsigviewer)
        # newAction.setShortcut("Alt+shift+n")

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
   
    def newwindow(self):
        new= mainwind()
        new.show()
        new.setWindowTitle("Sigviewer")
        new.setWindowIcon(QIcon("icon.png"))

    ###CHANNELFUNCTIONS###
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
                self.min_max()
                self.sc.plot(self.audio2[0:l])
                self.sc2.plot(self.audio2[0:l])
                xrange, yrange = self.sc.viewRange()
                self.max=l
                self.min=0
                self.sc.setXRange(xrange[0]/50, xrange[1]/50, padding=0)
                self.sc2.setXRange(xrange[0]/50, xrange[1]/50, padding=0)
                t=1/self.samplingrate
                self.yfft=fft(self.audio2)
                self.yfft_abs=np.abs(self.yfft)
                self.xfft=fftfreq(l,t)
                wave_obj = sa.WaveObject.from_wave_file(self.fileName)
                # play_obj = wave_obj.play()
                self.bandwidthedit()    
                        
                
            self.spectrogram()

    def bandwidthedit(self):
        bandwidth=int(self.samplingrate/20)
        self.label_13.setText(str(bandwidth))
        self.label_14.setText(str(2*bandwidth))
        self.label_15.setText(str(3*bandwidth))
        self.label_16.setText(str(4*bandwidth))
        self.label_17.setText(str(5*bandwidth))
        self.label_18.setText(str(6*bandwidth))
        self.label_19.setText(str(7*bandwidth))
        self.label_20.setText(str(8*bandwidth))
        self.label_21.setText(str(9*bandwidth))
        self.label_22.setText(str(10*bandwidth))
    
    def min_max(self):
        fmax=self.samplingrate/2
        arr= np.arange(1,(fmax+1) , 1)
        self.array= arr[::-1]
        logal = -20* (np.log10(self.array/(fmax)))
        
        self.min_freq_slider.setMinimum(logal[0])
        self.min_freq_slider.setMaximum(logal[-1])
        self.max_freq_slider.setMinimum(logal[0])
        self.max_freq_slider.setMaximum(logal[-1])

        self.max_freq_slider.setValue(logal[-1])
        self.min_freq_slider.setValue(0)

        self.min_freq_slider.setSingleStep(int(logal[-1]/10))
        self.max_freq_slider.setSingleStep(int(logal[-1]/10))

    def scrollR(self):  
        xrange, yrange = self.sc.viewRange()   
        if xrange[1] < self.max:
            self.scrollvalue = (xrange[1] - xrange[0])/10
            self.scroll()          
    
    def scrollL(self):
        xrange, yrange= self.sc.viewRange()
        if xrange[0]>self.min:
            self.scrollvalue = -1 * ((xrange[1] - xrange[0])/10)
            self.scroll()
        
    def scroll(self):
        xrange, yrange = self.sc.viewRange()   
        self.sc.setXRange(xrange[0]+self.scrollvalue, xrange[1]+self.scrollvalue, padding=0)
        self.sc2.setXRange(xrange[0]+self.scrollvalue, xrange[1]+self.scrollvalue, padding=0)
             
    def zoomin(self):
        self.factor = 0.5
        self.zoom()

    def zoomout(self):
        xrange, yrange = self.sc.viewRange()
        if xrange[1]<((0.5*self.max)+1):
            self.factor = 2
            self.zoom()

    def zoom(self):
            xrange, yrange = self.sc.viewRange()
            self.sc.setXRange(xrange[0]*self.factor, xrange[1]*self.factor, padding=0)
            self.sc2.setXRange(xrange[0]*self.factor, xrange[1]*self.factor, padding=0)
        
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
        if self.speed>0:
            self.speed-=5
        elif self.speed == 0:
            self.speed=2
        print (self.speed)

    def dec_speed(self):
        self.speed+= 5
        if self.speed > 255:
            self.speed= 255
        print(self.speed)

    def pauseSignal(self):
        self.timer.stop()

    def combbox(self):
        self.cmap= cm.get_cmap(str(self.colorPalette.currentText()))
        self.valuechange()
        
    def spectrogram(self):
        #plotting the spectrogram for .wav####
        if self.fileName.endswith(".wav"):
            fig = plot.figure()
            plot.subplot(111)
            self.powerSpectrum, self.freqenciesFound, self.time, self.imageAxis = plot.specgram(self.audio2, Fs=self.samplingrate, cmap=self.cmap)
            # plot.colorbar()
            # plot.ylim(self.min_freq_slider.value(),self.max_freq_slider.value())
            plot.xlabel('Time')
            plot.ylabel('Frequency')
            fig.savefig('plot.png')
            plot.close()
            self.upload()

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
            plot.close()
            self.upload()
         #plotting the spectrogram for wav####
                   
    def upload(self):
        self.label.setPixmap(QtGui.QPixmap("plot.png"))
        self.label.setScaledContents(True)

    def savepdf(self):
        # self.newsignal()
        fig=plot.figure()
        # plot.subplot(2,1,1)
        # plot.plot(self.audio2[0:],color='black',linewidth=0.005,scalex=True)
        # plot.title("before")
        plot.subplot(2,1,2)
        self.powerSpectrum, self.freqenciesFound, self.time, self.imageAxis = plot.specgram(self.signal[0:].real, Fs=self.samplingrate,cmap=self.cmap)
        # plot.colorbar()
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
        plot.close()
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

        self.new_yfft=self.yfft.copy()

        self.sliders_list=[self.slider_band1.value(),self.slider_band2.value(),self.slider_band3.value(),\
            self.slider_band4.value(),self.slider_band5.value(),self.slider_band6.value(),self.slider_band7.value(),\
                self.slider_band8.value(),self.slider_band9.value(),self.slider_band10.value()]
        
        for i in np.arange(10):
            self.new_yfft[i*bandwidth:(i+1)*bandwidth]=self.new_yfft[i*bandwidth:(i+1)*bandwidth]*self.sliders_list[i]
        self.newsignal()   

        # fig=plot.figure()
        # plot.close()
        # plot.clf()
        # plot.subplot(2,2,1)
        # plot.plot(self.xfft,abs(self.yfft))
        # plot.title("oldfft")
        # plot.subplot(2,2,2)
        # plot.plot(self.xfft,abs(self.new_yfft))
        # plot.title("newfft")
        # plot.show()
      
    def newsignal(self):

        
        mag= np.abs(self.new_yfft)
        phase= np.angle(self.new_yfft)
        mod_wave=np.multiply(mag,np.exp(1j*phase))
        self.signal=ifft(mod_wave)

        pen = pg.mkPen(color=(255, 255, 255))
        self.sc2.clear()
        # self.sc.clear()

        # self.signal=ifft(self.new_yfft)
        # mag= np.abs(self.signal)
        # phase= np.angle(self.signal)
        # mod_wave=np.multiply(mag,np.exp(1j*phase))
        # self.sc2.plot(mod_wave[0:].real, pen=pen)

        self.sc2.plot(self.signal.real, pen=pen)
        # self.sc.plot(self.audio2[0:], pen=pen)
        max= self.max_freq_slider.value()
        min=self.min_freq_slider.value()
        fig = plot.figure()
        self.powerSpectrum, self.freqenciesFound, self.time, self.imageAxis = plot.specgram(self.signal.real, Fs=self.samplingrate,cmap=self.cmap)
        # plot.colorbar()
        # plot.ylim(min,max)
        plot.xlabel('Time')
        plot.ylabel('Frequency')
        fig.savefig('plot.png')
        plot.close()
        self.upload()
        # sf.write('sound.wav',self.signal.real, self.samplingrate)
        # wave_obj = sa.WaveObject.from_wave_file("sound.wav")
        # play_obj = wave_obj.play()

    def changefreq(self):
        max= self.max_freq_slider.value()
        min=self.min_freq_slider.value()
        if max> min:
            plot.close()
            fig = plot.figure()
            plot.subplot(111) 
            self.powerSpectrum, self.freqenciesFound, self.time, self.imageAxis = plot.specgram\
                (self.signal.real, Fs=self.samplingrate,cmap=self.cmap, vmin=min, vmax=max)
            
            plot.xlabel('Time')
            plot.ylabel('Frequency')
            # plot.colorbar()
            fig.savefig('plot.png')
            plot.close()
            self.upload()
        else:
            pass
  


app = QApplication(sys.argv)
sheet= WINDOW()
sheet.show()
sheet.setWindowTitle("Sigviewer")
sheet.setWindowIcon(QIcon("icon.png"))
sys.exit(app.exec_())

