# -*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    """docstring for NewVisitorTest"""

    def setUp(self):
        self.brower = webdriver.Firefox()
        self.brower.implicitly_wait(30)  # selenium 常用方法

    def tearDown(self):
        self.brower.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.brower.get('http://localhost:8000')
        self.assertIn('To-Do', self.brower.title)
        header_text = self.brower.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.brower.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),
                         'Enter a to-do item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)

        table = self.brower.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1:Buy peacock feathers' for row in rows),
                        "New to-do item did not appear in table")
        self.fail('Finish the Test!', header_text)

if __name__ == '__main__':
    unittest.main()
