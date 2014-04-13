def checkSom(som):
    if som == 4 or som == 12:
        return (1, 'X won')

    if som == 28 or som == 30:
        return (2, 'O won')

    return (0, 'None')

def checkGame(matriz):
    #first check lines
    for i in matriz:
        som = 0
        for j in i:
            som += int(j)
        print som

        is_win = checkSom(som)
        if is_win[0]:
            return is_win

    #second check coluns
   # for i in matriz:
   #     for j in i:

    for i in range(4):
        som = 0
        for j in range(4):
          som += int(matriz[j][i])
        print som
        
        is_win = checkSom(som)
        if is_win[0]:
            return is_win

    #check diagonals
    som = int(matriz[0][0]) + int(matriz[1][1]) + int(matriz[2][2]) + int(matriz[3][3])
    print som
    is_win = checkSom(som)
    if is_win[0]:
        return is_win
    
    #check diagonal inverse
    som = int(matriz[0][3]) + int(matriz[1][2]) + int(matriz[2][1]) + int(matriz[3][0])
    print som
    is_win = checkSom(som)
    if is_win[0]:
        return is_win



    for i in matriz:
        if '0' in i:
            return (3, 'Game has not completed')
    
    return (4, 'Draw')



#__main__
try:
    inFile = open('input.txt', 'r')
    outFile = open('output.txt', 'w+')

    test_cases = inFile.readline()
    #cases = inFile.readlines()

    test_cases = int(test_cases.strip('\n'))

    for test in range(1, test_cases+1):
        matriz = []
        n = 4

        for i in range(n):
            line = inFile.readline().strip('\n')
            #line = line.strip('\n')

            #line = cases.pop(0).strip('\n')
            line = line.replace('X', '1').replace('O', '7').replace('T', '9').replace('.', '0')
            line = list(line)

            matriz.append(line[:])

        print matriz
        result, text = checkGame(matriz)
        print 'Winner: %s' % result


        print 'Case #%d: %s' % (test, text)
        outFile.write('Case #%d: %s\n' % (test, text))

        #to remove \n
        line = inFile.readline()
        #cases.pop(0)
    
finally:
    inFile.close()
    outFile.close()