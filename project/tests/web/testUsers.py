import pytest
import unittest
import json
from project.tests.web.baseTest import BaseTest 
from project.tests.utils import randomUtil 
from project.tests.helpers import commonHelper


class UserServiceTestCase(BaseTest):

    def createUser(self, staffInfo):
        
        resp = self.testClient.post('/api/v1.0/admin/user'
        , headers={"Authorization":"bearer " + staffInfo['token']}
        ,data = dict(
            firstName = "Tester",
            lastName = "Auto",
            username = randomUtil.randomUsername(),
            password = randomUtil.randomString(10, 25)
        ))
        self.debugResponse(resp)
        self.assertEquals(201, resp.status_code)
        responseData = json.loads(resp.data)

        return responseData["id"]

    def testUserCreate(self):
        print("Running: testUserCreate")
        staffInfo = commonHelper.getDefaultStaff()
        resp = self.testClient.post('/api/v1.0/admin/user'
        , headers={"Authorization":"bearer " + staffInfo['token']}
        ,data = dict(
            firstName = "Tester",
            lastName = "Auto",
            username = randomUtil.randomUsername(),
            password = randomUtil.randomString(10, 25)
        ))
        self.debugResponse(resp)

        self.assertEquals(201, resp.status_code)
        responseData = json.loads(resp.data)
        assert responseData["id"] is not None
        assert responseData["url"] is not None

        return responseData["id"]

    def testUserById_OK(self):
        print("Running: testUserById_OK")
        staffInfo = commonHelper.getDefaultStaff()
        id = self.createUser(staffInfo)


        print("\nRunning: test_user_by_id_OK")
        resp = self.testClient.get('/api/v1.0/admin/user/' + str(id)
        , headers={"Authorization":"bearer " + staffInfo['token']})
        
        self.debugResponse(resp)
        self.assertEquals( 200, resp.status_code)
        user = json.loads(resp.data)

        assert user is not None
        
        self.assertEquals(id, user["id"])
        self.assertEquals("Tester", user["firstName"])

    def testUpdateUser(self):
        print("Running: testUpdateUser")
        staffInfo = commonHelper.getDefaultStaff()
        id = self.createUser(staffInfo)
        newFirstName = "UpdatedTester"
        newLastName = "UpdatedAuto"
        newUsername = "updated.auto@tester.com"

        print("\nRunning: test_update_user")
        resp = self.testClient.put('/api/v1.0/admin/user/' + str(id)
        , headers={"Authorization":"bearer " + staffInfo['token']},
        data = dict(
            firstName = newFirstName,
            lastName = newLastName,
            username = newUsername
        ))
        self.debugResponse(resp)
        user = json.loads(resp.data)

        assert user is not None
        
        self.assertEquals(id,  user["id"])
        self.assertEquals( newFirstName , user["firstName"])
        self.assertEquals( newLastName , user["lastName"])
        self.assertEquals( newUsername , user["username"])


    def testUserDelete(self):
        print("Running: testUserDelete")
        staffInfo = commonHelper.getDefaultStaff()
        id = self.createUser(staffInfo)

        resp = self.testClient.delete('/api/v1.0/admin/user/' + str(id)
            , headers={"Authorization":"bearer " + staffInfo['token']}
        )
        
        print("resp.data=" + str(resp.data))
        self.assertEquals( 200, resp.status_code)


if __name__ == '__main__':
    unittest.main()
