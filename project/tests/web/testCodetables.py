
import unittest
import json
from project.tests.web.baseTest import BaseTest 


class CodetableTestCases(BaseTest):

    def test_CtGroupTypes_OK(self):
        print("Running: test_CtGroupTypes_OK")

        resp = self.testClient.get('/api/v1.0/admin/codetables/' + "CtGroupTypes")
        self.debug_response(resp)

        assert resp.status_code == 200
        code_dict = json.loads(resp.data)

        assert "FI" == code_dict[0]["code"]
        assert "Fitness" == code_dict[0]["description"]

    def test_CtGroupTypesCached_OK(self):
        print("Running: test_CtGroupTypesCached_OK")

        resp = self.testClient.get('/api/v1.0/admin/codetables/' + "CtGroupTypes")
        self.debug_response(resp)
        assert resp.status_code == 200
        code_dict = json.loads(resp.data)

        assert "FI" == code_dict[0]["code"]
        assert "Fitness" == code_dict[0]["description"]


if __name__ == '__main__':
    unittest.main()
