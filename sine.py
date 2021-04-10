
import matplotlib.pyplot as plot
from scipy.fftpack import rfft, rfftfreq
import numpy as np
from math import pi
import soundfile as sf
Fs = 2000
t= np.arange(0,1,1/Fs)
y=  np.sin(2*pi*90*t)+ np.sin(2*pi*190*t)+ np.sin(2*pi*290*t)+\
    np.sin(2*pi*390*t)+np.sin(2*pi*490*t)+ np.sin(2*pi*590*t)+\
    np.sin(2*pi*690*t)+ np.sin(2*pi*790*t)+ np.sin(2*pi*890*t)+np.sin(2*pi*990*t)

plot.subplot(2,1,1)
plot.plot(t,y)
# plot.show()
sf.write('synthetic_file.wav', y, Fs)