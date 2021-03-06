import unittest
import json
from tests.web.baseTest import BaseTest


class CommonApiTestCases(BaseTest):

    def testVersion_OK(self):
        print("Running: test_version_OK")

        resp = self.testClient.get('/api/v1.0/public/app/version')
        self.debug_response(resp)
        assert resp.status_code == 200
        
        code_dict = json.loads(resp.data)
        assert "0.1" == code_dict["application.version"].strip()


if __name__ == '__main__':
    unittest.main()
