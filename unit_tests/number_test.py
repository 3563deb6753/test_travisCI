import my_number
import unittest

class TestMyNumber(unittest.TestCase):
    def test_right_number(self):
        self.assertEqual(my_number.get_number(), 5)
 
if __name__ == '__main__':
    unittest.main()
