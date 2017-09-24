def zeroDetect(y,minSize = 0):
    #
    #  return step phase by detecting the zero point. if the interval is less than minSize,
    # then, ignore the zero point
    #
    numOfPhase = 0
    zeros = []
    for n in range(1,len(y)):
        if y[n] == 0 or y[n]*y[n-1]<0:
            print y[n],y[n-1]
            if  len(zeros) == 0:
                zeros.append(n)
            else:
                if (n - zeros[-1]) >= minSize:
                    zeros.append(n)
    print zeros
    return len(zeros)-1
    
