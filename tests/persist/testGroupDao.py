import uuid
from datetime import datetime
from tests.persist.baseTest import BaseTest
from tests.helpers import commonHelper
from tests.utils import randomUtil
from app.persist import groupDao, baseDao
from app.models.group import Group, Person


class GroupDaoTestCase(BaseTest):

    def create_person(self):
        session = baseDao.get_session()
        p = Person()
        p.user_uuid = uuid.uuid4()
        new_person = groupDao.add_person(session, p)
        self.assertTrue(new_person.person_id > 0)

        return new_person

    def create_group(self):
        session = baseDao.get_session()
        g = Group()
        g.group_uuid = uuid.uuid4()
        g.group_name = "Group_" + randomUtil.random_string(10, 10)
        g.group_de = "Group Description: " + randomUtil.random_string(10, 10)
        g.group_type_cd = 'SP'
        g.created_ts = datetime.now()
        g.private_fl = False
        new_group = groupDao.add_group(session, g)
        self.assertTrue(new_group.group_id > 0)

        return new_group

    def test_get_user_by_username(self):
        print("running test_get_user_by_username...")
        session = baseDao.get_session()
        created_group = commonHelper.create_public_group()

        group = groupDao.get_group_by_uuid(session, created_group.group_uuid)
        self.assertEqual(created_group.group_name, group.group_name)

    def test_add_person(self):
        session = baseDao.get_session()
        p = Person()
        p.user_uuid = uuid.uuid4()
        new_person = groupDao.add_person(session, p)
        self.assertTrue(new_person.person_id > 0)

    def test_add_group(self):
        session = baseDao.get_session()
        g = Group()
        g.group_uuid = uuid.uuid4()
        g.group_name = "Group_" + randomUtil.random_string(10, 10)
        g.group_de = "Group Description: " + randomUtil.random_string(10, 10)
        g.group_type_cd = 'SP'
        g.created_ts = datetime.now()
        g.private_fl = False
        new_group = groupDao.add_group(session, g)

        self.assertTrue(new_group.group_id > 0)

    def test_add_group_manager(self):

        group = self.create_group()
        manager = self.create_person()

        session = baseDao.get_session()

        manager = groupDao.get_person_by_id(session, manager.person_id)
        group_manager = groupDao.add_group_manager(session, group.group_id, manager)

        self.assertEqual(group.group_id, group_manager.group_id)
        self.assertEqual(manager.person_id, group_manager.person_id)
        self.assertTrue(group_manager.manager_id > 0)

    def test_add_group_membership(self):
        group = self.create_group()
        member = self.create_person()

        session = baseDao.get_session()

        manager = groupDao.get_person_by_id(session, member.person_id)
        group_membership = groupDao.add_group_membership(session, group.group_id, manager)

        self.assertEqual(group.group_id, group_membership.group_id)
        self.assertEqual(manager.person_id, group_membership.person_id)
        self.assertTrue(group_membership.membership_id > 0)
