from django.test import TestCase

# Create your tests here.
class SmokeTest(TestCase):
	"""docstring for SmokeTest"""
	'''
	def __init__(self, arg):
		super(SmokeTest, self).__init__()
		self.arg = arg
	'''
	def test_bad_maths(self):
		self.assertEqual(1+1,3)