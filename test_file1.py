import unittest
from file1 import double

class Testfile1(unittest.TestCase):
    def test_double(self):
        self.assertEqual(double(10),20)
        self.assertEqual(double(15),30)
        self.assertEqual(double(20),40)
        self.assertEqual(double(30),60)
        
if __name__ == '__main__':
    unittest.main()