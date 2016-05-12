from selenium import webdriver
brower = webdriver.Firefox()
brower.get('http://localhost:8000')
assert 'Django' in brower.title

class SmokeTest(TestCase):
	"""docstring for SmokeTest"""
	'''
	def __init__(self, arg):
		super(SmokeTest, self).__init__()
		self.arg = arg
	'''
	def test_bad_maths(self):
		self.assertEqual(1+1,3)