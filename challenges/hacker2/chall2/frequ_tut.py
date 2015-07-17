
#https://sites.google.com/site/haskell102/home/frequency-analysis-of-audio-file-with-python-numpy-scipy
import pylab
from pylab import plot, show, title, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft
from numpy import sin, linspace, pi, average
from scipy.io.wavfile import read,write
import wave
import struct
import pygame
import sys
import math

def plotSpectru(y,Fs):
    n = len(y) # lungime semnal
    k = arange(n)
    T = n/Fs
    frq = k/T # two sides frequency range
    frq = frq[range(n/2)] # one side frequency range

    Y = fft(y)/n # fft computing and normalization
    Y = Y[range(n/2)]
    
    
    plot(frq,abs(Y),'r') # plotting the spectrum
    xlabel('Freq (Hz)')
    ylabel('|Y(freq)|')
    

Fs = 44100;  # sampling rate
shrink = Fs #shrink y data by 1000 or more

rate,data=read('moonlight.wav')
y=data
lungime=len(y)
timp=len(y)/Fs
t=linspace(0,timp,len(y))

#print min(y), max(y), average(y)
"""
#do some max,min,av of amplitude
print len(y[::shrink])
avArray = []
for amp in y[::shrink]:
    for x in t[::shrink]:
        if amp >0:
            avArray.append([x,amp])

print max(avArray)
print min(avArray)
print average(avArray)
"""        
        
#print y,t
subplot(2,1,1)
plot(t[::shrink],y[::shrink]) #abs(y) only plots the positive numbers (amplitude)
xlabel('Time')
ylabel('Amplitude')
subplot(2,1,2)
plotSpectru(y,Fs)
show()





"""
#http://glowingpython.blogspot.ro/2011/08/how-to-plot-frequency-spectrum-with.html
from numpy import sin, linspace, pi
from pylab import plot, show, title, xlabel, ylabel, subplot
from scipy import fft, arange

def plotSpectrum(y,Fs):
 #Plots a Single-Sided Amplitude Spectrum of y(t)
 n = len(y) # length of the signal
 k = arange(n)
 T = n/Fs
 frq = k/T # two sides frequency range
 frq = frq[range(n/2)] # one side frequency range

 Y = fft(y)/n # fft computing and normalization
 Y = Y[range(n/2)]
 print frq,abs(Y)
 plot(frq,abs(Y),'r') # plotting the spectrum
 xlabel('Freq (Hz)')
 ylabel('|Y(freq)|')

Fs = 150.0;  # sampling rate
Ts = 1.0/Fs; # sampling interval
t = arange(0,1,Ts) # time vector

ff = 5;   # frequency of the signal
y = sin(2*pi*ff*t)

subplot(2,1,1)
plot(t,y)
xlabel('Time')
ylabel('Amplitude')
subplot(2,1,2)
plotSpectrum(y,Fs)
show()
"""




"""
#!/usr/bin/env python
#
# Youcope Emulator
#
#(c)2007 Felipe Sanches <juca@members.fsf.org>
#(c)2007 Leandro Lameiro <lameiro@gmail.com>
#licensed under GNU GPL v3 or later
#https://code.google.com/p/felipesanches/source/browse/trunk/youscope-emu/youscope-emu.py
import wave
import struct
import pygame
import sys
import math

SIZE = (800,400)#(1.5*640,1.5*480)
DOTCOLOR  = (0,255,0)
GRIDCOLOR  = (40,40,0)
BGCOLOR = (0,0,0) #branco
FPS = 24
PERSISTENCE = 0.60

#get the wave file and play it
wro = wave.open('moonlight.wav')
READ_LENGTH = wro.getframerate()/FPS

#continue with original
pygame.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('YouScope XY-Demo Osciloscope Emulator')
pygame.mouse.set_visible(0)

clock = pygame.time.Clock()

grid = pygame.Surface(SIZE)
grid = grid.convert_alpha()
grid.set_alpha(128)
grid.fill(BGCOLOR)

for x in range(10):
    pygame.draw.line(grid, GRIDCOLOR, (x*SIZE[0]/10,0), (x*SIZE[0]/10,SIZE[0]))

for y in range(8):
    pygame.draw.line(grid, GRIDCOLOR, (0 , y*SIZE[1]/8), (SIZE[0] , y*SIZE[1]/8))

pygame.draw.line(grid, GRIDCOLOR, (SIZE[0]/2,0), (SIZE[0]/2,SIZE[0]), 3)
pygame.draw.line(grid, GRIDCOLOR, (0 , SIZE[1]/2), (SIZE[0] , SIZE[1]/2), 3)

for x in range(100):
    pygame.draw.line(grid, GRIDCOLOR, (x*SIZE[0]/100,SIZE[1]/2-3), (x*SIZE[0]/100,SIZE[1]/2+3))

for y in range(80):
    pygame.draw.line(grid, GRIDCOLOR, (SIZE[0]/2 - 3, y*SIZE[1]/80), (SIZE[0]/2 + 3, y*SIZE[1]/80))

surface = pygame.Surface(screen.get_size())

while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    frames = wro.readframes(READ_LENGTH)
    
    surface.fill(BGCOLOR)
    surface.blit(grid, grid.get_rect())
    
    for i in range(0,READ_LENGTH,4):
        r = struct.unpack('hh', frames[i:i+4])
        x = int(r[1]*SIZE[0]/65536) + SIZE[0]/2 
        b = int(-r[0]*SIZE[1]/65536) + SIZE[1]/2
        surface.set_at((x,b), DOTCOLOR)
    

    screen.blit(surface, surface.get_rect())
        
    pygame.display.flip()

"""


"""
import numpy
import pylab
from pylab import plot, show, title, xlabel, ylabel, subplot, savefig
from scipy import fft, arange, ifft
from numpy import sin, linspace, pi
from scipy.io.wavfile import read,write

beta = [2,4,16,32]


#this works with everthing above

pylab.figure()
for b in beta:
 w = numpy.kaiser(101,b) 
 pylab.plot(range(len(w)),w,label="beta = "+str(b))
pylab.xlabel('n')
pylab.ylabel('W_K')
pylab.legend()
pylab.show()
"""


#this uses random and smoothing

"""
def smooth(x,beta):
 #kaiser window smoothing
 window_len=11
 # extending the data at beginning and at the end
 # to apply the window at the borders
 s = numpy.r_[x[window_len-1:0:-1],x,x[-1:-window_len:-1]]
 w = numpy.kaiser(window_len,beta)
 y = numpy.convolve(w/w.sum(),s,mode='valid')
 return y[5:len(y)-5]

# random data generation
#y = numpy.random.random(100)*100 
#for i in range(100):
 #y[i]=y[i]+i**((150-i)/80.0) # modifies the trend

Fs = 44100;  # sampling rate

rate,data=read('melodie.wav')
y=data
lungime=len(y)
timp=len(y)/Fs
t=linspace(0,timp,len(y))


# smoothing the data
pylab.figure(1)
pylab.plot(y,'-k',label="original signal",alpha=.3)
for b in beta:
    
    yy = smooth(abs(y),b) 
pylab.plot(yy,label="filtered (beta = "+str(b)+")")
pylab.legend()
pylab.show()
"""



