
from datetime import datetime
from app.models.batch import BatchJob
from app.persist import groupDao, batchDao


def run_stats():
    start_ts = datetime.now()

    user_count = groupDao.get_group_count()
    print("stats: group_count=" + str(user_count))

    end_ts = datetime.now()

    batch_job = BatchJob()
    batch_job.start_ts = start_ts
    batch_job.job_code = 'STATS'
    batch_job.details = "stats: group_count=" + str(user_count)
    batch_job.status_code = 'COMPLETED'
    batch_job.end_ts = end_ts

    batchDao.add_batch_job(batch_job)



# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).days.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
