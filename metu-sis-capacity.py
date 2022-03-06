import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from functions import scroll, is_there_empty_chair, find_course, play_music

file_path = 'C:/Users/Legion/Desktop/Python/selenium-metu-sis/warning.mp3'

def metu_course_capacity_questioning(url, course_code):

    s = Service('C:/Users/Legion/Desktop/Python/geckodriver-v0.30.0-win64/geckodriver.exe')
    driver = webdriver.Firefox(service=s)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)

    columns_button = driver.find_element(By.CSS_SELECTOR, ".btn-group")
    driver.implicitly_wait(10)
    time.sleep(3)
    columns_button.click()

    scroll(driver)

    capacity = driver.find_element(By.XPATH, "//*[@id='SearchResults_column_toggler']/label[13]")
    used_capacity = driver.find_element(By.XPATH, "//*[@id='SearchResults_column_toggler']/label[14]")
    driver.implicitly_wait(10)
    capacity.click()
    used_capacity.click()

    # close columns section
    columns_button.click()

    records_per_page = driver.find_element(By.ID, "s2id_autogen4")
    driver.implicitly_wait(10)
    records_per_page.click()

    records_per_page_elements = driver.find_elements(By.CSS_SELECTOR, ".select2-result-label")
    show_all_button = records_per_page_elements[3]
    show_all_button.click()

    scroll(driver)
     
    courses = find_course(driver, course_code)

    for course in courses:
        results = is_there_empty_chair(course)
        if results[1]: 
            print(results[0])
            play_music(file_path)
    
if __name__ == "__main__":
    
    url_ee = "https://sis.metu.edu.tr/get.php?package=I0oVOF5fGqPn2HT2oK7dqD3NEfGk351-WCU4vddDFBZ5fqO5zHQf5lcLL_s70FniHLSrs6qnxpgp61Vuqu0_Yg#/?selectSemester=20212&selectProgram=567&submitSearchForm=Search&stamp=ddkd2XBH4hPEeWn6bQ9x_qWPVTug33AG-oU6vNN68XJD_xmG416j5wAA8LkKyrGkukXGHhwsvKXWUwnsMPrpyg"
    url_486 = "https://sis.metu.edu.tr/get.php?package=I0oVOF5fGqPn2HT2oK7dqD3NEfGk351-WCU4vddDFBZ5fqO5zHQf5lcLL_s70FniHLSrs6qnxpgp61Vuqu0_Yg#/?selectSemester=20212&selectProgram=460&submitSearchForm=Search&stamp=RzGYhMejUjYw8Azib2EeZWcGblUaacxj10CAIeBNLl5eSxZX2cZtihl2ZLtrDwO7S8jXSRzJRHnX7cJcmKQ4sg"
    metu_course_capacity_questioning(url_ee, course_code=5670312)
    metu_course_capacity_questioning(url_486, course_code=4600486)