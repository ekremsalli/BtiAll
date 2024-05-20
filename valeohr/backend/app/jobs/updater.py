from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from app.jobs.jobs import Syncing


def start():
    scheduler = BackgroundScheduler()

    scheduler.add_job(Syncing.sync_anomalies, 'interval', minutes=45)
    scheduler.add_job(Syncing.sync_employees, 'interval', days=1)
    scheduler.add_job(Syncing.sync_gecogroups, 'interval', days=1)
    scheduler.add_job(Syncing.sync_gecodefs, 'interval', days=1)
    scheduler.add_job(Syncing.sync_transaction, 'interval', minutes=45)

    # scheduler.add_job(Syncing.sync_anomalies, 'interval', minutes=1)
    # scheduler.add_job(Syncing.sync_employees, 'interval',  minutes=1)
    # scheduler.add_job(Syncing.sync_gecogroups, 'interval',  minutes=1)
    # scheduler.add_job(Syncing.sync_gecodefs, 'interval',  minutes=1)
    # scheduler.add_job(Syncing.sync_transaction, 'interval',  minutes=1)

    scheduler.start()
