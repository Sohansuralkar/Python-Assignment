counter = 1
def primenumber():
    
    global counter
    if (counter<=5):
        print(counter)
        counter = counter + 1
        primenumber()

primenumber()