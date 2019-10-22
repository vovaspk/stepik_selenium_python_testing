from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #push button
    button_submit = browser.find_element_by_class_name("btn-primary")      
    button_submit.click()
    #accept confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    #calculate formula
    num1 = browser.find_element_by_id("input_value").text
    ans = calc(num1)
    print(ans)

    #write answer
    answer_input = browser.find_element_by_id("answer")
    answer_input.send_keys(ans)

    #script 
    button_submit = browser.find_element_by_class_name("btn-primary")     
    button_submit.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
