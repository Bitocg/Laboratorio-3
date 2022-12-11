#!/usr/bin/python

import sys

for line in sys.stdin:
    try:
        data = line.strip().split("\t")
        date, time, store, item, cost, payment = data
        print("Total"+"\t"+cost)
    except ValueError:
	pass
