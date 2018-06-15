#!/usr/bin/env python

import sys
import re


if __name__ == "__main__":
    monthdict={'jan':'01','feb':'02','mar':'03','apr':'04', 'may':'05', 'jun':'06', \
        'jul':'07', 'aug':'08', 'sep':'09','oct':'10','nov':'11','dec':'12'}
    yearlist=['2012','2013']
    monthlist=['jan','feb','mar','apr', 'may', 'jun','jul','aug','sep','oct','nov','dec']
    for line in sys.stdin:
        yearbag =re.compile(r'[0-9]{4,4}').findall(line)
        for i in range(0,len(yearbag)):
            if yearbag[i] in yearlist:    
                break
        year=yearbag[i]
        month_medium = re.compile(r'[a-z]{3,3}').findall(line.lower())
        for i in range(0,len(month_medium)):
            if month_medium[i] in monthlist:
                break
        month=monthdict[month_medium[i]]
        word = year+'-'+month
        sys.stdout.write("{}\t1\n".format(word))



