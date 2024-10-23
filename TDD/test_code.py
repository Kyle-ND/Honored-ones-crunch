import unittest
import mycode

class Tests(unittest.TestCase):

    def test_add(self):
        self.assertEqual(mycode.add(6,6),12)
        self.assertEqual(mycode.add(-1,2),1)
        self.assertEqual(mycode.add(-5,2),-3)

    def test_multiply(self):
        self.assertEqual(mycode.multiply(6,3),18)
        self.assertEqual(mycode.multiply(1,1),1)
        self.assertEqual(mycode.multiply(5,2),10)

    def test_subtract(self):
        self.assertEqual(mycode.subtract(6,6),0)
        self.assertNotEqual(mycode.subtract(-1,-1),2)
        self.assertEqual(mycode.subtract(5,2),3)

    def test_divide(self):
        self.assertEqual(mycode.divide(6,6),1)
        self.assertEqual(mycode.divide(12,2),6)
        self.assertEqual(mycode.divide(5,2),2.5)
        self.assertEqual(mycode.divide(5,0),"Invalid")
if __name__ == "__main__":
    unittest.main()