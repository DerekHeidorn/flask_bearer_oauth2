from sqlalchemy import func

from project.app.models.group import Group
from project.app.persist import baseDao


def add_group(new_group, session=None):
    """
    Creates and saves a new group to the database.

    :param new_group: new Group record
    :param session: database session

    """
    if session is None:
        session = baseDao.get_session()

    session.add(new_group)
    session.commit()

    return new_group


def get_groups(session=None):
    """
    Get all groups, order by Group Name

    :param session: existing db session
    :return: groups.
    """
    if session is None:
        session = baseDao.get_session()

    all_users = session.query(Group).order_by(Group.group_name).all()

    return all_users


def get_group_by_id(group_id, session=None):
    """
    Gets the Group based on the id parameter

    :param group_id: The id of the group which needs to be loaded
    :param session: existing db session
    :return: The Group.
    """
    if session is None:
        session = baseDao.get_session()

    user = session.query(Group).filter(Group.group_id == group_id).first()
    return user


def get_group_by_uuid(group_uuid, session=None):
    """
    Gets the Group based on the id parameter

    :param group_uuid: The uuid of the group which needs to be loaded
    :param session: existing db session
    :return: The Group.
    """
    if session is None:
        session = baseDao.get_session()

    user = session.query(Group).filter(Group.group_uuid == group_uuid).first()
    return user


def get_group_by_name(group_name, session=None):
    """
    Gets the Group based on the group name parameter

    :param group_name: The group name of the Group which needs to be loaded
    :param session: existing db session
    :return: The Group.
    """

    if session is None:
        session = baseDao.get_session()

    user = session.query(Group).filter(func.lower(Group.group_name) == func.lower(group_name)).first()
    return user


def is_group_name_unique(group_name, exclude_group_id=None, session=None):
    """
    Gets the User based on the username parameter

    :param group_name: The group name of the group which needs to be loaded
    :param exclude_group_id: exclude the current group
    :param session: existing db session
    :return: The group.
    """

    if session is None:
        session = baseDao.get_session()

    query = session.query(func.count(Group.id)).filter(func.lower(Group.group_name) == func.lower(group_name))
    if exclude_group_id is not None:
        query.filter(Group.id != exclude_group_id)

    count = query.scalar()

    return count == 0


def update_group(group_id, group_to_be_updated):
    updated_group = None
    session = baseDao.get_session()

    group = get_group_by_id(group_id, session=session)
    if group is None:
        return updated_group

    group.group_name = group_to_be_updated["group_name"]

    session.commit()
    updated_user = get_group_by_id(group_id)

    return updated_user


def delete_group(group_id):
    id_value = int(group_id)
    if id_value < 0:
        raise ValueError("Parameter [id] should be a positive number!")

    if id_value > 0:
        session = baseDao.get_session()
        items_deleted = session.query(Group).filter(Group.group_id == id_value).delete()
        return items_deleted > 0

    return False
