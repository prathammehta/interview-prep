n = int(input()) 

inputs = []

for _ in range(n):
    inputs.append(int(input()))

for root_index in range(n):
    number = inputs[root_index]
    digits = [int(d) for d in str(number)]
    building_number = ''
    processed = False
    for index in range(len(digits) - 1):
        if digits[index] % 2 == 1:
            if digits[index] == 9:
                final_number = int(building_number + str(digits[index] - 1) + ''.join('8' for _ in range(index, len(digits)-1)))
                print('Case #' + str(root_index + 1) + ': ' + str(abs(final_number - number)))
                processed = True
                break
            else:
                final_number1 = int(building_number + str(digits[index] - 1) + ''.join('8' for _ in range(index, len(digits)- 1)))
                final_number2 = int(building_number + str(digits[index] + 1) + ''.join('0' for _ in range(index, len(digits)-1)))
                final_number = min(abs(number - final_number1), abs(number - final_number2))
                print('Case #' + str(root_index + 1) + ': ' + str(final_number))
                processed = True
                break
        else:
            building_number += str(digits[index])

    if processed == False:
        if digits[-1] % 2 == 1:
            print('Case #' + str(root_index + 1) + ': 1')
        else:
            print('Case #' + str(root_index + 1) + ': 0')