# https://www.geeksforgeeks.org/cutting-a-rod-dp-13/
INT_MIN = -32767

# Non DP recursive
def getCutRodConfiguration(currentLength, currentPrice, lengths, costs):
	if currentLength == 0:
		return currentPrice
	else:
		availableAmounts = []
		for i in range(0,len(costs)):
			if currentLength >= lengths[i]:
				availableAmounts.append(getCutRodConfiguration(currentLength - lengths[i], currentPrice + costs[i], lengths, costs))
		return max(availableAmounts)

# print(getCutRodConfiguration(8, 0, [1, 2, 3, 4, 5, 6, 7, 8],[3, 5, 8, 9, 10, 17, 17, 20]))


# Bottom UP

def getCutRodConfigurationBU(length, costs):
	maxCosts = [0 for i in range(length + 1)]
	maxCosts[0] = 0
	for i in range(1,length + 1):
		print(maxCosts)
		maxVal = INT_MIN
		for j in range(i):
			maxVal = max(maxVal, costs[j] + maxCosts[i-j-1])
		maxCosts[i] = maxVal

	print(maxCosts)


getCutRodConfigurationBU(8,[3, 5, 8, 9, 10, 17, 17, 20])


