import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR

# _levelToName = {
#     CRITICAL: 'CRITICAL',
#     ERROR: 'ERROR',
#     WARNING: 'WARNING',
#     INFO: 'INFO',
#     DEBUG: 'DEBUG',
#     NOTSET: 'NOTSET',
# }

# 1. Konfiguracja loggera
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

# 2. Definicja listenera
def job_listener(event):
    job_id = event.job_id
    if event.exception:
        logger.error(f"❌ Job {job_id} zakończone błędem: {event.exception!r}")
    else:
        logger.info(f"✅ Job {job_id} wykonany pomyślnie")

# 3. Przykładowe zadanie
def my_job():
    # tutaj Twoja logika
    return "wynik"

# 4. Uruchomienie schedulera
scheduler = BackgroundScheduler()
# podłączamy listener pod eventy zakończenia i błędu
scheduler.add_listener(job_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)

# 5. Dodajemy zadanie w interwale
scheduler.add_job(my_job, 'interval', minutes=1, id="interval_job")

scheduler.start()

# 6. Trzymaj proces przy życiu (tylko demo)
import time
try:
    while True:
        time.sleep(5)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
