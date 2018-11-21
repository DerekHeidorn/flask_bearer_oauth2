from datetime import datetime
from sqlalchemy import func, or_, and_

from project.app.models.group import Group, Person, Membership, GroupManager
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

    all_groups = session.query(Group).order_by(Group.group_name).all()

    return all_groups


def get_group_by_id(group_id, session=None):
    """
    Gets the Group based on the id parameter

    :param group_id: The id of the group which needs to be loaded
    :param session: existing db session
    :return: The Group.
    """
    if session is None:
        session = baseDao.get_session()

    group = session.query(Group).filter(Group.group_id == group_id).first()
    return group


def get_group_by_uuid(group_uuid, session=None):
    """
    Gets the Group based on the id parameter

    :param group_uuid: The uuid of the group which needs to be loaded
    :param session: existing db session
    :return: The Group.
    """
    if session is None:
        session = baseDao.get_session()

    group = session.query(Group).filter(Group.group_uuid == group_uuid).first()
    return group


def get_group_by_name(group_name, session=None):
    """
    Gets the Group based on the group name parameter

    :param group_name: The group name of the Group which needs to be loaded
    :param session: existing db session
    :return: The Group.
    """

    if session is None:
        session = baseDao.get_session()

    group = session.query(Group).filter(func.lower(Group.group_name) == func.lower(group_name)).first()
    return group


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


def get_group_count(session=None):
    if session is None:
        session = baseDao.get_session()
    row_count = session.query(func.count(Group.group_id)).scalar()
    return row_count


def get_group_member(group_id, person_id, session=None):
    if session is None:
        session = baseDao.get_session()

    member = session.query(Membership)\
        .filter(and_(Membership.group_id == group_id,
                     Membership.person_id == person_id
                     )) \
        .first()

    return member


def get_group_manager(group_id, person_id, session=None):
    if session is None:
        session = baseDao.get_session()

    member = session.query(GroupManager)\
        .filter(and_(GroupManager.group_id == group_id,
                     GroupManager.person_id == person_id
                     )) \
        .first()

    return member


def get_person_by_id(person_id, session=None):
    if session is None:
        session = baseDao.get_session()

    person = session.query(Person).filter(Person.person_id == person_id).first()
    return person


def get_person_by_uuid(user_uuid, session=None):
    if session is None:
        session = baseDao.get_session()

    person = session.query(Person).filter(Person.user_uuid == user_uuid).first()
    return person


def get_active_group_members(group_id, session=None):
    if session is None:
        session = baseDao.get_session()

    members = session.query(Membership)\
        .filter(and_(Membership.group_id == group_id,
                     Membership.from_ts <= func.current_timestamp()),
                or_(Membership.to_ts.is_(None), Membership.to_ts >= func.current_timestamp()))\
        .all()

    return members


def get_active_group_managers(group_id, session=None):
    if session is None:
        session = baseDao.get_session()

    managers = session.query(GroupManager)\
        .filter(GroupManager.group_id == group_id
                and GroupManager.from_ts <= func.current_timestamp(),
                or_(GroupManager.to_ts.is_(None), GroupManager.to_ts >= func.current_timestamp()))\
        .all()

    return managers


def add_person(new_person, session=None):
    """
    Creates and saves a new person to the database.

    :param new_person: new person record
    :param session: database session

    """
    if session is None:
        session = baseDao.get_session()

    session.add(new_person)
    session.commit()

    return new_person


def add_group_manager(group_id, person, session=None):
    if session is None:
        session = baseDao.get_session()

    group_manager = GroupManager()
    group_manager.group_id = group_id

    group_manager.from_ts = datetime.now()
    group_manager.person_id = person.person_id
    group_manager.person = person

    session.add(group_manager)
    session.commit()

    return group_manager


def add_group_member(group_id, person, session=None):
    if session is None:
        session = baseDao.get_session()

    group_membership = Membership()
    group_membership.group_id = group_id

    group_membership.from_ts = datetime.now()
    group_membership.person_id = person.person_id
    group_membership.person = person

    session.add(group_membership)
    session.commit()

    return group_membership

