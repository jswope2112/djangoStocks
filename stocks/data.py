import requests
import json
import numpy as np
from datetime import date
import sys

#Allow the stock called to be based upon an input and retrieve the data if that stock is valid
#Error if nothing is entered and exit the program
def get_graph(ticker):
	try:
		SMA200 = 'http://www.alphavantage.co/query?function=SMA&symbol=' + ticker +'&interval=daily&time_period=200&series_type=open&apikey=9S5OS48JQM20W5U9'
		cost = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + ticker + '&outputsize=full&interval=60min&apikey=9S5OS48JQM20W5U9'
		first_data = requests.get(SMA200)
		second_data = requests.get(cost)
	except BaseException:
		exit()

	data = first_data.json()
	days = []
	SMA = []

	#Get all of the SMA values from the data pulled and throw an exception and exit the program if an invalid stock was entered
	try:
		for k, v in data["Technical Analysis: SMA"].items():
			year = int(k[:4])
			month = int(k[5:7])
			day = int(k[8:10])
			SMA.append(v["SMA"])
			days.append(str(date(year,month,day)))
	except BaseException:
		exit()
	#get data for the price averages at opening
	data1 = second_data.json()
	prices = []
	days1 = []
	for d, p in data1['Time Series (Daily)'].items():
		prices.append(p['1. open'])
		year = int(d[:4])
		month = int(d[5:7])
		day = int(d[8:10])
		days1.append(str(date(year,month,day)))

	#shorten days1 and prices so that all data is the same length for the graph 
	days1 = days1[:500]
	prices = prices[:500]
	days = days[:500]
	SMA = SMA[:500]
	#Make data into a dictionary and return it
	info = {'price_day': days1[::-1], 'price': prices[::-1], 'sma_day': days[::-1], 'SMA': SMA[::-1], 'ticker-symbol': ticker}
	return info
