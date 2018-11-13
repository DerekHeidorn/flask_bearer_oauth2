import unittest
import json
from project.tests.web.baseTest import BaseTest 
from project.tests.utils import randomUtil 
from project.tests.helpers import commonHelper


class UserServiceTestCase(BaseTest):

    def create_group(self, staff_info):
        self.assertIsNotNone(staff_info)

        new_group_name = "Group_" + randomUtil.random_string(10, 25)

        resp = self.testClient.post('/api/v1.0/admin/group',
                                    headers={"Authorization": "bearer " + staff_info['token']},
                                    data=dict(
                                                group_name=new_group_name
                                             )
                                    )
        self.debug_response(resp)
        self.assertEquals(201, resp.status_code)
        response_data = json.loads(resp.data)

        return response_data["group_uuid"]

    def test_group_create(self):
        print("Running: test_group_create")
        staff_info = commonHelper.get_default_staff()

        new_group_name = "Group_" + randomUtil.random_string(10, 25)
        resp = self.testClient.post('/api/v1.0/admin/group',
                                    headers={"Authorization": "bearer " + staff_info['token']},
                                    data=dict(
                                                group_name=new_group_name
                                             )
                                    )
        self.debug_response(resp)

        self.assertEquals(201, resp.status_code)
        response_data = json.loads(resp.data)
        assert response_data["group_uuid"] is not None

    def test_group_by_uuid_ok(self):
        print("Running: test_group_by_uuid_ok")
        staff_info = commonHelper.get_default_staff()
        group_uuid = self.create_group(staff_info)

        resp = self.testClient.get('/api/v1.0/admin/group/' + str(group_uuid),
                                   headers={"Authorization": "bearer " + staff_info['token']})
        
        self.debug_response(resp)
        self.assertEquals(200, resp.status_code)
        group = json.loads(resp.data)

        assert group is not None
        
        self.assertEquals(group_uuid, group["group_uuid"])
        # self.assertEquals("Tester", user["firstName"])


if __name__ == '__main__':
    unittest.main()
