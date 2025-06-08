from apscheduler.schedulers.background import BackgroundScheduler
import atexit

def scheduled_update():
    print("Running scheduled job update...")
    dashboard.update_data()
    print(f"Update completed at {datetime.now()}")

# Set up scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(func=scheduled_update, trigger="interval", hours=6)
scheduler.start()

# Shut down scheduler when exiting app
atexit.register(lambda: scheduler.shutdown())