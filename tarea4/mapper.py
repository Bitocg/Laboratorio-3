#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data)!=6:
	pass;
    else:
    	date, time, store, item, cost, payment = data
    	print(payment+"\t"+cost)
