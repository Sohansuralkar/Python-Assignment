import schedule
import time
def display():
    print("Jay Ganeshh..")

def main():
    schedule.every(2).seconds.do(display)
    while True:
        schedule.run_pending()
        time.sleep(1)

main()