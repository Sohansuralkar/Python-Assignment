mull = 1
no = 5
def factorial():
    global no
    global mull
    if no >= 1:
        mull = mull * no
        no = no - 1
        factorial()

factorial()
print(mull)