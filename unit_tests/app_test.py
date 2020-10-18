#As soon as OpenGL is called, it crashes Jenkins - don't know why
import my_app
import unittest

class TestMyApp(unittest.TestCase):
    def setUp(self):
        self.app = my_app.MainApp()
        self.app.run()

    def test_run(self):
        self.assertTrue(self.app.get_running_app())

    def tearDown(self):
        self.app.stop()

if __name__ == '__main__':
    unittest.main()
