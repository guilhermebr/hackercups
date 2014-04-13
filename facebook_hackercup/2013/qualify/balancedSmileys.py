# Balanced Smileys for Facebook Hackercup
# fb.com/gbrezende
# Guilherme Rezende <guilhermebr@gmail.com>

def rule1(word):
    """
    rule: If an empty string
    """
    if word == '':
        return True
    return False

def rule2(word):
    """
    rule: One or more of the following characters: 'a' to 'z', ' ' (a space) or ':' (a colon)
    added to rule parenthesis chacacter.
    """
    for char in word:
        if not char.isalpha() and char != ' ' and char != ':' and char != '(' and char != ')':
            return False
    return True

def rule3(word):
    """
    rule: An open parenthesis '(', followed by a message with balanced parentheses, followed by a close parenthesis ')'
    """
    open_parenthesis = 0
    close_parenthesis = 0
    for char in word:
        if char == '(' and close_parenthesis <= open_parenthesis:
            open_parenthesis += 1
        elif char == ')':
            if open_parenthesis == 0:
                return False
            if  close_parenthesis > open_parenthesis:
                return False
            close_parenthesis += 1
    if open_parenthesis != close_parenthesis:
        return False
    return True

def rule4(word):
    """
    rule: A smiley face ":)" or a frowny face ":("
    """
    position = word.find(':')
    while position != -1:
        if word[position+1] in '()':
            word = word[:position] + word[position+2:]
        else:
            position +=1
        position = word.find(':', position)
    return word


def checkBalanced(word):
    """
    The logical to check all rules and return if is a balanced smiley or not.
    """
    if rule1(word):
        return True

    if rule2(word):
        if rule3(word):
            return True
        else:
            word = rule4(word)
            if rule3(word):
                return True
            else:
                return False
    return False

#__main__
try:
    inFile = open('balanced_smileystxt.txt', 'r')
    outFile = open('output2.txt', 'w+')

    numLines = inFile.readline()
    words = inFile.readlines()

    numLines = int(numLines.strip('\n'))
    line = 1
    while line <= numLines:
        word = words[line-1].strip('\n')
        if checkBalanced(word):
            outFile.write('Case #%d: YES\n' % (line))

        else:
            outFile.write('Case #%d: NO\n' % (line))

        line += 1

finally:
    inFile.close()
    outFile.close()














