
import unittest
import json
from project.tests.web.baseTest import BaseTest 


class CodetableTestCases(BaseTest):

    def test_CtUserStatuses_OK(self):
        print("Running: test_CtUserStatuses_OK")

        resp = self.testClient.get('/api/v1.0/admin/codetables/' + "CtUserStatuses",
                                   headers={"MY_AUTH_TOKEN":
                                            "81c4e12b6879000837a3e7206795ee9ca874986cc97984d383c64093f5cc352d"})
        self.debug_response(resp)
        assert resp.status_code == 200
        code_dict = json.loads(resp.data)

        assert "1" == code_dict[0]["code"]
        assert "Batch" == code_dict[0]["description"]

    def test_CtUserStatusesCached_OK(self):
        print("Running: test_CtUserStatuses_cached_OK")

        resp = self.testClient.get('/api/v1.0/admin/codetables/' + "CtUserStatuses",
                                   headers={"MY_AUTH_TOKEN":
                                            "81c4e12b6879000837a3e7206795ee9ca874986cc97984d383c64093f5cc352d"})
        self.debug_response(resp)
        assert resp.status_code == 200
        code_dict = json.loads(resp.data)

        assert "1" == code_dict[0]["code"]
        assert "Batch" == code_dict[0]["description"]

    def test_CtUserTypes_OK(self):
        print("Running: test_CtUserTypes_OK")

        resp = self.testClient.get('/api/v1.0/admin/codetables/' + "CtUserTypes",
                                   headers={"MY_AUTH_TOKEN":
                                            "81c4e12b6879000837a3e7206795ee9ca874986cc97984d383c64093f5cc352d"})
        self.debug_response(resp)

        assert resp.status_code == 200
        code_dict = json.loads(resp.data)

        assert "A" == code_dict[0]["code"]
        assert "Active" == code_dict[0]["description"]


if __name__ == '__main__':
    unittest.main()
