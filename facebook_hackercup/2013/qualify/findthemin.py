# Find the Min for Facebook Hackercup 2013
# fb.com/gbrezende
# Guilherme Rezende <guilhermebr@gmail.com>

def calcMatriz(n, k, a, b, c, r):
    m = []
    m.append(a)

    for i in range(1, k):
        m.append((b * m[i-1] +c) % r)

    return m


def getNelement(m, n, k):
    i = k
    minimum = 0

    while i < n:
        if minimum in m:
            minimum += 1
        else:
            m.append(minimum)
            m.remove(m[0])
            i += 1
            minimum = 0
    return m[k-1]

#__main__
try:
    inFile = open('find_the_mintxt.txt', 'r')
    outFile = open('output3.txt', 'w+')

    numTests = inFile.readline()
    numTests = int(numTests.strip('\n'))

    for test in range(1, numTests+1):
        n, k = (int(x) for x in inFile.readline().split())
        a, b, c, r = (int(x) for x in inFile.readline().split())

        m = calcMatriz(n, k, a, b, c, r)
        nth = getNelement(m, n, k)
       
        print 'Case #%d: %d' % (test, nth)
        outFile.write('Case #%d: %d\n' % (test, nth))


finally:
    inFile.close()
    outFile.close()















