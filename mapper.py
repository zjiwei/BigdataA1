#!/usr/bin/env python

import sys
import re



if __name__ == "__main__":
	monthdict={'jan':'01','feb':'02','mar':'03','apr':'04', 'may':'05', 'jun':'06', \
		'jul':'07', 'aug':'08', 'sep':'09','oct':'10','nov':'11','dec':'12'}
	for line in sys.stdin:
		year = re.search(r'([0-9]){4,4}', line).group()
		month_medium = re.search(r'([a-z]){3,3}', line.lower()).group()
		month=monthdict[month_medium]
		word = year+'-'+month
		sys.stdout.write("{}\t1\n".format(word))

