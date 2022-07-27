from selenium import webdriver
import os
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import *
from tkinter import ttk
import pyautogui


root = Tk()

root.title("Auto Insta") #the name of the window

root.geometry("1280x720")  #just to give a size




users = ['']  # Add the users which you want to send message to 
message = "Hey"   # Enter the message you want to send

class bot:
    def __init__(self, username, password, user, message):  # in the example it was given audience but it should be user 

        self.username = username
        self.password = password
        self.user = user
        self.message = message
        self.base_url = 'https://www.instagram.com/'
        self.bot = driver
        self.login()
        self.sendMessage()

    def login(self):
        
        self.bot.get(self.base_url)

        enter_username = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)

        enter_password = WebDriverWait(self.bot, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)

        enter_password.send_keys(Keys.RETURN)
        time.sleep(4)

        # turn on notifications popup
        self.bot.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]').click()  
                            # /html/body/div[5]/div/div/div/div[3]/button[2]   xpath for not now        

                            # /html/body/div[5]/div/div/div/div[3]/button[1]   xpath for turn on
        time.sleep(1)

        # the anchor element has to be selected and not just the svg           
        x_mesenger ='/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a'             #  mesenger xpath
        # x_DM = '//*[@id="react-root"]/section/div/div[1]/div/div[3]/div/div[2]/a/svg'                  #  dm xpaths this is the old instagram xpath 
        self.bot.find_element_by_xpath(x_mesenger).click()   # depending on the account choose xpaths default/NewUser is of DM xpath            
        time.sleep(2)

        # pencil/new message button  
        # ---------------------not working fromn here -------------------
        self.bot.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button/div').click()
        time.sleep(1)

    def sendMessage(self):
        for i in users:
            # enters the username
            self.bot.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[1]/div/div[2]/input').send_keys(i)  #send_keys is used to send some data 
            time.sleep(1)

            # click on username
            self.bot.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/div[2]/div[1]/div').click()  # where as click is used to click 
            time.sleep(1)

            # click on username
            self.bot.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div[2]/div/button').click()
            time.sleep(1)

            # click on message area
            send = self.bot.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
            
            send.send_keys(self.message)
            time.sleep(1)

            send.send_keys(Keys.RETURN)  #Keys.RETURN is the keyboard enter button
            time.sleep(1)
            
            # pencil/new message button
            self.bot.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
            time.sleep(1)



lbl1 = Label(root, text = "Enter your username:   ")
lbl1.grid()


usernameInput = Entry(root, width = 35)
usernameInput.grid(column =1, row =0)

lbl2 = Label(root, text = "Enter your password:   ").grid(column=0, row=1)

passwordInput = Entry(root, width = 35)
passwordInput.grid(column =1, row =1)

def clicked():
    global driver, username, password

    username = usernameInput.get()    
    password = passwordInput.get()

    driver = webdriver.Chrome(ChromeDriverManager().install())

    root.destroy()

btn = Button(root, text = "Enter", fg = "blue", bg = "black", command=clicked)
btn.grid(column = 0, row = 2)


root.mainloop()

username = "shashaank213@gmail.com"
password = "aniso9001"


bot(username, password, users, message)

input("DONE")

