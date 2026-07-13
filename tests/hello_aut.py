import unittest, sys, os
from selenium import webdriver
from selenium.webdriver.common.by import By

class AutTest(unittest.TestCase):
    def setUp(self):
        # Mengambil tipe browser dari GitHub Actions (jika kosong, default ke firefox)
        self.browser_type = os.environ.get('BROWSER_TYPE', 'firefox').lower()
        
        if self.browser_type == 'chrome':
            options = webdriver.ChromeOptions()
        elif self.browser_type == 'edge':
            options = webdriver.EdgeOptions()
        else:
            options = webdriver.FirefoxOptions()

        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors=yes')
        server = 'http://localhost:4444'
        self.browser = webdriver.Remote(command_executor=server, options=options)
        self.addCleanup(self.browser.quit)

    def test_homepage(self):
        if len(sys.argv) > 1:
            url = sys.argv[1]
        else:
            url = "http://localhost"
        
        self.browser.get(url)
        
        # Penamaan screenshot dibuat unik sesuai nama browsernya
        self.browser.save_screenshot(f'tests/screenshot_{self.browser_type}.png')
        
        expected_result = "Welcome back, Guest!"
        actual_result = self.browser.find_element(By.TAG_NAME, 'p')
        self.assertIn(expected_result, actual_result.text)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, warnings='ignore')