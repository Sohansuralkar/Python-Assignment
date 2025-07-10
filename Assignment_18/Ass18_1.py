import os 
file = input("Enter the file name you want to check ")
res = os.path.exists(file)
if res:
    print("file exist..")

else:
    print("File does not exixts...")

     