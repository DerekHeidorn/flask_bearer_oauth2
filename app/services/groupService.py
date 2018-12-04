import uuid
from datetime import datetime
from app.models.group import Group, Person
from app.persist import groupDao, baseDao
from app import core


class GroupDetail:
    group = None
    active_members = []
    active_managers = []

    def __repr__(self):
        return "<GroupDetail(group='%s', active_members='%s', active_managers='%s')>" \
               % (self.group, self.active_members, self.active_managers)


def get_group_detail_by_uuid(group_uuid, is_private_fl=None):
    session = baseDao.get_session()
    group_detail = GroupDetail()
    group = groupDao.get_group_by_uuid(group_uuid, is_private_fl, session)
    group_detail.group = group
    group_detail.active_members = groupDao.get_active_group_members(group.group_id, session)
    group_detail.active_managers = groupDao.get_active_group_managers(group.group_id, session)

    return group_detail


def get_group_detail(group_id):
    session = baseDao.get_session()
    group_detail = GroupDetail()
    group_detail.group = groupDao.get_group_by_id(group_id, session)
    group_detail.active_members = groupDao.get_active_group_members(group_id, session)
    group_detail.active_managers = groupDao.get_active_group_managers(group_id, session)

    return group_detail


def delete_group(group_id):
    return groupDao.delete_group(group_id)


def update_group(group_id, group_to_be_updated):
    return groupDao.update_group(group_id, group_to_be_updated)


def get_public_groups(user_uuid):
    session = baseDao.get_session()

    public_groups = groupDao.get_groups_by_filter(False, session)
    subscribed_groups = groupDao.get_groups_by_user_uuid(user_uuid, session)

    return {"groups": public_groups, "subscribed": subscribed_groups}


def get_groups():
    return groupDao.get_groups()


def get_groups_by_user_uuid(user_uuid):
    return groupDao.get_groups_by_user_uuid(user_uuid)


def get_group_by_id(group_id):
    return groupDao.get_group_by_id(group_id)


def get_group_by_uuid(group_uuid, is_private_fl=None):
    return groupDao.get_group_by_uuid(group_uuid, is_private_fl)


def get_group_by_name(group_name):
    return groupDao.get_group_by_name(group_name)


def is_group_name_unique(group_name):
    return groupDao.is_group_name_unique(group_name)


def add_group(group_name, group_de):
    g = Group()
    g.group_uuid = uuid.uuid4()
    g.group_name = group_name
    g.group_de = group_de
    g.created_ts = datetime.now()
    g.private_fl = False
    g.group_type_cd = 'SP'
    return groupDao.add_group(g)


def get_group_member_by_uuid(group_uuid, person_uuid):
    session = baseDao.get_session()

    group = groupDao.get_group_by_uuid(group_uuid, None, session)
    person = groupDao.get_person_by_uuid(person_uuid, session)

    return groupDao.get_group_member(group.group_id, person.person_id, session)


def get_group_manager_by_uuid(group_uuid, person_uuid):
    session = baseDao.get_session()

    group = groupDao.get_group_by_uuid(group_uuid, None, session)
    person = groupDao.get_person_by_uuid(person_uuid, session)

    return groupDao.get_group_manager(group.group_id, person.person_id, session)


def add_group_membership(group_uuid, user_uuid):
    session = baseDao.get_session()

    group = groupDao.get_group_by_uuid(group_uuid, None, session)

    if group:
        if not group.private_fl:
            try:
                person = groupDao.get_person_by_uuid(user_uuid, session)
                if person is None:
                    person = Person()
                    person.user_uuid = user_uuid
                    person = groupDao.add_person(person, session)

                group_membership = groupDao.add_group_membership(group.group_id, person, session)
                session.commit()
                return group_membership
            except Exception:
                session.rollback()
                raise
        else:
            raise Exception("Not a public group")
    else:
        raise Exception("Group Doesn't exist!")


def remove_group_membership(group_uuid, user_uuid):
    core.logger.debug("Removing Group Membership: " + str(group_uuid) + ", " + str(user_uuid))

    session = baseDao.get_session()

    group = groupDao.get_group_by_uuid(group_uuid, None, session)

    if group:
        if not group.private_fl:
            try:
                person = groupDao.get_person_by_uuid(user_uuid, session)
                if person is None:
                    person = Person()
                    person.user_uuid = user_uuid
                    person = groupDao.add_person(person, session)

                is_removed = groupDao.remove_group_membership(group.group_id, person.person_id, session)
                session.commit()
                return is_removed
            except Exception:
                session.rollback()
                raise
        else:
            raise Exception("Not a public group")
    else:
        raise Exception("Group Doesn't exist!")


def add_group_manager(group_uuid, user_uuid):
    core.logger.debug("Adding Group Manager: " + str(group_uuid) + ", " + str(user_uuid))

    session = baseDao.get_session()

    group = groupDao.get_group_by_uuid(group_uuid, None, session)

    if group:
        if not group.private_fl:
            try:
                person = groupDao.get_person_by_uuid(user_uuid, session)
                if person is None:
                    person = Person()
                    person.user_uuid = user_uuid
                    person = groupDao.add_person(person, session)

                group_manager = groupDao.add_group_manager(group.group_id, person, session)
                session.commit()
                return group_manager
            except Exception:
                session.rollback()
                raise
        else:
            raise Exception("Not a public group")
    else:
        raise Exception("Group Doesn't exist!")


def remove_group_manager(group_uuid, user_uuid):
    core.logger.debug("Removing Group Manager: " + str(group_uuid) + ", " + str(user_uuid))

    session = baseDao.get_session()

    group = groupDao.get_group_by_uuid(group_uuid, None, session)

    if group:
        if not group.private_fl:
            try:
                person = groupDao.get_person_by_uuid(user_uuid, session)
                if person is None:
                    person = Person()
                    person.user_uuid = user_uuid
                    person = groupDao.add_person(person, session)

                is_removed = groupDao.remove_group_manager(group.group_id, person.person_id, session)
                session.commit()
                return is_removed
            except Exception:
                session.rollback()
                raise
        else:
            raise Exception("Not a public group")
    else:
        raise Exception("Group Doesn't exist!")
