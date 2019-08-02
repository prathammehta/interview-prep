# https://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-twice/

def findBestSale(prices, start, end):
	bestSale = 0
	for i in range(start, end):
		for j in range(i + 1, end + 1):
			sale = prices[j] - prices[i]
			if sale > bestSale:
				bestSale = sale

	return bestSale



def findBestPairOfSales(prices):
	maximumProfit = 0
	for index in range(1,len(prices) - 1):
		profit = 0
		if index == 1:
			profit = findBestSale(prices,0, len(prices) - 1)
		else:
			profit = findBestSale(prices,0,len(prices) - index - 1) + findBestSale(prices, len(prices) - index, len(prices) - 1)


		if profit > maximumProfit:
			maximumProfit = profit

	return maximumProfit


print(findBestPairOfSales([100, 30, 15, 10, 8, 25, 80]))

