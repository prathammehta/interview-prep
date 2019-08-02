# https://www.geeksforgeeks.org/coin-change-dp-7/

def coin_change(amount, coins, coin_limit):
	if amount == 0:
		return 1
	if amount <= 0:
		return 0
	if coin_limit < 0:
		return 0
	else:
		return coin_change(amount, coins, coin_limit - 1) + coin_change(amount - coins[coin_limit], coins, coin_limit)


def coin_change_bu(amount, coins):
	combinations = [[0 for _ in range(amount + 1)] for _ in range(len(coins))]

	for i in range(len(coins)):
		combinations[i][0] = 1
		pass

	for i in range(len(coins)):
		for j in range(1,amount + 1):
			x = combinations[i-1][j] if i > 0 else 0
			y = combinations[i][j - coins[i]] if j-coins[i] >= 0 else 0
			combinations[i][j] = x + y


	return combinations

print(coin_change_bu(4, [1,2,3]))