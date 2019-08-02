# Coin Change | DP-7

# Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter.
# For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.


# Recursive Approach
def check_coin_change(coins, sum, target, added_value, map):
	key = str(sum) + '-' + str(added_value)
	if key in map:
		return map[key]
	if sum > target:
		return 0
	elif sum == target:
		return 1
	else:
		return_value = 0
		for index in range(coins.index(added_value),len(coins)):
			return_value += check_coin_change(coins, sum + coins[index], target, coins[index], map)
		map[key] = return_value
		return return_value


# Bottom Up Approach (Kinda Messed Up) - I copied this code
def check_coin_change_bu(coins,length, sum):
	map = [0 for k in range(sum+1)] 
	map[0] = 1

	for i in range(0,length):
		for j in range(coins[i], sum+1):
			map[j] = map[j] + map[j - coins[i]]

	return map


print(check_coin_change_bu([1,2,3], 3, 5))
