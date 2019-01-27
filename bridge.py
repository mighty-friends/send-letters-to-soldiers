from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def init(isHeadless):
	chrome_options = webdriver.ChromeOptions()
	
	if isHeadless:
		chrome_options.add_argument('--headless')
	
	driver = webdriver.Chrome(chrome_options=chrome_options)
	driver.implicitly_wait(3)
	
	return driver

def login(driver, email, password):
	driver.get('https://www.thecamp.or.kr/pcws/common/loginView.do')	
	driver.find_element_by_name('loginUserId').send_keys(email)
	driver.find_element_by_name('loginUserPassword').send_keys(password)
	driver.find_element_by_xpath("//div[@class='input_4']/button").click()
	
def send(driver, title, content):	
	# 사단 선택
	driver.find_element_by_xpath("//div[@id='leftMyGroupListDiv']/a[@class='present_selected']").click()
	driver.find_element_by_xpath("//div[@id='leftMyGroupSelectDiv']/a[@group_id='934'][@unit_code='6142027'][@school_type='1']").click()

	# 위문편지
	element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//img[@alt='위문편지 쓰기']")))
	element.click()

	# 제목, 내용 입력
	driver.find_element_by_xpath("//input[@class='letter_post_foot'][@id='title']").send_keys(title)
	driver.find_element_by_xpath("//textarea[@id='contents']").send_keys(content)

	# 전송
	driver.find_element_by_xpath("//div[@class='post_btn']/button[@id='btnWrite']").click()
	driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']").find_element_by_tag_name('button').click()
	driver.find_element_by_xpath("//div[@class='ui-dialog-buttonset']/button").click()
	
def quit(driver):
	driver.quit()