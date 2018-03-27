import unittest
import hello_world as hw


class HelloWorldTest(unittest.TestCase):

    def setUp(self):
        self.app = hw.app.test_client()
        self.app.testing = True


    def test_hello_world(self):
        html = self.app.get('/')
        self.assertIn('Vijay Python', str(html.data))


if __name__ == "__main__":
    unittest.main()