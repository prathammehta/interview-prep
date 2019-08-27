def stores_and_houses(houses, stores):
	stores.sort()
	sol = []

	for house in houses:
		l = 0
		r = len(stores) - 1
		ans = None

		while True:
			m = (l+r)//2
			if stores[m] == house:
				ans = stores[m]
				break
			elif r - l <= 1 and stores[r] != house and stores[l] != house:
				break
			elif stores[m] < house:
				l = m
			else:
				r = m

		if ans is None:
			if abs(house - stores[l]) <= abs(house - stores[r]):
				ans = stores[l]
			else:
				ans = stores[r]

		sol.append(ans)

	return sol

print(stores_and_houses([5, 10, 17], [1, 5, 20, 11, 16]))