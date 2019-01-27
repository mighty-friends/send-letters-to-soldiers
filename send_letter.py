import bridge

# 편지를 보내고자 하는 사람의 사단/연대 카페에 가입해야 합니다. 또한 경우에 따라 코드의 변경이 필요합니다.

id = 'your_id'
password = 'your_password'

title = "TEST"
content = '''이것은 편지 보내기 프로그램의 TEST입니다.
이 편지가 무사히 보내진다면 앞으로 다양한 사람들이 이 계정을 사용하게 될 수 있으므로 보내는 실질적 사람이 '서재현'이 아닐 수 있습니다.
또한 뉴스 같은 내용을 크롤링하여 대량 발송할 수 있으므로 원치 않는다면 편지로 알려주세요.
건승을 빕니다.'''

driver = bridge.init(True)
bridge.login(driver, id, password)
bridge.send(driver, title, content)
bridge.quit()

