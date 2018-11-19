import uuid
from project.app.models.group import Group
from project.app.persist import groupDao, baseDao


class GroupData:
    group = None
    active_members = []
    active_managers = []

    def __repr__(self):
        return "<GroupData(group='%s', active_members='%s', active_managers='%s')>" \
               % (self.group, self.active_members, self.active_managers)


def get_group_data(group_id):
    session = baseDao.get_session()
    group_data = GroupData
    group_data.group = groupDao.get_group_by_id(group_id, session)
    group_data.active_members = groupDao.get_active_group_members(group_id, session)
    group_data.active_managers = groupDao.get_active_group_managers(group_id, session)

    return group_data;


def delete_group(group_id):
    return groupDao.delete_group(group_id)


def update_group(group_id, group_to_be_updated):
    return groupDao.update_group(group_id, group_to_be_updated)


def get_groups():
    return groupDao.get_groups()


def get_group_by_id(group_id):
    return groupDao.get_group_by_id(group_id)


def get_group_by_uuid(get_group_by_uuid):
    return groupDao.get_group_by_uuid(get_group_by_uuid)


def get_group_by_name(group_name):
    return groupDao.get_group_by_name(group_name)


def is_group_name_unique(group_name):
    return groupDao.is_group_name_unique(group_name)


def add_group(group_name):
    g = Group()
    g.group_uuid = uuid.uuid4()
    g.group_name = group_name
    g.group_type_cd = 'SP'
    return groupDao.add_group(g)
