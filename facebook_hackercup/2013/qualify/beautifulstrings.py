# Beautiful Strings for Facebook Hackercup
# fb.com/gbrezende
# Guilherme Rezende <guilhermebr@gmail.com>
#
import operator        

def letterCount(word):
    """
    Returns a dict of letter and the occurrence count in word.
    """
    letter_count = {}
    for letter in word:
        if letter.isalpha():
            if not letter_count.has_key(letter):
                letter_count[letter] = word.count(letter)
    return letter_count

def maxBeauty(word_dict):
    """
    Returns the maximum possible beauty of the string.
    """
    price = 26
    maximum = 0  
    for x, y in word_dict:
        maximum += y * price
        price -= 1
    return maximum

#__main__
try:
    inFile = open('input.txt', 'r')
    outFile = open('output.txt', 'w+')

    numLines = inFile.readline()
    words = inFile.readlines()

    numLines = int(numLines.strip('\n'))

    line = 1
    while line <= numLines:
        word = words[line-1] 
        #print len(word) 

        letter_dict = letterCount(word.lower())
        letter_dict = sorted(letter_dict.iteritems(), key=operator.itemgetter(1))
        letter_dict.reverse()
        maximum = maxBeauty(letter_dict)
        print 'Case #%d: %d' % (line, maximum)
        outFile.write('Case #%d: %d\n' % (line, maximum))
        line += 1
finally:
    inFile.close()
    outFile.close()







