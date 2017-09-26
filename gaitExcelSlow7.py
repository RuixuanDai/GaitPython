
import xlrd
import filter
import phaseDetect
import numpy as np

from matplotlib import style
import matplotlib.pyplot as plt

def open_excel(file='file.xls'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception, e:
        print str(e)

excel = open_excel('Book1.xlsx')


tableSlow7RX = excel.sheets()[1]


x = tableSlow7RX.col_values(0)
y1 = tableSlow7RX.col_values(1)
y2 = tableSlow7RX.col_values(2)
y3 = tableSlow7RX.col_values(3)

fs = 50 # sampling rate 10Hz
n = len(x) # num sample



y2Avr = filter.avrSmooth(y2,wdsSize=4)
y2MediaSmooth = filter.medianSmooth(y2,wdsSize=4)

y2 = filter.zeroOffset(y2)
y2Avr = filter.zeroOffset(y2Avr)
y2MediaSmooth = filter.zeroOffset(y2MediaSmooth)

print sum(y2Avr)/float(len(y2Avr))

num1,zeros1 = phaseDetect.zeroDetect(y2,3)
num2,zeros2 = phaseDetect.zeroDetect(y2Avr,3)

print 'Median:%d , Avr:%d'% (num1,num2)
# print zeros1
print zeros2

peaks1,position1 = phaseDetect.peakDetect(y2,zeros2)

print peaks1
print position1
# print [y2[n] for n in position1]
print 'zeros:%d,  peaks&valleys:%d' %(num2,len(peaks1))


zerosList = [ 0 for temp in zeros2]


# print zerosList
plt.subplot(211)
plt.scatter([xx/float(10) for xx in position1],peaks1,s=10,c='r')
plt.plot(x,y2)
plt.subplot(212)
plt.plot(x,y2Avr,color='red')
plt.scatter([xx/float(10) for xx in zeros2],zerosList,s=10,c='black')
plt.show()

        





