#!/usr/bin/env python3

from sys import argv

if len(argv)<2:
	print('usage: ' + argv[0] + ' DIVISOR')
	quit()

d = int(argv[1])
print('1', end=' ')
p = 1
l = [1]
while True:
	p = p*10%d
	print(p if p<=d/2 else p-d, end=' ')
	if p==0:
		print('')
		break
	if p in l or d-p in l:
		print('...')
		break
	l.append(p)
