# Tenisson for Facebook Hackercup 2014
# fb.com/gbrezende
# Guilherme Rezende <guilhermebr@gmail.com>

"""
Problem: Tenisson

L1: T
L2: K P(s) P(r) P(i) P(u) P(w) P(d) P(l) 

Ps = Probability to Win in Sun
Pr = Probability to Win in Rain
Pi = Probability to make Sun
P(Rain) = 1 - Pi 
Pu =
Pw =
Pd =
Pl =

Formula:

P(Round) = Ps * Pi + Pr * P(Rain)

"""

import itertools

#__main__
try:
    inFile = open('tennison_example_input.txt', 'r')
    #outFile = open('tenisson_example_output.txt', 'w+')

    numTests = inFile.readline()
    numTests = int(numTests.strip('\n'))


    for test in range(1, numTests+1):
        K,Ps,Pr,Pi,Pu,Pw,Pd,Pl = inFile.readline().split()
        print K,Ps,Pr,Pi,Pu,Pw,Pd,Pl
        Psol = float(Pi)
        #print Psol
        Pwin = 1
        result = 0

        for x in itertools.combinations(range(1,2*int(K)),int(K)):
            print x
            status = 1
            for game in range(1, 2*int(K)):
                print 'Game %d' % game
                tmp = float(Ps)*Psol+float(Pr)*(1-Psol)

                if status == 0:
                    Pwin *= 1 - tmp
                    print 1 - tmp

                else:
                    Pwin *= tmp
                    print tmp

                if game in x:
                    Psol = float(Pw)*(float(Psol)+float(Pu))
                    status = 1
                else:
                    Psol = float(Pl)*(float(Psol)-float(Pd))
                    status = 0
                
                print Pwin

                if game == x[-1]:
                    break
            
            result += Pwin
            print 'R: %f'% result
            Pwin = 1
            Psol = float(Pi)

        print 'Result %f' % result
       
        		



finally:
    inFile.close()
