# Square detector for Facebook Hackercup 2014
# fb.com/gbrezende
# Guilherme Rezende <guilhermebr@gmail.com>

"""
Problem: Shape detector

Detectar diferentes formas geometricas
Detectar quadrados apenas na primeira versao
Input:
Teste Case
Numero da Matriz
Matriz

# = Black
. = White

numero de # deve ser NxN em paralelo.
"""
from math import sqrt

def is_sequential(black):
    n = len(black)

    for x in range(0,n):
        if x == n-1:
            break
        l,c = black[x]
        l2,c2 = black[x+1]
        if l == l2:
            if c+1 != c2:
                return False
        elif l+1 != l2:
            return False

    return True

def is_parallel(black):
    n = len(black)
    m = int(sqrt(n))

    for x in range(0,n):
        if x == n-m:
            break
        l,c = black[x]
        l2,c2 = black[x+m]
        if l+1 != l2:
            return False
        if c != c2:
            return False
    
    return True
     

def has_square(lines):
    black = []

    for x in range(0, lines):
        line = inFile.readline().strip('\n')
        for c in range(0, lines):
            if line[c] == '#':
                black.append((x, c))

    return black


#__main__
try:
    inFile = open('square_detector.txt', 'r')
    outFile = open('sd_output.txt', 'w+')

    numTests = inFile.readline()
    numTests = int(numTests.strip('\n'))


    for test in range(1, numTests+1):
        lines = int(inFile.readline().strip('\n'))

        black = has_square(lines) 
        if (sqrt(len(black)) * 10) % 10 == 0:
            if (sqrt(len(black))) == lines:
                result ='Case #%d: YES\n' % (test)

            else:
                if is_parallel(black) and is_sequential(black):
                    result = 'Case #%d: YES\n' % (test)
                else:
                    result = 'Case #%d: NO\n' % (test)


        else:
            result = 'Case #%d: NO\n' % (test)

        outFile.write(result)


finally:
    inFile.close()
    outFile.close()