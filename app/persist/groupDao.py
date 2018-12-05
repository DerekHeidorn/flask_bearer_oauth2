from datetime import datetime
from sqlalchemy import func, and_

from app.models.group import Group, Person, Membership, GroupManager, MembershipHistory, GroupManagerHistory
from app.persist import baseDao


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


def get_groups_by_filter(is_private_fl, session=None):
    """
    Get all groups, order by Group Name

    :param is_private_fl: filter on private group flag
    :param session: existing db session
    :return: groups.
    """
    if session is None:
        session = baseDao.get_session()

    if is_private_fl is not None:
        all_groups = session.query(Group) \
            .filter(Group.private_fl == is_private_fl) \
            .order_by(Group.group_name).all()
    else:
        all_groups = get_groups()

    return all_groups


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


def get_groups_by_user_uuid(user_uuid, session=None):
    """
    Get all groups, order by Group Name
    :param user_uuid: user UUID
    :param session: existing db session
    :return: groups.
    """
    if session is None:
        session = baseDao.get_session()

    group_ids = []

    membership_group_ids = session.query(Membership.group_id) \
        .join(Membership.person) \
        .filter(Person.user_uuid == user_uuid) \
        .all()

    manager_group_ids = session.query(GroupManager.group_id) \
        .join(GroupManager.person) \
        .filter(Person.user_uuid == user_uuid) \
        .all()

    if membership_group_ids is not None:
        for i in membership_group_ids:
            group_ids.append(i)

    if manager_group_ids is not None:
        for i in manager_group_ids:
            group_ids.append(i)

    all_groups = session.query(Group) \
        .filter(Group.group_id.in_(group_ids)) \
        .all()

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


def get_group_by_uuid(group_uuid, is_private_fl=None, session=None):
    """
    Gets the Group based on the id parameter

    :param group_uuid: The uuid of the group which needs to be loaded
    :param is_private_fl: whether to query the group is private or not
    :param session: existing db session
    :return: The Group.
    """
    if session is None:
        session = baseDao.get_session()

    filters = {'group_uuid': group_uuid}
    if is_private_fl is not None:
        filters["private_fl"] = is_private_fl
    group = session.query(Group).filter_by(**filters).first()
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
        .filter(Membership.group_id == group_id)\
        .all()

    return members


def is_active_group_member(group_id, person_id, session=None):
    if session is None:
        session = baseDao.get_session()

    member = session.query(Membership)\
        .filter(Membership.group_id == group_id, Membership.person_id == person_id)\
        .first()

    return member is not None


def get_membership_by_ids(group_id, person_id, session=None):
    if session is None:
        session = baseDao.get_session()

    membership = session.query(Membership)\
        .filter(Membership.group_id == group_id,
                Membership.person_id == person_id)\
        .first()

    return membership


def is_active_group_manager(group_id, person_id, session=None):
    if session is None:
        session = baseDao.get_session()

    manager = session.query(GroupManager)\
        .filter(GroupManager.group_id == group_id, GroupManager.person_id == person_id)\
        .first()

    return manager is not None


def get_active_group_managers(group_id, session=None):
    if session is None:
        session = baseDao.get_session()

    managers = session.query(GroupManager)\
        .filter(GroupManager.group_id == group_id)\
        .all()

    return managers


def get_group_manager_by_ids(group_id, person_id, session=None):
    if session is None:
        session = baseDao.get_session()

    group_manager = session.query(GroupManager) \
        .filter(GroupManager.group_id == group_id,
                GroupManager.person_id == person_id) \
        .first()

    return group_manager


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


def add_group_manager_history(group_manager, session=None):
    """
    Creates and saves a new history record to the database.

    :param group_manager: group manager to make history record from
    :param session: database session

    """
    if session is None:
        session = baseDao.get_session()

    h = GroupManagerHistory()
    h.manager_id = group_manager.manager_id
    h.group_id = group_manager.group_id
    h.person_id = group_manager.person_id
    h.from_ts = group_manager.from_ts
    h.to_ts = datetime.now()

    session.add(h)
    session.commit()

    return h


def remove_group_manager(group_id, person_id, session=None):
    if session is None:
        session = baseDao.get_session()

    group_manager = get_group_manager_by_ids(group_id, person_id, session)

    if group_manager is not None:
        add_group_manager_history(group_manager, session)

        items_deleted = session.query(GroupManager).filter(GroupManager.group_id == group_id,
                                                           GroupManager.person_id == person_id).delete()
        return items_deleted > 0

    return False


def add_group_membership(group_id, person, session=None):
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


def add_membership_history(membership, session=None):
    """
    Creates and saves a new history record to the database.

    :param membership: membership to make history record from
    :param session: database session

    """
    if session is None:
        session = baseDao.get_session()

    h = MembershipHistory()
    h.membership_id = membership.membership_id
    h.group_id = membership.group_id
    h.person_id = membership.person_id
    h.from_ts = membership.from_ts
    h.to_ts = datetime.now()

    session.add(h)
    session.commit()

    return h


def remove_group_membership(group_id, person_id, session=None):
    if session is None:
        session = baseDao.get_session()

    membership = get_membership_by_ids(group_id, person_id, session)

    if membership is not None:
        add_membership_history(membership, session)

        items_deleted = session.query(Membership).filter(Membership.group_id == group_id,
                                                         Membership.person_id == person_id).delete()
        return items_deleted > 0

    return False
