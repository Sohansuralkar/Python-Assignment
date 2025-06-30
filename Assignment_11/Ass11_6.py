no = 5
sum = 0
def natural_sum_addition():
    global sum
    global no
    if no >= 1:
        sum = sum + no
        no = no - 1
        natural_sum_addition()

natural_sum_addition()
print(sum)