import helloWorld
import unittest


class Mytest(unittest.TestCase):
	def test_greeting(self):
		greeting = helloWorld.helloWorld()
		self.assertEqual(greeting, "Hello World!")

if __name__ == '__main__':
	unittest.main()