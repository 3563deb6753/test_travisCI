import my_string
import unittest




class TestMyStringMethods(unittest.TestCase):
    
    def test_true_false(self):
        self.assertTrue(my_string.send_true())
        self.assertFalse(my_string.send_false())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()



