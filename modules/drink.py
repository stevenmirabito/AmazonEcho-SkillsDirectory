"""
Drink module for Amazon Echo. A random drink that is in 
stock and costs 1 credit is chosen from Big Drink and dropped.

Computer Science House

Author: Jordan Rodgers (com6056@gmail.com)
"""

import json
import urllib
import urllib2
import random

def get_drinks(url, machine_id):
	available_drinks = []
	get_url = url + 'machines/stock&machine_id=2'
	req = urllib2.Request(get_url)
	response = urllib2.urlopen(req)
	stock = response.read()
	parsed_stock = json.loads(stock)
	parsed_data = parsed_stock['data']
	for drink in parsed_data['2']:
		if drink['available'] >= '1' and drink['item_price'] == '1':
			available_drinks.append([str(drink['item_name']), str(drink['slot_num'])])
	return available_drinks

def drop(url, ibutton, machine_id, available_drinks):
	drop_url = url + 'drops/drop'
	rand = random.randint(0, len(available_drinks) - 1)
	slot_num = available_drinks[rand][1]
	values = {'ibutton' : ibutton,
			  'machine_id' : machine_id,
			  'slot_num' : slot_num,
			  'delay'	: '0'}
	data = urllib.urlencode(values)
	req = urllib2.Request(drop_url, data)
	response = urllib2.urlopen(req).read()
	if json.loads(response)['status']:
		return available_drinks[rand][0] + ' has been dropped successfully.', True
	else:
		return 'Failed to drop drink.', True

def main():
	ibutton = ''
	machine_id = '2'
	base_url = 'https://webdrink.csh.rit.edu/api/index.php?request='
	available_drinks = get_drinks(base_url, machine_id)
	return drop(base_url, ibutton, machine_id, available_drinks)

if __name__ == '__main__':
    print main()
