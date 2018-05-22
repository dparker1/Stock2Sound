#Python Version 3.6.3

import json
import urllib3
import numpy as np
from scipy.io.wavfile import write

def normalize(nums):
	return np.int16(nums/np.max(np.abs(nums)) * (2 ** 15 - 1))

def repeat(nums, n):
	result = []
	for i in range(0, n):
		for j in nums:
			result += [j]
	
	return np.array(result)

def main():
	apiKey = ""
	with open("./Key.txt", "r") as keyFile:
		apiKey = keyFile.readline()

		

	caller = urllib3.PoolManager()
	url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=STRM&apikey=" + apiKey

	data = list(json.loads(caller.request("GET", url).data)['Time Series (Daily)'].values())
	vals = []
	for i in range(0, len(data)):
		vals.insert(0, float(data[i]['4. close']) - float(data[i]['1. open']))

	vals = normalize(np.array(vals))
	print(repeat(vals, 1000))
	write("./test.wav", 44100, repeat(vals, 1000))



main()