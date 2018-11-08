import unittest
import json
from project.tests.web.baseTest import BaseTest 
from project.tests.utils import randomUtil 
from project.tests.helpers import commonHelper


class UserServiceTestCase(BaseTest):

    def createUser(self, staff_info):
        
        resp = self.testClient.post('/api/v1.0/admin/user',
                                    headers={"Authorization": "bearer " + staff_info['token']},
                                    data=dict(
                                                first_name="Tester",
                                                last_name="Auto",
                                                username=randomUtil.random_username(),
                                                password=randomUtil.random_string(10, 25)
                                             )
                                    )
        self.debug_response(resp)
        self.assertEquals(201, resp.status_code)
        response_data = json.loads(resp.data)

        return response_data["id"]

    def testUserCreate(self):
        print("Running: testUserCreate")
        staff_info = commonHelper.get_default_staff()
        resp = self.testClient.post('/api/v1.0/admin/user',
                                    headers={"Authorization": "bearer " + staff_info['token']},
                                    data=dict(
                                                firstName="Tester",
                                                lastName="Auto",
                                                username=randomUtil.random_username(),
                                                password=randomUtil.random_string(10, 25)
                                             )
                                    )
        self.debug_response(resp)

        self.assertEquals(201, resp.status_code)
        response_data = json.loads(resp.data)
        assert response_data["id"] is not None
        assert response_data["url"] is not None

        return response_data["id"]

    def test_user_by_id_ok(self):
        print("Running: testUserById_OK")
        staff_info = commonHelper.get_default_staff()
        user_id = self.createUser(staff_info)

        print("\nRunning: test_user_by_id_OK")
        resp = self.testClient.get('/api/v1.0/admin/user/' + str(user_id),
                                   headers={"Authorization": "bearer " + staff_info['token']})
        
        self.debug_response(resp)
        self.assertEquals(200, resp.status_code)
        user = json.loads(resp.data)

        assert user is not None
        
        self.assertEquals(id, user["id"])
        self.assertEquals("Tester", user["firstName"])

    def test_update_user(self):
        print("Running: test_update_user")
        staff_info = commonHelper.get_default_staff()
        user_id = self.createUser(staff_info)
        new_first_name = "UpdatedTester"
        new_last_name = "UpdatedAuto"
        new_username = "updated.auto@tester.com"

        print("\nRunning: test_update_user")
        resp = self.testClient.put('/api/v1.0/admin/user/' + str(user_id),
                                   headers={"Authorization": "bearer " + staff_info['token']},
                                   data=dict(
                                               first_name=new_first_name,
                                               last_name=new_last_name,
                                               username=new_username
                                            )
                                   )
        self.debug_response(resp)
        user = json.loads(resp.data)

        assert user is not None
        
        self.assertEquals(id,  user["id"])
        self.assertEquals(new_first_name, user["first_name"])
        self.assertEquals(new_last_name, user["last_name"])
        self.assertEquals(new_username, user["username"])

    def test_user_delete(self):
        print("Running: test_user_delete")
        staff_info = commonHelper.get_default_staff()
        user_id = self.createUser(staff_info)

        resp = self.testClient.delete('/api/v1.0/admin/user/' + str(user_id),
                                      headers={"Authorization": "bearer " + staff_info['token']}
                                      )
        
        print("resp.data=" + str(resp.data))
        self.assertEquals(200, resp.status_code)


if __name__ == '__main__':
    unittest.main()
