import unittest
import json
from project.tests.web.baseTest import BaseTest 
from project.tests.utils import randomUtil 
from project.tests.helpers import commonHelper


class GroupApiTestCase(BaseTest):

    def create_group(self, staff_info):
        self.assertIsNotNone(staff_info)

        new_group_name = "Group_" + randomUtil.random_string(10, 25)
        new_group_de = "Random Group Description No. " + randomUtil.random_string(10, 25)

        resp = self.testClient.post('/api/v1.0/admin/group',
                                    headers={"Authorization": "bearer " + staff_info['token']},
                                    data=dict(
                                                group_name=new_group_name,
                                                group_de=new_group_de
                                             )
                                    )
        self.debug_response(resp)
        self.assertEqual(201, resp.status_code)
        response_data = json.loads(resp.data)

        return response_data["data"]["group_uuid"]

    def test_group_create(self):
        print("Running: test_group_create")
        staff_info = commonHelper.get_default_staff()

        new_group_name = "Group_" + randomUtil.random_string(10, 25)
        new_group_de = "Random Group Description No. " + randomUtil.random_string(10, 25)
        resp = self.testClient.post('/api/v1.0/admin/group',
                                    headers={"Authorization": "bearer " + staff_info['token']},
                                    data=dict(
                                                group_name=new_group_name,
                                                group_de=new_group_de
                                             )
                                    )
        self.debug_response(resp)

        self.assertEqual(201, resp.status_code)
        response_data = json.loads(resp.data)
        assert response_data["data"]["group_uuid"] is not None

    def test_group_by_uuid_ok(self):
        print("Running: test_group_by_uuid_ok")
        staff_info = commonHelper.get_default_staff()
        group_uuid = self.create_group(staff_info)

        resp = self.testClient.get('/api/v1.0/admin/group/' + str(group_uuid),
                                   headers={"Authorization": "bearer " + staff_info['token']})
        
        self.debug_response(resp)
        self.assertEqual(200, resp.status_code)
        group = json.loads(resp.data)

        assert group is not None
        
        self.assertEqual(group_uuid, group["data"]["group_uuid"])
        # self.assertEqual("Tester", user["firstName"])

# /api/v1.0/public/group/detail/<group_uuid>
    def test_get_public_group_detail_by_uuid(self):
        print("Running: test_get_public_group_detail_by_uuid")
        user_info = commonHelper.get_default_public_user()
        group = commonHelper.get_group(commonHelper.GROUP_THE_AVENGERS_GROUP_ID)

        print("user_info['token']: " + str(user_info['token']))
        print("group.group_uuid: " + str(group.group_uuid))

        resp = self.testClient.get('/api/v1.0/public/group/detail/' + str(group.group_uuid),
                                   headers={"Authorization": "bearer " + user_info['token']})

        self.debug_response(resp)
        self.assertEqual(200, resp.status_code)
        json_data = json.loads(resp.data)
        print("**group: " + str(json_data))

        assert group is not None

        self.assertEqual(str(group.group_uuid), json_data['data']["group"]["group_uuid"])
        # self.assertEqual("Tester", user["firstName"])

    def test_subscribe_to_group(self):
        print("Running: test_subscribe_to_group")
        user_info = commonHelper.get_default_public_user()
        group = commonHelper.get_group(commonHelper.GROUP_THE_AVENGERS_GROUP_ID)

        print("user_info['token']: " + str(user_info['token']))
        print("group.group_uuid: " + str(group.group_uuid))

        resp = self.testClient.post('/api/v1.0/my/subscribe/group/' + str(group.group_uuid),
                                    headers={"Authorization": "bearer " + user_info['token']})

        self.debug_response(resp)
        self.assertEqual(201, resp.status_code)
        json_data = json.loads(resp.data)
        print("**group: " + str(json_data))

        assert group is not None

        self.assertTrue(json_data['data']["from_ts"] is not None)


if __name__ == '__main__':
    unittest.main()
