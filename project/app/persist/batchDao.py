
from project.app.persist.baseDao import getSession
from project.app.models.batch import BatchJob


def getBatchJobById(id, session=None):

    if(session == None):
        session = getSession()

    configItem = session.query(BatchJob).filter(BatchJob.id == id).first()
    return configItem