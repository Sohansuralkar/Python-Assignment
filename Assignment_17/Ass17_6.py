import time 
import schedule
import datetime

def lunch():
    print("Lunch Time..")

def wrap():
    print("Wrap up..")

def main():
    schedule.every().day.at("13:00").do(lunch)
    schedule.every().day.at("18:00").do(wrap)
    while True:
        schedule.run_pending()
        time.sleep(1)
main()