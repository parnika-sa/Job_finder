# =============================================
# main.py - Job Alert System ka Main File
# Run: python main.py
# =============================================

import schedule
import time
from datetime import datetime
from job_fetcher import fetch_jobs
from email_sender import send_email
from config import ALERT_TIME


def run_job_alert():
    """
    Main function - jobs fetch karo aur email bhejo
    """
    print("\n" + "="*50)
    print(f"🚀 Job Alert Running: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    print("="*50)

    # Step 1: Jobs fetch karo
    jobs = fetch_jobs()

    # Step 2: Email bhejo
    if jobs:
        send_email(jobs)
    else:
        print("\n⚠️  Koi job nahi mili. Email nahi bheja.")

    print("\n✅ Done! Next alert kal aayega.")
    print("="*50)


def main():
    print("="*50)
    print("  🎯 Ankit ka Job Alert Bot - Started!")
    print(f"  ⏰ Daily alert time: {ALERT_TIME}")
    print("  📍 Locations: Mohali, Chandigarh, Zirakpur")
    print("="*50)

    # Abhi ek baar test run karo
    print("\n🔄 Pehli baar abhi chalate hain (test run)...")
    run_job_alert()

    # Daily schedule set karo
    print(f"\n⏰ Scheduler set: Roz {ALERT_TIME} baje alert aayega")
    schedule.every().day.at(ALERT_TIME).do(run_job_alert)

    # Keep running
    while True:
        schedule.run_pending()
        time.sleep(60)  # Har minute check karo


if __name__ == "__main__":
    main()
