import os 
import sys
import shutil

class CopyFiles:
    def __init__(self):
        self.fobj = open("logfile.txt","w")

    def copyfiles(self,dirname1,dirname2,ex):
        if not os.path.isabs(dirname1):
            dirname1 = os.path.abspath(dirname1)

        if not os.path.exists(dirname1) and not os.path.isdir(dirname1):
            print("Invalid path, please provide a correct path")

        if not os.path.exists(dirname1):
            os.mkdir(dirname2)

        if not os.path.isabs(dirname2):
            dirname2 = os.path.abspath(dirname2)

        for folder, subfolders, files in os.walk(dirname1):
            for file in files:
                if file.endswith(ex):
                    filename = os.path.join(folder,file)
                    dfilename = filename.replace(dirname1,dirname2)
                    shutil.copy(filename,dfilename)
                    self.fobj.write("file copied : " +filename + "to the file"+dirname2+"directory.\n")


    def main(self):
        dirname1 = sys.argv[1]
        dirname2 = sys.argv[2]
        ex = sys.argv[3]
        self.copyfiles(dirname1,dirname2,ex)


if __name__ == "__main__":
    obj = CopyFiles()
    obj.main()
