
# Google Code Jam 2014
# Magic Trick
# Guilherme Rezende <guilhermebr@gmail.com>
# guilhermebr.com

import sys

def get_cards():
	col = int(raw_input())
	for x in range(1, 5):
		if x == col:
			cards = map(int, raw_input().strip().split())
		else:
			raw_input()

	return set(cards)

def main():
	T = int(raw_input())

	for x in range(1, T+1):
		c1 = get_cards()
		c2 = get_cards()
		if len(c1.intersection(c2)) > 1 :
			print('Case #%d: Bad magician!' % x)
		elif len(c1.intersection(c2)) == 0:
			print('Case #%d: Volunteer cheated!' % x)

		else:
			card = c1.intersection(c2).pop()
			print('Case #%d: %d' % (x, card))

if __name__ == '__main__':
	main()