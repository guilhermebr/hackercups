# Google Code Jam 2014
# 1 A
# Charging Chaos
# Guilherme Rezende <guilhermebr@gmail.com>
# guilhermebr.com

import sys

def switch(of, l):
    for a in range(0, len(of)):
        of[a][l] = 1 ^ of[a][l]


def main():
    T = int(raw_input())
    #T = 1

    for t in range(1, T+1):
        N, L = map(int, raw_input().strip().split())
        of = [ list([int(a) for a in x]) for x in map(str, raw_input().strip().split()) ]
        df = [ list([int(a) for a in x]) for x in map(str, raw_input().strip().split()) ]
        #print of, df
        
        of.sort()
        df.sort()

        ok = 0
        sw = 0
        for l in range(0, L):
            nof = [ of[x][l] for x in range(0, N) ]
            ndf = [ df[x][l] for x in range(0, N) ]

            #print nof, ndf
            nof.sort()
            ndf.sort()
            if nof != ndf:
                switch(of, l)
                    
                of.sort()
                df.sort()
                sw += 1

                
             #   print of
             #   print df
           

            if of == df:
                ok = 1
                break 

        if ok:
            print('Case #%d: %d' % (t, sw))
        else:
            print('Case #%d: NOT POSSIBLE' % t)


if __name__ == '__main__':
    main()