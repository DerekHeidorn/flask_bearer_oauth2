import uuid
from project.app.models.group import Group
from project.app.persist import groupDao, baseDao


class GroupDetail:
    group = None
    active_members = []
    active_managers = []

    def __repr__(self):
        return "<GroupDetail(group='%s', active_members='%s', active_managers='%s')>" \
               % (self.group, self.active_members, self.active_managers)


def get_group_detail_by_uuid(group_uuid):
    session = baseDao.get_session()
    group_detail = GroupDetail()
    group = groupDao.get_group_by_uuid(group_uuid, session)
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


def get_groups():
    return groupDao.get_groups()


def get_groups_by_user_uuid(user_uuid):
    return groupDao.get_groups_by_user_uuid(user_uuid)

def get_group_by_id(group_id):
    return groupDao.get_group_by_id(group_id)


def get_group_by_uuid(group_uuid):
    return groupDao.get_group_by_uuid(group_uuid)


def get_group_by_name(group_name):
    return groupDao.get_group_by_name(group_name)


def is_group_name_unique(group_name):
    return groupDao.is_group_name_unique(group_name)


def add_group(group_name, group_de):
    g = Group()
    g.group_uuid = uuid.uuid4()
    g.group_name = group_name
    g.group_de = group_de
    g.group_type_cd = 'SP'
    return groupDao.add_group(g)


def get_group_member_by_uuid(group_uuid, person_uuid):
    session = baseDao.get_session()

    group = groupDao.get_group_by_uuid(group_uuid, session)
    person = groupDao.get_person_by_uuid(person_uuid, session)

    return groupDao.get_group_member(group.group_id, person.person_id, session)


def get_group_manager_by_uuid(group_uuid, person_uuid):
    session = baseDao.get_session()

    group = groupDao.get_group_by_uuid(group_uuid, session)
    person = groupDao.get_person_by_uuid(person_uuid, session)

    return groupDao.get_group_manager(group.group_id, person.person_id, session)
