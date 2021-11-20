def partial_sums(*num):
    sum = 0
    sum_list = list(sum)
    for i in num:
        sum +=i
        sum_list.append(sum)
    return sum_list