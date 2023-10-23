import os
import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import random

# path = current file folder
PATH = os.path.dirname(os.path.realpath(__file__))


def setNameList():
    with open(PATH + '/namelist.json') as f:
        namelist = json.load(f)
    return namelist
nameList = setNameList()

def getFakeName():
    # random based on length of nameList
    name = random.randint(0, len(nameList)-1)
    # get name from nameList
    nameR = nameList[name]
    # remove name from nameList
    nameList.pop(name)
    # write new nameList to namelist.json
    with open(PATH + '/namelist2.json', 'w') as f:
        json.dump(nameList, f)
    return nameR

def getUmur():
    # umur = random.randint(18, 22)
    umur = random.randint(18, 22)
    return umur

def getUnivAndProdi():
    with open(PATH + '/univlist.json') as f:
        univAndProdi = json.load(f)
    # random based on length of univAndProdi
    prob = [50, 25, 25]
    options = {
        0: prob[0],
        1: prob[1],
        2: prob[2]
    }
    univ = randomizer(prob, options)
    univName = univAndProdi[univ][0]


    # random based on length of prodi
    if univ == 0:
        # 4
        prob = [70, 20, 5, 5]
        options = {
            0: prob[0],
            1: prob[1],
            2: prob[2],
            3: prob[3],
        }
    elif univ == 1:
        # 10
        prob = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
        options = {
            0: prob[0],
            1: prob[1],
            2: prob[2],
            3: prob[3],
            4: prob[4],
            5: prob[5],
            6: prob[6],
            7: prob[7],
            8: prob[8],
            9: prob[9]
        }
    elif univ == 2:
        prob = [17, 17, 17, 16, 17, 16]
        options = {
            0: prob[0],
            1: prob[1],
            2: prob[2],
            3: prob[3],
            4: prob[4],
            5: prob[5]
        }

    prodi = randomizer(prob, options)
    prodiName = univAndProdi[univ][1][prodi]
    # prodi = random.randint(0, len(univAndProdi[univ][1])-1)
    # prodiName = univAndProdi[univ][1][prodi]
    return univName, prodiName

def randomizer(prob, options):
    rand = random.randint(1, 100)
    threshold = 0
    for option, probability in options.items():
        threshold += probability
        if rand <= threshold:
            return option
    return 0


def getAnswer5Option(index):
    if index == 0:
        prob = [5, 15, 30, 30, 20]
    elif index == 1:
        prob = [10, 20, 30, 30, 10]
    elif index == 2:
        prob = [20, 30, 30, 15, 5]
    elif index == 3:
        prob = [5, 15, 40, 30, 10]
    elif index == 4:
        prob = [10, 20, 40, 20, 10]
    elif index == 5:
        prob = [5, 15, 60, 15, 5]
    elif index == 6:
        prob = [10, 20, 40, 20, 10]
    elif index == 7:
        prob = [5, 15, 40, 30, 10]

    options = {
        0: prob[0],
        1: prob[1],
        2: prob[2],
        3: prob[3],
        4: prob[4]
    }
    rand = random.randint(1, 100)
    threshold = 0
    for option, probability in options.items():
        threshold += probability
        if rand <= threshold:
            return option
    return 0

def getAnswerDown(index):
    if index == 0:
        prob = [80, 20]
        options = {
            0: prob[0],
            1: prob[1]
        }
    elif index == 1:
        prob = [20, 30, 50]
        options = {
            0: prob[0],
            1: prob[1],
            2: prob[2]
        }
    elif index == 2:
        prob = [35, 65]
        options = {
            0: prob[0],
            1: prob[1]
        }
    elif index == 3:
        prob = [20, 50, 30]
        options = {
            0: prob[0],
            1: prob[1],
            2: prob[2]
        }
    elif index == 4:
        prob = [70, 30]
        options = {
            0: prob[0],
            1: prob[1]
        }


    return randomizer(prob, options)


def openBrowser():
    # open browser

    # back one folder
    path = os.path.dirname(PATH)
    chrome_driver_path = path + '/chromedriver_win32/chromedriver.exe'
    service = Service(chrome_driver_path)
    service.start()
    driver = webdriver.Chrome(service=service)
    return driver

def main():
    driver = openBrowser()
    for i in range(len(setNameList())):
        link = "https://docs.google.com/forms/d/e/****************************"
        driver.get(link)
        time.sleep(2)


        # +========+
        # | page 1 |
        # +========+

        # Xb9hP
        page1form = driver.find_elements(By.CLASS_NAME, "whsOnd")
        print(len(page1form))
        ans1 = getFakeName()
        ans2 = getUmur()
        ans3, ans4 = getUnivAndProdi()
        print(ans3)
        print(ans4)
        print(ans1)
        page1form[0].send_keys(ans1)
        page1form[1].send_keys(ans3)
        page1form[2].send_keys(ans4)
        page1form[3].send_keys(ans2)
        # NPEfkd 1st class is submit button
        nextButton = driver.find_elements(By.CLASS_NAME, "NPEfkd")[0]
        nextButton.click()
        time.sleep(2)

        # +========+
        # | page 2 |
        # +========+

        # 5 options question
        # N9Qcwe
        page2form5q = driver.find_elements(By.CLASS_NAME, "N9Qcwe")
        print(len(page2form5q))
        # SG0AAe
        page2formdown = driver.find_elements(By.CLASS_NAME, "SG0AAe")
        print(len(page2formdown))


        for i in range(len(page2form5q)):
            ans = getAnswer5Option(i)
            # print(ans)
            # T5pZmf
            options = page2form5q[i].find_elements(By.CLASS_NAME, "T5pZmf")
            # d7L4fc
            options[ans].find_element(By.CLASS_NAME, "d7L4fc").click()

        for i in range(len(page2formdown)):
            ans = getAnswerDown(i)
            print(str(i) + ". " + str(ans))
            # bzfPab 
            options = page2formdown[i].find_elements(By.CLASS_NAME, "bzfPab")
            options[ans].click()

        # Y5sE8d
        nextButton = driver.find_elements(By.CLASS_NAME, "Y5sE8d")[0]
        nextButton.click()

    time.sleep(20)

if __name__ == '__main__':
    main()
    