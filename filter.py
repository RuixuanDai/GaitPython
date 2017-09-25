
def medianSmooth(x,wdsSize=4):
    firstFill = [ x[0] for t in range(wdsSize/2)]
    lastFill = [ x[-1] for t in range(wdsSize - wdsSize/2-1)]
##    print x
    newX = firstFill + x + lastFill
    y = list(x)
##    print newX
    for n in range(len(x)):
        wds = [ newX[t+n] for t in range(wdsSize) ]
        wds.sort()
        y[n] = wds[wdsSize/2]
    return y

def avrSmooth(x,wdsSize=4):
    firstFill = [ x[0] for t in range(wdsSize/2)]
    lastFill = [ x[-1] for t in range(wdsSize - wdsSize/2-1)]
##    print x
    newX = firstFill + x + lastFill
    y = list(x)
##    print newX
    for n in range(len(x)):
        wds = [ newX[t+n] for t in range(wdsSize) ]
        y[n] = sum(wds)/float(len(wds))
    return y

def zeroOffset(y):
    avr = sum(y)/float( len(y) ) 
    y = map(lambda x:x-avr, y)
#    print  sum(y)/float( len(y) )
    return y
