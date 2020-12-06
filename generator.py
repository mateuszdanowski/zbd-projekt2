import csv
import sys
from datetime import datetime, timedelta, date
import random
import string
import numpy as np
from math import log, ceil
from itertools import product

DATE_FROM = date(2020, 1, 1)
DAYS = 10000
CATEGORIES = 100
VALUES = 5000
MEAN = 0
DEVIATION = 10

ALPHABET = list(string.ascii_uppercase)

def write_csv(days=DAYS, categories=CATEGORIES, values=VALUES, type="", value=""):
	DAYS = days
	CATEGORIES = categories
	VALUES = values
	category_len = ceil(log(CATEGORIES, 26)) if CATEGORIES != 1 else 1
	categories = [ALPHABET for _ in range(category_len)]
	categories_tuples = list(product(*categories))
	final_categories = list(map(lambda w: ''.join(w), categories_tuples[:CATEGORIES]))
	# print(final_categories)

	np.random.seed()

	csv_name = 'data/{}-{}.csv'.format(type, value)
	
	with open(csv_name, 'w', newline='') as file:
		writer = csv.writer(file)
		
		header_row = ['date', 'category']
		
		for i in range(VALUES):
			header_row.append('value' + str(i + 1))
			
		# writer.writerow(header_row)
		
		
		values = np.random.normal(loc=MEAN, scale=DEVIATION, size=(DAYS, VALUES)) 
		
		date = DATE_FROM
		index = 0
		
		while index < DAYS:
			str_date = "{}".format(date)
			category = "{}".format(random.choice(final_categories))
			row = [str_date, category]
			for i in range(VALUES):
				row.append(int(values[index][i]))
			
			writer.writerow(row)
			date += timedelta(days=1)
			index += 1
	
if __name__ == "__main__":
	for i in range(1, len(sys.argv)):
		split_equal = sys.argv[i].split('=')
		if len(split_equal) != 2:
			continue
		
		name = split_equal[0]
		value = int(split_equal[1])
		
		if name == "days":
			DAYS = value
		elif name == "categories":
			CATEGORIES = value
		elif name == "values":
			VALUES = value
		elif name == "mean":
			MEAN = value	
		elif name == "deviation":
			DEVIATION = value
		else: 
			continue
			
	write_csv()
