import sys
file1 = sys.argv[1]
file2 = "Demo.txt"

fobj = open(file1,"r")
f1content = fobj.read()
fobj.close()

fobj1 = open(file2,"w")
fobj1.write(f1content)
fobj1.close()
