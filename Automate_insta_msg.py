from matplotlib.pyplot import text
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
        self.bot.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
        time.sleep(1)

    def sendMessage(self):
        
        # enters the username
        self.bot.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/input').send_keys(users)  #send_keys is used to send some data 
        time.sleep(4)

        # click on username
        self.bot.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div[3]/button').click()  # where as click is used to click 
        time.sleep(1)

        # click on next
        self.bot.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/button').click()
        time.sleep(1)

        # click on message area
        send = self.bot.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        
        for j in range(number):  # to send a msg a number of times
                send.send_keys(self.message)
                # time.sleep(1)

                send.send_keys(Keys.RETURN)  #Keys.RETURN is the keyboard enter button
                # time.sleep(1)

        # pencil/new message button
        self.bot.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/section/div/div[2]/div/div/div[1]/div[1]/div/div[3]/button').click()
        time.sleep(1)


class gui:
    root = Tk()

    def __init__(self):

        self.root.title("Auto Insta") #the name of the window

        self.root.geometry("1280x720")  #just to give a size
        # sender username 
        lbl1 = Label(self.root, text = "Enter your username:   ").grid()
        usernameInput = Entry(self.root, width = 35)
        usernameInput.grid(column =1, row =0)
        # user password
        lbl2 = Label(self.root, text = "Enter your password:   ").grid(column=0, row=1)
        passwordInput = Entry(self.root, width = 35, show= "*")
        passwordInput.grid(column = 1, row = 1)
        # receiver username
        lbl3 = Label(self.root, text = "Enter username you want to send to :   ").grid(column=0, row=2)
        usersInput = Entry(self.root, width = 35)
        usersInput.grid(column = 1, row = 2)
        # number of times to send the message
        lbl5 = Label(self.root, text = "Enter the number of times to send the message:   ").grid(column=0, row=3)
        numberInput = Entry(self.root, width = 35)
        numberInput.grid(column = 1, row = 3)
        # message
        lbl4 = Label(self.root, text = "Enter the message:   ").grid(column=0, row=4)
        messageInput = Entry(self.root, width = 50)
        messageInput.grid(column = 1, row = 4)
        

        def clicked():
            global driver, username, password, users, message, number

            number = 1
            username = usernameInput.get()
            password = passwordInput.get()
            users = usersInput.get()        # Users which you want to send message to 
            message = messageInput.get()    # Enter the message you want to send
            number = int(numberInput.get())

            driver = webdriver.Chrome(ChromeDriverManager().install())

            self.root.destroy()
            
        btn = Button(self.root, text = "Send", fg = "blue", bg = "gray", command=clicked)
        btn.grid(column = 0, row = 5)

        self.root.mainloop()


gui()


bot(username, password, users, message)

input("DONE")

