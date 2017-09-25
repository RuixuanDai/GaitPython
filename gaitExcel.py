
import xlrd
import filter
import phaseDetect

import numpy as np
from scipy.fftpack import fft,ifft

from matplotlib import style
import matplotlib.pyplot as plt

def open_excel(file='file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception, e:
        print str(e)

excel = open_excel('Gait Data for Dingwen.xlsx')

tableNorm20 = excel.sheets()[0]

tableSlow7RX = excel.sheets()[1]

##
##row1 = tableNorm20.nrows
##col1 = tableNorm20.ncols
##
##print row1,col1





x = tableSlow7RX.col_values(0)
y1 = tableSlow7RX.col_values(1)
y2 = tableSlow7RX.col_values(2)
y3 = tableSlow7RX.col_values(3)

fs = 10 # sampling rate 10Hz
n = len(x) # num sample

xfft = [ xx*(float(fs)/n) for xx in range(n/2)]

y1fft = fft(y1)[:n/2]
y2fft = fft(y2)[:n/2]
y3fft = fft(y3)[:n/2]

y3ori = list(y3)
y3copy = list(y3)
# print y3
y3Avr = filter.avrSmooth(y3)
y3MediaSmooth = filter.medianSmooth(y3)
# print y3MediaSmooth
# print y3Avr
y3Avr = filter.zeroOffset(y3Avr)
y3MediaSmooth = filter.zeroOffset(y3MediaSmooth)

print sum(y3Avr)/float(len(y3Avr))

num1,zeros1 = phaseDetect.zeroDetect(y3MediaSmooth,5)
num2,zeros2 = phaseDetect.zeroDetect(y3Avr,5)

print 'Median:%d , Avr:%d'% (num1,num2)
print zeros1
print zeros2

peaks1,position1 = phaseDetect.peakDetect(y3,zeros1)

print peaks1
print position1
print [y3[n] for n in position1]



# plt.subplot(211)
# plt.plot(x,y3,color='r')
# plt.subplot(212)
# plt.plot(x,y3MediaSmooth,color='b')
# plt.plot(x,y3Avr,color='black')
# plt.plot(x,y3ori,color='r')
# # plt.plot(x,y3MediaSmooth,color='b')
# plt.show()



        
## plot for frequency
##plt.plot(xfft,y1fft)
##plt.plot(xfft,y2fft)
##plt.plot(xfft,abs(y3fft))
##plt.show()
##         


##plt.plot(x,y1)
##plt.plot(x,y2)
##plt.plot(x,y3,color='r')
##plt.show()




