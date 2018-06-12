### Download Selenium web driver into env/bin folder
from selenium import webdriver

#options = webdriver.ChromeOptions()
#options.add_argument('--ignore-certificate-errors')
#options.add_argument('--test-type')
#options.binary_location = ('chromedriver')
#driver = webdriver.Chrome(chrome_options = options)
browser = webdriver.Chrome()
browser.get('http://localhost:8000')
assert 'Django' in browser.title
