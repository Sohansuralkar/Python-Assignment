file = input("please enter a file name ..")
string = input("please enter a string you want to find in the file : ")

fobj = open(file,"r").read()

res = fobj.count(string)
print(res)