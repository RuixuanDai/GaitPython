
def medianSmooth(x,wdsSize=4):
    firstFill = [ x[0] for t in range(wdsSize/2)]
    lastFill = [ x[-1] for t in range(wdsSize - wdsSize/2-1)]
##    print x
    newX = firstFill + x + lastFill
##    print newX
    for n in range(len(x)):
        wds = [ newX[t] for t in range(wdsSize) ]
        wds.sort()
        x[n] = wds[wdsSize/2]
    return x
