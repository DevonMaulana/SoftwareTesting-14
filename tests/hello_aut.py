import unittest, sys
from selenium import webdriver
from selenium.webdriver.common.by import By

class AutTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors=yes')
        server = 'http://localhost:4444'
        self.browser = webdriver.Remote(command_executor=server, options=options)
        self.addCleanup(self.browser.quit)

    def test_homepage(self):
        # Menerima parameter URL dinamis yang dikirim dari workflow GitHub Actions
        if len(sys.argv) > 1:
            url = sys.argv[1]
        else:
            url = "http://localhost"
        
        self.browser.get(url)
        
        # Mengambil tangkapan layar untuk bukti pengujian nanti
        self.browser.save_screenshot('tests/screenshot.png')
        
        # Validasi teks fungsional pada halaman web
        expected_result = "Welcome back, Guest!"
        actual_result = self.browser.find_element(By.TAG_NAME, 'p')
        self.assertIn(expected_result, actual_result.text)

if __name__ == '__main__':
    # Parameter argv ditambahkan agar unittest tidak bingung dengan argumen URL dari GitHub Actions
    unittest.main(argv=['first-arg-is-ignored'], verbosity=2, warnings='ignore')