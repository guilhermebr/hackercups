# basketball game for Facebook Hackercup 2014
# fb.com/gbrezende
# Guilherme Rezende <guilhermebr@gmail.com>

"""
Problem: Basketball Game

L1: T
L2: N M P
L[N]: Name Shot_Percent height
ex:
5
6 3 2
Wai 99 131
"""


def switch_player(playing, bench):
    for player in playing:
        player[3] += 1

    if len(bench) == 0:
        return

    sorted(playing, key=lambda x: (-x[3], x[1]))
    #sorted(bench, key=lambda x: (-x[3], x[1]), reverse=False)
    bench.sort(key=lambda x: (-x[3], x[1]), reverse=False)
    out_game = playing.pop()
    in_game = bench.pop()
    bench.insert(0, out_game)
    playing.insert(0, in_game)


#__main__
try:
    inFile = open('basketball_game.txt', 'r')
    outFile = open('basketball_game_output.txt', 'w+')

    numTests = inFile.readline()
    numTests = int(numTests.strip('\n'))


    for test in range(1, numTests+1):
        N,M,P = inFile.readline().split()
        players = []
        team1 = []
        team2 = []
        playing_t1 = []
        playing_t2 = []
        bench_t1 = []
        bench_t2 = []

        for line in range(0, int(N)):
            player,shot,height = inFile.readline().split()
            players.append([player,int(shot),int(height), 0])

        players = sorted(players, key=lambda player: (player[1], player[2]), reverse=True)
        #print players

        for player in range(0, len(players)):
            if player % 2 == 0:
                team1.append(players[player])
            else:
                team2.append(players[player])

        [playing_t1.append(team1[x]) for x in range(0, int(P))]
        [playing_t2.append(team2[x]) for x in range(0, int(P))]
        [bench_t1.append(team1[x]) for x in range(int(P), len(team1))]
        [bench_t2.append(team2[x]) for x in range(int(P), len(team2))]

        bench_t1.reverse()
        bench_t2.reverse()

        for time in range(1, int(M)+1):
            switch_player(playing_t1, bench_t1)
            switch_player(playing_t2, bench_t2)


        result = []
        [result.append(x[0]) for x in playing_t1]
        [result.append(x[0]) for x in playing_t2]

        to_print = 'Case #%d: %s\n' % (test, " ".join(sorted(result)))
        outFile.write(to_print)


finally:
    inFile.close()
    outFile.close()
