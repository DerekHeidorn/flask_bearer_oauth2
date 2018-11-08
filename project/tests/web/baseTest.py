
import unittest
from project.app import main


class BaseTest(unittest.TestCase):

    app = main.create_application()

    def setUp(self):
        print("setting up Test Client...")
        self.app.config['TESTING'] = True
        self.testClient = self.app.test_client()

    def tearDown(self):
        pass

    def debug_response(self, response):
        
        print("type=" + str(type(response)))
        print("status_code=" + str(response.status_code))
        print("response.content_type=" + str(response.content_type))
        
        if response.data:
            print("Data=" + response.data.decode("utf-8") )
