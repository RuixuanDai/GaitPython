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
    peaks = []
    peakPos = []
    avr = sum(y)/float(len(y))
    temp = y[zeros[0]:zeros[1]]
    maximum = max(temp)
    minimum = min(temp)
    #find the first peak or valley. note: the first valley or peak may be not accurate
    if abs(maximum-avr)>abs(minimum-avr):  # it is a peak
        peakPos.append(temp.index(maximum)+zeros[0])
        peaks.append(maximum)
    else:
        peakPos.append(temp.index(minimum)+zeros[0])
        peaks.append(minimum)

    for n in range(2,len(zeros)): # start from 2
        temp = y[zeros[n-1]:zeros[n]]
        maximum = max(temp)
        minimum = min(temp)
        if abs(maximum-avr)>abs(minimum-avr):  # it is a peak
            peakPos.append(temp.index(maximum)+zeros[n-1])
            peaks.append(maximum)
        else: # find valley according to the last peak
            temp = y[peakPos[-1]:zeros[n]]
            minimum = min(temp)
            peakPos.append(temp.index(minimum)+peakPos[-1])
            peaks.append(minimum)
            
    return peaks,peakPos
    
