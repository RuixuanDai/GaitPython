def zeroDetect(y,minSize = 0):
    #
    #  return step phase and zeros position by detecting the zero point. if the interval is less than minSize,
    # then, ignore the zero point
    #
    zeros = []
    for n in range(1,len(y)):
        if y[n] == 0 or y[n]*y[n-1]<0:
#            print y[n],y[n-1]
            if  len(zeros) == 0:
                zeros.append(n)
            else:
                if (n - zeros[-1]) >= minSize:
                    zeros.append(n)
#    print zeros
    return len(zeros)-1 , zeros


def peakDetect(y,zeros):
    #
    #  return peaks accouding to the zeros position 
    #
    peakPos = []
    peaks = []
    avr = sum(y)/float(len(y))
    for n in range(1,len(zeros)): # start from 1
        temp = y[zeros[n-1]:zeros[n]]
        maximum = max(temp)
        minimum = min(temp)
        if abs(maximum-avr)>abs(minimum-avr):  # it is a peak
            peaks.append(temp.index(maximum)+zeros[n-1])
            peakPos.append(maximum)
        else:
            peaks.append(temp.index(minimum)+zeros[n-1])
            peakPos.append(minimum)
    return peakPos,peaks
    
