from selenium import webdriver
import time
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5'
        self.left = 100
        self.top = 100
        self.width = 300
        self.height = 200
        self.initUI()
        self.start_value = True
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
    
        self.textLabel = QLabel(self)
        self.textLabel.setText("Account")
        self.textLabel.move(50,40)

        self.account_box = QLineEdit(self)
        self.account_box.move(100, 42)
        self.account_box.resize(150,25)

        self.textLabel = QLabel(self)
        self.textLabel.setText("Password")
        self.textLabel.move(50,80)

        self.password_box = QLineEdit(self)
        self.password_box.move(100, 82)
        self.password_box.resize(150,25)

        self.start = QPushButton('START', self)
        self.start.move(48,122)
        self.start.clicked.connect(self.on_click_start)

        self.stop = QPushButton('STOP', self)
        self.stop.move(151,122)
        self.stop.clicked.connect(self.on_click_stop)

        self.show()
    @pyqtSlot()
    def on_click_stop(self):
        self.start_value = False

    @pyqtSlot()
    def on_click_start(self):
        self.start_value = True
        browser = webdriver.Chrome('./chromedriver')
        browser.maximize_window()

        browser.get('https://gmail.com')
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
                            browser.find_element_by_xpath("//yt-formatted-string[text()='不請自來的廣告或垃圾留言']").click()
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