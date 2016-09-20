from numberList import number_list
import unittest

class Mytest(unittest.TestCase):
	def test_numberList(self):
		result = number_list(5)
		newArray = [1,2,3,4,5]
		self.assertEqual(newArray, result)

if __name__ == '__main__':
	unittest.main()
