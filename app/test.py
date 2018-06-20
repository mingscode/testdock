import unittest
import testdock

class TestCase(unittest.TestCase):

   def setUp(self):
       testdock.app.config["TESTING"] = True
       self.app = testdock.app.test_client()

   def test_get_mainpage(self):
       page = self.app.post("/", data=dict(name="Ming"))
       assert page.status_code == 200
       assert 'Hello' in str(page.data)
       assert 'Ming' in str(page.data)

if __name__ == '__main__':
   unittest.main()
