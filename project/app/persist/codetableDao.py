
from project.app.persist.baseDao import getSession


def getCodeTable(codetable, session=None):

    if session == None:
        session = getSession()

    all_data = session.query(codetable).order_by(codetable.description).all()

    return all_data

