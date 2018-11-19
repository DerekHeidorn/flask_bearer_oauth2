import uuid
from project.tests.persist.baseTest import BaseTest
from project.tests.helpers import commonHelper
from project.tests.utils import randomUtil
from project.app.persist import groupDao
from project.app.models.group import Group


class UserDaoTestCase(BaseTest):

    def test_get_user_by_username(self):
        print("running test_get_user_by_username...")
        created_group = commonHelper.create_public_group()

        group = groupDao.get_group_by_uuid(created_group.group_uuid)
        self.assertEqual(created_group.group_name, group.group_name)

    def test_add_group(self):

        g = Group()
        g.group_uuid = uuid.uuid4()
        g.group_name = "Group_" + randomUtil.random_string(10, 10)
        g.group_type_cd = 'SP'
        new_group = groupDao.add_group(g)

        self.assertTrue(new_group.group_id > 0)


