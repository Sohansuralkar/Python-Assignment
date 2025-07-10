import time
import schedule
import datetime

def display():
    t = datetime.datetime.now()
    fobj = open("Marvellous.txt","a")
    fobj.write(str(t)+"\n")
    fobj.close()

def main():
    schedule.every(5).minutes.do(display)
    while True:
        schedule.run_pending()
        time.sleep(1)

main()