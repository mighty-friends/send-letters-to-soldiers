from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome()
driver.implicitly_wait(3)

id_ = 'your_id'
password = 'your_password'
# 편지를 보내고자 하는 사람의 사단? 연대? 카페에 가입해야 합니다. 또한 사단?에 따라 아래 코드의 변경이 필요합니다.

title = "TEST"
content = '''이것은 편지 보내기 프로그램의 TEST입니다.
이 편지가 무사히 보내진다면 앞으로 다양한 사람들이 이 계정을 사용하게 될 수 있으므로 보내는 실질적 사람이 '서재현'이 아닐 수 있습니다.
또한 뉴스 같은 내용을 크롤링하여 대량 발송할 수 있으므로 원치 않는다면 편지로 알려주세요.
건승을 빕니다.'''

# url에 접근한다.
driver.get('https://www.thecamp.or.kr/pcws/common/loginView.do')
driver.find_element_by_name('loginUserId').send_keys(id_)
driver.find_element_by_name('loginUserPassword').send_keys(password)

driver.find_element_by_xpath("//div[@class='input_4']/button").click()

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

driver.quit()
