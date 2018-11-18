import uuid
from project.app.models.group import Group
from project.app.persist import groupDao


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
