#!/usr/bin/python

import sys

Totalventas = {}

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
	# Something has gone wrong. Skip this line.
		continue
	total, thisSale = data_mapped
	if total not in Totalventas.keys():
		Totalventas[total] = float(thisSale)
	else:
		Totalventas[total] += float(thisSale)
  
for key, value in Totalventas.items():
	print(key+"\t"+str(value))
