file = input("enter the file name ...")
fobj = open(file,"r")
content = fobj.read()
print(content)