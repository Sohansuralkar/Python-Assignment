import os 
import sys
import hashlib


class chechsum:
    def __init__(self):
        lobj = open("logfile.txt","w")

    def calculatechecksum(self,filename):
        algo = hashlib.md5()
        fobj = open(filename,"rb")
        buffer = fobj.read(1000)
        while len(buffer) > 0 :
            algo.update(buffer)
            buffer = fobj.read(1000)
        return algo.hexdigest()
    
    def main(self):
        dir = sys.argv[1]
        if not os.path.isabs(dir):
            dir = os.path.abspath(dir)
        dir = dir.split("\\")[0:-1]
        dir = "\\".join(dir)

        if not os.path.exists(dir) and not os.path.isdir(dir):
            print("invalid pathh")


        chk = None

        for folder, sf,files in os.walk(dir):
            for file in files:
                filename = os.path.join(folder,file)
                chk = self.calculatechecksum(filename)
                print("filename : ",file)
                print("check sum : ",chk)

if __name__ == "__main__":
    obj = chechsum()
    obj.main()