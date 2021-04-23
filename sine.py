
import matplotlib.pyplot as plot
import numpy as np
from math import pi
import soundfile as sf

Fs = 8000
t= np.arange(0,1,1/Fs)

f= 100
y=  np.sin(2*pi*t)
for i in np.arange(10):
    y+=np.sin(2*pi*f*t)
    f+=300

# y=  np.sin(2*pi*190*t)+ np.sin(2*pi*1190*t)+ np.sin(2*pi*290*t)+\
#     np.sin(2*pi*390*t)+np.sin(2*pi*490*t)+ np.sin(2*pi*1590*t)+\
#     np.sin(2*pi*690*t)+ np.sin(2*pi*790*t)+ np.sin(2*pi*1890*t)+np.sin(2*pi*1990*t)

# plot.subplot(2,1,1)
# plot.plot(t,y)
# plot.show()
# print(y)
# sf.write('synthetic_file.wav', y, Fs)