# -*-coding:utf-8-*-
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    """docstring for NewVisitorTest"""

    def setUp(self):
        self.brower = webdriver.Firefox()
        self.brower.implicitly_wait(3)  # selenium 常用方法

    def tearDown(self):
        self.brower.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.brower.get('http://localhost:8000')
        self.assertIn('To-Do', self.brower.title)
        self.fail('Finish the Test!')

if __name__ == '__main__':
    unittest.main()
