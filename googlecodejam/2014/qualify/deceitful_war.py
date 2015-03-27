# Google Code Jam 2014
# Deceitful War
# Guilherme Rezende <guilhermebr@gmail.com>
# guilhermebr.com

import sys


def deceitful_war(n, naomi, ken):
    naomi.sort()
    ken.sort()
    np = kp = 0
    for game in range(1, n+1):
        nc = naomi[0]
        if nc > ken[0]
        for x in range(len(ken) -1, -1, -1):
            nt = ken[x] - 0.00001
            if nt not in ken:
                break
        print('nc: %f || nt: %f' % (nc, nt))

        if max(ken) > nt:
            kc = ken.pop()
        else:
            kc = ken.pop(0)  
        
        print('kc: %f' % kc)

        if nc > kc:
            np += 1
        
        print('np: %d' % np)
    return np

def war(n, naomi, ken):
    naomi.sort()
    ken.sort()
    np = kp = 0
    for game in range(1, n+1):
        nc = naomi.pop()
        
        if max(ken) > nc:
            kc = ken.pop()
        else:
            kc = ken.pop(0)  
        
        if nc > kc:
            np += 1

    return np

def main():
    T = int(raw_input())

    for t in range(1, T+1):
        n = int(raw_input())
        naomi = map(float, raw_input().strip().split())
        ken = map(float, raw_input().strip().split())

        n1 = deceitful_war(n, naomi[:], ken[:])
        n2 = war(n, naomi[:], ken[:])
        print('Case #%d: %d %d' % (t, n1, n2))

if __name__ == '__main__':
    main()