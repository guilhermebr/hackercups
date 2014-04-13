# Google Code Jam 2014
# Cookie Clicker
# Guilherme Rezende <guilhermebr@gmail.com>
# guilhermebr.com

import sys

def calc(c, x, f, tick, t):
    p = int(x / c)
    time = 0
    last_time = time + (x / tick)

    while 1:
        time += c / tick
        tick += f
        timef = time + (x / tick)
        if timef > last_time:
            break
        last_time = timef 

    print('Case #%d: %.7f' % (t, last_time))

def main():
    T = int(raw_input())

    for t in range(1, T+1):
        tick = 2.0
        c, f, x = map(float, raw_input().strip().split())
        calc(c, x, f, tick, t)


if __name__ == '__main__':
    main()