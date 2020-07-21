from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class AddToCVTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_go_to_cv_page_and_add_to_the_education_section(self):

        self.browser.get('http://127.0.0.1:8000/admin/')

        username = self.browser.find_element_by_id('id_username')
        username.send_keys('Anandbir')

        password = self.browser.find_element_by_id('id_password')
        password.send_keys('HelloWorld99')

        password.send_keys(Keys.ENTER)

        time.sleep(3)

        self.browser.get('http://127.0.0.1:8000/cv/')

        self.assertIn('Anandbir\'s Website', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Anandbir\'s Website', header_text)

        button = self.browser.find_element_by_link_text("ADD TO EDUCATION SECTION")

        button.click()

        title = self.browser.find_element_by_id('id_title')
        title.send_keys('Post1')

        text = self.browser.find_element_by_id('id_text')
        text.send_keys('sample text')

        title.send_keys(Keys.ENTER)

        self.browser.get('http://127.0.0.1:8000/cv/')

        cvlist = self.browser.find_element_by_id('id_cv_list')
        rows = cvlist.find_elements_by_tag_name('p')
        self.assertTrue(
            any(row.text == 'sample text' for row in rows)
        )

    def test_can_go_to_cv_page_and_add_to_the_career_history_section(self):

        self.browser.get('http://127.0.0.1:8000/admin/')

        username = self.browser.find_element_by_id('id_username')
        username.send_keys('Anandbir')

        password = self.browser.find_element_by_id('id_password')
        password.send_keys('HelloWorld99')

        password.send_keys(Keys.ENTER)

        time.sleep(3)

        self.browser.get('http://127.0.0.1:8000/cv/')

        self.assertIn('Anandbir\'s Website', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Anandbir\'s Website', header_text)

        button = self.browser.find_element_by_link_text("ADD TO CAREER HISTORY SECTION")

        button.click()

        title = self.browser.find_element_by_id('id_title')
        title.send_keys('Post1')

        text = self.browser.find_element_by_id('id_text')
        text.send_keys('sample text')

        title.send_keys(Keys.ENTER)

        self.browser.get('http://127.0.0.1:8000/cv/')

        cvlist = self.browser.find_element_by_id('id_cv_list2')
        rows = cvlist.find_elements_by_tag_name('p')
        self.assertTrue(
            any(row.text == 'sample text' for row in rows)
        )

    def test_can_go_to_cv_page_and_add_to_the_skills_section(self):

        self.browser.get('http://127.0.0.1:8000/admin/')

        username = self.browser.find_element_by_id('id_username')
        username.send_keys('Anandbir')

        password = self.browser.find_element_by_id('id_password')
        password.send_keys('HelloWorld99')

        password.send_keys(Keys.ENTER)

        time.sleep(3)

        self.browser.get('http://127.0.0.1:8000/cv/')

        self.assertIn('Anandbir\'s Website', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Anandbir\'s Website', header_text)

        button = self.browser.find_element_by_link_text("ADD TO SKILLS SECTION")

        button.click()

        title = self.browser.find_element_by_id('id_title')
        title.send_keys('Post1')

        text = self.browser.find_element_by_id('id_text')
        text.send_keys('sample text')

        title.send_keys(Keys.ENTER)

        self.browser.get('http://127.0.0.1:8000/cv/')

        cvlist = self.browser.find_element_by_id('id_cv_list3')
        rows = cvlist.find_elements_by_tag_name('p')
        self.assertTrue(
            any(row.text == 'sample text' for row in rows)
        )


if __name__ == '__main__':
    unittest.main(warnings='ignore')