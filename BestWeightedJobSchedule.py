# https://www.geeksforgeeks.org/weighted-job-scheduling/

def findBestJobSchedule(available_jobs, profit, current_time, start):
	print(available_jobs)
	if start == len(available_jobs):
		return profit
	else:
		current_job = available_jobs[start]
		max_profit = 0
		if current_time <= current_job[0]:
			max_profit = findBestJobSchedule(
							available_jobs, 
							profit + current_job[2], 
							current_time + current_job[1], 
							start + 1)

		max_profit = max(findBestJobSchedule(
							available_jobs, 
							profit, 
							current_time, 
							start + 1), max_profit)

		return max_profit


#Bottom up DP Solution

def findBestJobScheduleNonRecursive(jobs, n):
	best_profits = [0]*n
	time_ended = [0]*n
	time_ended[0] = jobs[0][1]
	best_profits[0] = jobs[0][2]

	for index in range(1,len(jobs)):
		max_profit = 0
		end_time = 0
		
		for sub_index in range(0,index):
			
			
			if time_ended[sub_index] <= jobs[index][0]:
				profit = best_profits[sub_index] + jobs[index][2]
				if profit > max_profit:
					max_profit = profit
					end_time = jobs[index][1]

		if max_profit == 0:
			if best_profits[index-1] < jobs[index][2]:
				time_ended[index] = jobs[index][1]
				best_profits[index] = jobs[index][2]
			else:
				time_ended[index] = time_ended[index - 1]
				best_profits[index] = max_profit[index - 1]
		else:
			time_ended[index] = end_time
			best_profits[index] = max_profit

		pass

	print(best_profits)
	print(time_ended)

findBestJobScheduleNonRecursive([
	[1, 2, 50],
	[3, 5, 20],
	[6, 19, 100],
	[2, 100, 200]
], 4)