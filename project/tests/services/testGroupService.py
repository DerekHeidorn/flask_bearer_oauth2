
from project.tests.services.baseTest import BaseTest
from project.tests.helpers import commonHelper
from project.app.services import groupService


class GroupServiceTestCase(BaseTest):

    def test_get_group_by_name(self):
        print("running test_get_group_by_name...")
        created_group = commonHelper.create_public_group()

        group = groupService.get_group_by_name(created_group.group_name)
        self.assertEquals(created_group.group_name, group.group_name)

    def test_get_group_data_avengers(self):
        print("running test_get_group_data...")
        group = groupService.get_group_by_id(commonHelper.GROUP_THE_AVENGERS_GROUP_ID)

        group_data = groupService.get_group_detail(group.group_id)
        print("group_data=" + str(group_data))
        print("group_data.group=" + str(group_data.group))
        for m in group_data.active_members:
            print("active_member=" + str(m))
        for m in group_data.active_managers:
            print("active_managers=" + str(m))

        self.assertEqual(group_data.group.group_name, group.group_name)
        self.assertEqual(len(group_data.active_members), 10)
        self.assertEqual(len(group_data.active_managers), 1)
        self.assertEqual(group_data.active_managers[0].person.nick_name, "Iron Man")

    def test_get_group_data_abc(self):
        print("running test_get_group_data...")
        group = groupService.get_group_by_id(commonHelper.GROUP_COMPANY_ABC_WORKOUT_GROUP_ID)

        group_data = groupService.get_group_detail(group.group_id)
        print("group_data=" + str(group_data))
        print("group_data.group=" + str(group_data.group))
        for m in group_data.active_members:
            print("active_member=" + str(m))
        for m in group_data.active_managers:
            print("active_managers=" + str(m))

        self.assertEqual(group_data.group.group_name, group.group_name)
        self.assertEqual(len(group_data.active_members), 2)
        self.assertEqual(len(group_data.active_managers), 1)

    def test_get_group_data_zombie(self):
        print("running test_get_group_data...")
        group = groupService.get_group_by_id(commonHelper.GROUP_ZOMBIE_APOCALPSE_GROUP_ID)

        group_data = groupService.get_group_detail(group.group_id)
        print("group_data=" + str(group_data))
        print("group_data.group=" + str(group_data.group))
        for m in group_data.active_members:
            print("active_member=" + str(m))
        for m in group_data.active_managers:
            print("active_managers=" + str(m))

        self.assertEqual(group_data.group.group_name, group.group_name)
        self.assertEqual(len(group_data.active_members), 6)
        self.assertEqual(len(group_data.active_managers), 1)
