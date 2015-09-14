import csv

ct = 0

with open('iowa-liquor-sample.csv','rb') as infile:
	r = csv.reader(infile)
	for row in r:
		if "single malt scotch".upper() in ("".join(row).upper()):
			ct = ct + 1

print ct
