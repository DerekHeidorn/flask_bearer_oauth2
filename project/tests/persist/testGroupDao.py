import uuid
from project.tests.persist.baseTest import BaseTest
from project.tests.helpers import commonHelper
from project.tests.utils import randomUtil
from project.app.persist import groupDao, baseDao
from project.app.models.group import Group, Person


class GroupDaoTestCase(BaseTest):

    def create_person(self):
        p = Person()
        p.user_uuid = uuid.uuid4()
        p.nick_name = "Nickname_" + randomUtil.random_string(10, 10)
        new_person = groupDao.add_person(p)
        self.assertTrue(new_person.person_id > 0)

        return new_person

    def create_group(self):
        g = Group()
        g.group_uuid = uuid.uuid4()
        g.group_name = "Group_" + randomUtil.random_string(10, 10)
        g.group_type_cd = 'SP'
        new_group = groupDao.add_group(g)
        self.assertTrue(new_group.group_id > 0)

        return new_group

    def test_get_user_by_username(self):
        print("running test_get_user_by_username...")
        created_group = commonHelper.create_public_group()

        group = groupDao.get_group_by_uuid(created_group.group_uuid)
        self.assertEqual(created_group.group_name, group.group_name)

    def test_add_person(self):

        p = Person()
        p.user_uuid = uuid.uuid4()
        p.nick_name = "Nickname_" + randomUtil.random_string(10, 10)
        new_person = groupDao.add_person(p)
        self.assertTrue(new_person.person_id > 0)

    def test_add_group(self):

        g = Group()
        g.group_uuid = uuid.uuid4()
        g.group_name = "Group_" + randomUtil.random_string(10, 10)
        g.group_type_cd = 'SP'
        new_group = groupDao.add_group(g)

        self.assertTrue(new_group.group_id > 0)

    def test_add_group_manager(self):

        group = self.create_group()
        manager = self.create_person()

        session = baseDao.get_session()

        manager = groupDao.get_person_by_id(manager.person_id, session)
        group_manager = groupDao.add_group_manager(group.group_id, manager, session)

        self.assertEqual(group.group_id, group_manager.group_id)
        self.assertEqual(manager.person_id, group_manager.person_id)
        self.assertTrue(group_manager.manager_id > 0)

    def test_add_group_membership(self):

        group = self.create_group()
        member = self.create_person()

        session = baseDao.get_session()

        manager = groupDao.get_person_by_id(member.person_id, session)
        group_membership = groupDao.add_group_member(group.group_id, manager, session)

        self.assertEqual(group.group_id, group_membership.group_id)
        self.assertEqual(manager.person_id, group_membership.person_id)
        self.assertTrue(group_membership.membership_id > 0)
