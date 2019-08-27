def evaluate(nums):
    if len(nums) == 0:
        return []
    elif len(nums) == 1:
        return [nums[0]]
    elif len(nums) == 2:
        return [nums[0] + nums[1], nums[0] - nums[1], nums[0] * nums[1], nums[0] / nums[1]]
    else:
        final_result = []
        for i in range(len(nums)-1):
            el1 = nums[i]
            el2 = nums[i+1]
            comps = [el1 + el2, el1 - el2, el1 * el2, el1 / el2]
            left = evaluate(nums[0:i])
            right = evaluate(nums[i+2:len(nums)])
            first_combs = []
            if len(left) > 0:
                for j in left:
                    for comp in comps:
                        first_combs.append(j+comp)
                        first_combs.append(j-comp)
                        first_combs.append(j*comp)
                        if comp != 0:
                            first_combs.append(j/comp)
            else:
                first_combs = comps


            second_combs = []
            if len(right) > 0:
                for j in right:
                    for comp in comps:
                        second_combs.append(comp + j)
                        second_combs.append(comp - j)
                        second_combs.append(comp * j)
                        if j != 0:
                            second_combs.append(comp / j)
            else:
                second_combs = comps

            # print(comps, left, right, first_combs, second_combs)
            for first in first_combs:
                for j in right:
                    final_result.append(first + j)
                    final_result.append(first - j)
                    final_result.append(first * j)
                    if j != 0:
                        final_result.append(first / j)

            for second in second_combs:
                for j in left:
                    final_result.append(j + second)
                    final_result.append(j - second)
                    final_result.append(j * second)
                    if second != 0:
                        final_result.append(j / second)

        return final_result 



print(len(evaluate([4,2,3,1])))



