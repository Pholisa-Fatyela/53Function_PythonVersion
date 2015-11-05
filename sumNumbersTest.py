from sumNumbers import sum_numbers
import unittest

class Mytest(unittest.TestCase):
	def test_sum_numbers_for_3(self):
		sumList = sum_numbers(3)
		self.assertEqual(sumList, 6)

	def test_sum_numbers_for_7(self):
		sumList = sum_numbers(7)
		self.assertEqual(sumList, 28)

	def test_sum_numbers_for_20(self):
		sumList = sum_numbers(20)
		self.assertEqual(sumList, 210)

	def test_sum_numbers_for_0(self):
		sumList = sum_numbers(0)
		self.assertEqual(sumList, 0)

if __name__ == '__main__':
	unittest.main()
