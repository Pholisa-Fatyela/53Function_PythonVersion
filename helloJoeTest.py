from helloJoe import hello_joe
import unittest

class Mytest(unittest.TestCase):
	def test_helloJoe(self):
		username = hello_joe("pholisa")
		username2 = hello_joe("joe")
		self.assertEqual(username, "Hello, pholisa!")
		self.assertEqual(username2, "Hello!")

if __name__ == '__main__':
	unittest.main()