from helloUpperCase import UpperCase
import unittest

class Mytest(unittest.TestCase):
	def test_upperCase(self):
		username = UpperCase("pholisa")
		self.assertEqual(username, "Hello, PHOLISA")

if __name__ == '__main__':
	unittest.main()