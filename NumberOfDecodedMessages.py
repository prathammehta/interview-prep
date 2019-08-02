# https://www.youtube.com/watch?v=qli-JCrSwuk

def get_number_of_possibilites(string):
	number_of_messages = 1
	if string[0] == 0:
		return 0
	for index in range(len(string)):
		if string[index] == '1' and index < len(string)-1 and string[index+1] != '0':
			number_of_messages += 1
		elif string[index] == '2' and index < len(string)-1 and string[index+1] <= '6' and string[index+1] != '0':
			number_of_messages += 1
		else:
			number_of_messages += 0

	return number_of_messages


print(get_number_of_possibilites('211'))