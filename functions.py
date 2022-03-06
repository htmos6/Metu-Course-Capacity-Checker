import time
from pygame import mixer
from selenium.webdriver.common.by import By

def scroll(driver):
    #javascript integrated code to python-selenium
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    match=False
    while(match==False):
        lastCount = lenOfPage
        time.sleep(3)
        lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
        if lastCount == lenOfPage:
            match=True
        time.sleep(3)

def find_course(driver, course_code):
    courses = driver.find_elements(By.XPATH, "//tr[td[contains(text(), {})]]".format(course_code))
    return courses

def is_there_empty_chair(course):
    sentence = course.text.split()
    result = str(sentence[2]+" "+" ".join(sentence[3:-5])+" "+"Section: "+sentence[-3]+" Capacity: "+str(int(sentence[-2]) - int(sentence[-1])))
    total_capacity = int(sentence[-2])
    used_capacity = int(sentence[-1])

    if total_capacity-used_capacity > 0:
        return [result,True]
    else:
        return [result,False]

def play_music(file_path):
    mixer.init()
    mixer.music.load(file_path)
    mixer.music.play()
    time.sleep(2)
