
import xlrd
import filter

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





x=tableSlow7RX.col_values(0)
y1=tableSlow7RX.col_values(1)
y2=tableSlow7RX.col_values(2)
y3=tableSlow7RX.col_values(3)

fs = 10 # sampling rate 10Hz
n = len(x) # num sample

xfft = [ xx*(float(fs)/n) for xx in range(n/2)]

y1fft = fft(y1)[:n/2]
y2fft = fft(y2)[:n/2]
y3fft = fft(y3)[:n/2]



y3MediaSmooth = filter.medianSmooth(y3)





        
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




