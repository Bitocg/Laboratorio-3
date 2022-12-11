#!/usr/bin/python

import sys

pago_maximo = {}

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
	continue
    thisKey, thisSale = data_mapped

    if thisKey not in pago_maximo.keys():
        pago_maximo[thisKey] = thisSale
    elif float(pago_maximo[thisKey]) < float(thisSale):
        pago_maximo[thisKey] = thisSale

for llave, valor in pago_maximo.items():
    print(llave + "\t" + valor)
