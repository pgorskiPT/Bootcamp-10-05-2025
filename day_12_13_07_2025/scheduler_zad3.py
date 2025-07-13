import logging
from logging.handlers import TimedRotatingFileHandler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR

# 1. Konfiguracja loggera z FileHandler i opcjonalnie StreamHandler
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# FileHandler: zapisuje logi do 'jobs.log', rotacja codziennie, zachowuje 7 plików
file_handler = TimedRotatingFileHandler(
    filename="jobs.log",
    when="midnight",
    interval=1,
    backupCount=7,
    encoding="utf-8"
)
file_handler.setFormatter(
    logging.Formatter("%(asctime)s %(levelname)s %(message)s")
)
logger.addHandler(file_handler)

# (opcjonalnie) StreamHandler, by dalej widzieć logi w konsoli
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(
    logging.Formatter("%(asctime)s %(levelname)s %(message)s")
)
logger.addHandler(stream_handler)

# 2. Definicja listenera APScheduler
def job_listener(event):
    job_id = event.job_id
    if event.exception:
        logger.error(f"❌ Job {job_id} zakończone błędem: {event.exception!r}")
    else:
        logger.info(f"✅ Job {job_id} wykonany pomyślnie")

# 3. Przykładowe zadanie
def my_job():
    # Twoja logika
    return "wynik"

# 4. Uruchomienie schedulera
scheduler = BackgroundScheduler()
scheduler.add_listener(
    job_listener,
    EVENT_JOB_EXECUTED | EVENT_JOB_ERROR
)
scheduler.add_job(my_job, 'interval', minutes=1, id="interval_job")
scheduler.start()

# 5. Blok utrzymujący proces przy życiu (demo)
import time
try:
    while True:
        time.sleep(5)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
