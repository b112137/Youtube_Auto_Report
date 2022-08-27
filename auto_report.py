from selenium import webdriver
import time
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QRadioButton, QButtonGroup, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import random


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5'
        self.left = 100
        self.top = 100
        self.width = 450
        self.height = 200
        self.initUI()
        self.start_value = True
        self.choice = ""
        self.random_list = ["ONCE!", "TWICE!", "GOOD JOB!", "TALK THAT TALK", "LIKE OOH AHH", "CHEER UP", "TT", 
        "KNOCK KNOCK", "SIGNAL", "LIKEY", "HEART SHAKER", "WHAT IS LOVE?", "DANCE THE NIGHT AWAY", "YES OR YES", 
        "FANCY", "FEEL SPECIAL", "MORE & MORE", "I CANT STOP ME", "Alcohol-Free", "SCIENTIST", "ONE IN A MILLION", "21:29", "LOVELY",
        "0", "1", "2","3","4","5","6","7","8","9","10","20151020","20160505","20220712","20220826","20220624"]

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.myradiobutton1 = QRadioButton('不請自來的廣告或垃圾留言', self)
        self.myradiobutton1.move(260,15)
        self.myradiobutton1.resize(170,25)

        self.myradiobutton2 = QRadioButton('色情或煽情露骨的留言', self)
        self.myradiobutton2.move(260,35)
        self.myradiobutton2.resize(170,25)

        self.myradiobutton3 = QRadioButton('虐待兒童', self)
        self.myradiobutton3.move(260,55)
        self.myradiobutton3.resize(170,25)

        self.myradiobutton4 = QRadioButton('仇恨言論或血腥暴力的內容', self)
        self.myradiobutton4.move(260,75)
        self.myradiobutton4.resize(170,25)

        self.myradiobutton5 = QRadioButton('宣傳恐怖主義', self)
        self.myradiobutton5.move(260,95)
        self.myradiobutton5.resize(170,25)

        self.myradiobutton6 = QRadioButton('騷擾或霸凌內容', self)
        self.myradiobutton6.move(260,115)
        self.myradiobutton6.resize(170,25)

        self.myradiobutton7 = QRadioButton('自殺或自殘', self)
        self.myradiobutton7.move(260,135)
        self.myradiobutton7.resize(170,25)
        
        self.myradiobutton8 = QRadioButton('不實資訊', self)
        self.myradiobutton8.move(260,155)
        self.myradiobutton8.resize(170,25)

        self.myradiobutton4.setChecked(True)

        self.buttongroup1 = QButtonGroup(self)
        self.buttongroup1.addButton(self.myradiobutton1, 1)
        self.buttongroup1.addButton(self.myradiobutton2, 2)
        self.buttongroup1.addButton(self.myradiobutton3, 3)
        self.buttongroup1.addButton(self.myradiobutton4, 4)
        self.buttongroup1.addButton(self.myradiobutton5, 5)
        self.buttongroup1.addButton(self.myradiobutton6, 6)
        self.buttongroup1.addButton(self.myradiobutton7, 7)
        self.buttongroup1.addButton(self.myradiobutton8, 8)


        self.textLabel = QLabel(self)
        self.textLabel.setText("Account")
        self.textLabel.move(40,40)

        self.account_box = QLineEdit(self)
        self.account_box.move(90, 42)
        self.account_box.resize(150,25)

        self.textLabel = QLabel(self)
        self.textLabel.setText("Password")
        self.textLabel.move(40,80)

        self.password_box = QLineEdit(self)
        self.password_box.move(90, 82)
        self.password_box.resize(150,25)


        self.report = QPushButton('自動檢舉', self)
        self.report.move(38,122)
        self.report.clicked.connect(self.on_click_report)

        self.reply = QPushButton('自動倒讚回覆', self)
        self.reply.move(141,122)
        self.reply.clicked.connect(self.on_click_reply)

        self.textLabel = QLabel(self)
        self.textLabel.setText("回覆內容")
        self.textLabel.move(38,165)
        

        self.reply_text = QLineEdit(self)
        self.reply_text.move(90,167)
        self.reply_text.resize(80,25)
        self.reply_text.setText("Be kind!")

        self.dislike = QCheckBox('倒讚功能', self)
        self.dislike.move(175,155)
        self.random = QCheckBox('留言隨機穿插', self)
        self.random.move(175,175)
        self.random.setChecked(True)

        self.show()
    @pyqtSlot()
    def on_click_reply(self):
        self.random_list.append(self.reply_text.text())
        self.start_value = True
        browser = webdriver.Chrome('./chromedriver')
        browser.maximize_window()

        browser.get('https://accounts.google.com')
        browser.find_element_by_xpath('//*[@id="identifierId"]').send_keys(self.account_box.text())
        browser.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(self.password_box.text())
        browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()

        browser.get('https://www.youtube.com/watch?v=k6jqx9kZgPM')
        time.sleep(2)
        for i in range(2):
            browser.execute_script("window.scrollTo(0, 1000);")
            time.sleep(1)
        time.sleep(1)

        while self.start_value:
            try:
                button = browser.find_element_by_id("sort-menu").find_element_by_id("label")
                browser.execute_script("arguments[0].click();", button)

                time.sleep(1)
                button = browser.find_element_by_id("menu").find_element_by_xpath("//div[text()='由新到舊']")
                browser.execute_script("arguments[0].click();", button)
                time.sleep(2)

                comment_all = browser.find_element_by_id("comments").find_elements_by_id("comment")

                for comment_div in comment_all:
                    try:
                        text = comment_div.find_element_by_id("content-text").text
                        emoji = comment_div.find_element_by_id("content-text").find_elements_by_class_name("emoji")
                        
                        same_check = False
                        if len(text) > 5:
                            same_check = True
                            for i in range(len(text)):
                                if i != 0:
                                    if text[i] != text[i-1]:
                                        same_check = False
                                        break

                        text_len = len(text)
                        emoji_len = len(emoji)

                        print(text_len, emoji_len)

                        if emoji_len > 15 or same_check:
                            print("bad.")
                            if self.dislike.isChecked():
                                comment_div.find_element_by_id("dislike-button").click()
                                time.sleep(0.5)
                            comment_div.find_element_by_id("reply-button-end").click()
                            time.sleep(1)

                            comment_div.find_element_by_id("contenteditable-root").click()
                            time.sleep(0.5)

                            if self.random.isChecked():
                                reply_text = self.random_list[random.randint(0, len(self.random_list)-1)]
                                comment_div.find_element_by_id("contenteditable-root").send_keys(reply_text)
                            else:
                                comment_div.find_element_by_id("contenteditable-root").send_keys(self.reply_text.text())
                            time.sleep(0.5)

                            comment_div.find_element_by_id("submit-button").click()
                            time.sleep(2.5)
                    except:
                        break

                element = browser.find_element_by_id("sort-menu")
                browser.execute_script("arguments[0].scrollIntoView();", element)

            except:
                break

    @pyqtSlot()
    def on_click_report(self):
        if self.buttongroup1.checkedId() == 1:
            self.choice = self.myradiobutton1.text()
        elif self.buttongroup1.checkedId() == 2:
            self.choice = self.myradiobutton2.text()
        elif self.buttongroup1.checkedId() == 3:
            self.choice = self.myradiobutton3.text()
        elif self.buttongroup1.checkedId() == 4:
            self.choice = self.myradiobutton4.text()
        elif self.buttongroup1.checkedId() == 5:
            self.choice = self.myradiobutton5.text()
        elif self.buttongroup1.checkedId() == 6:
            self.choice = self.myradiobutton6.text()
        elif self.buttongroup1.checkedId() == 7:
            self.choice = self.myradiobutton7.text()
        elif self.buttongroup1.checkedId() == 8:
            self.choice = self.myradiobutton8.text()
        else:
            self.choice = self.myradiobutton4.text()
        print(self.choice)

        self.start_value = True
        browser = webdriver.Chrome('./chromedriver')
        browser.maximize_window()

        browser.get('https://accounts.google.com')
        browser.find_element_by_xpath('//*[@id="identifierId"]').send_keys(self.account_box.text())
        browser.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()
        time.sleep(5)
        browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(self.password_box.text())
        browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()

        browser.get('https://www.youtube.com/watch?v=k6jqx9kZgPM')
        time.sleep(2)
        for i in range(2):
            browser.execute_script("window.scrollTo(0, 1000);")
            time.sleep(1)
        time.sleep(1)

        while self.start_value:
            try:

                button = browser.find_element_by_id("sort-menu").find_element_by_id("label")
                browser.execute_script("arguments[0].click();", button)

                time.sleep(1)
                button = browser.find_element_by_id("menu").find_element_by_xpath("//div[text()='由新到舊']")
                browser.execute_script("arguments[0].click();", button)
                time.sleep(2)

                comment_all = browser.find_element_by_id("comments").find_elements_by_id("comment")

                for comment_div in comment_all:
                    try:
                        text = comment_div.find_element_by_id("content-text").text
                        emoji = comment_div.find_element_by_id("content-text").find_elements_by_class_name("emoji")
                        
                        same_check = False
                        if len(text) > 5:
                            same_check = True
                            for i in range(len(text)):
                                if i != 0:
                                    if text[i] != text[i-1]:
                                        same_check = False
                                        break

                        text_len = len(text)
                        emoji_len = len(emoji)

                        print(text_len, emoji_len)

                        if emoji_len > 15 or same_check:
                            print("bad.")
                            comment_div.find_element_by_id("action-menu").find_element_by_id("button").click()
                            browser.find_element_by_xpath("//yt-formatted-string[text()='檢舉']").click()
                            time.sleep(1)
                            browser.find_element_by_xpath("//yt-formatted-string[text()='" + self.choice + "']").click()
                            time.sleep(1)
                            browser.find_element_by_id("submit-button").click()
                            time.sleep(1)
                            browser.find_element_by_id("confirm-button").click()
                            time.sleep(0.5)
                    except:
                        break

                element = browser.find_element_by_id("sort-menu")
                browser.execute_script("arguments[0].scrollIntoView();", element)

            except:
                break

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())