
from project.app.persist import baseDao
from project.app.models.batch import BatchJob


def get_batch_job_by_id(batch_id, session=None):

    if session is None:
        session = baseDao.get_session()

    item = session.query(BatchJob).filter(BatchJob.id == batch_id).first()
    return item
