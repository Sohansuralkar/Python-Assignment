no = 2
power = 3
mul  = 1

def powerX():
    global power
    global mul
    if power >= 1:

        mul = mul * no
        power = power - 1
        powerX()

powerX()
print(mul)