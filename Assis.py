#Under working ____________________________________

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from time import sleep
# from webdriver_manager.firefox import Fire
from selenium.webdriver.common.by import By
import pathlib
import pyttsx3
import speech_recognition as sr
import warnings

# from Clap import MainClapExe
# MainClapExe()

warnings.simplefilter('ignore')


def speak(text):
    engine = pyttsx3.init()
    Id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
    engine.setProperty('voice', Id)
    print("")
    print(f"==> Jarvis AI : {text}")
    print("")
    engine.say(text=text)
    engine.runAndWait()


def speechrecognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)

    try:
        print("Recogizing....")
        query = r.recognize_google(audio, language="en")
        print(f"==> Shresth : {query}")
        return query.lower()

    except:
        return ""


ScriptDir = pathlib.Path().absolute()

url = "https://flowgpt.com/chat"

firefox_option = Options()
user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"
firefox_option.add_argument(f"user-agent={user_agent}")
firefox_option.add_argument('--profile-directory=Default')
firefox_option.add_argument("--headless=new")
firefox_option.add_argument(f'user-data-dir={ScriptDir}\\firefoxdata')
service = Service(FirefoxProfile().install())
driver = webdriver.Chrome(service=service, options=firefox_option)
driver.maximize_window()
driver.get(url=url)
# sleep(500)
ChatNumber = 3
def Checker():
    global ChatNumber
    for i in range(1, 1000):
        if i % 2 != 0:
            try:
                ChatNumber = str(i)
                Xpath = f"/html/body/div[1]/main/div[3]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[{ChatNumber}]/div/div/div/div[1]"
                driver.find_element(by=By.XPATH, value=Xpath)

            except:
                print(f"The next chatnumber is : {i}")
                ChatNumber = str(i)
                break


def Websiteopener():
    while True:
        try:
            xPATH = '/html/body/div[1]/main/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/textarea'
            driver.find_element(by=By.XPATH, value=xPATH)
            break

        except:
            pass


def SendMessage(Query):
    xPATH = '/html/body/div[1]/main/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/textarea'
    driver.find_element(by=By.XPATH, value=xPATH).send_keys(Query)
    sleep(0.5)
    Xpath2 = '/html/body/div[1]/main/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/button'
    driver.find_element(by=By.XPATH, value=Xpath2).click()


def Resultscrapper():
    global ChatNumber
    ChatNumber = str(ChatNumber)
    Xpath = f"/html/body/div[1]/main/div[3]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[{ChatNumber}]/div/div/div/div[1]"
    Text = driver.find_element(by=By.XPATH, value=Xpath).text
    ChatNumberNew = int(ChatNumber) + 2
    ChatNumber = ChatNumberNew
    return Text


def waitfortheanswer():
    sleep(2)
    Xpath = '/html/body/div[1]/main/div[3]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/div/button'
    while True:
        try:
            driver.find_element(by=By.XPATH, value=Xpath)
        except:
            break


Websiteopener()
Checker()

while True:
    Query = speechrecognition()
    if len(str(Query)) < 3:
        pass

    elif Query == None:
        pass

    else:
        SendMessage(Query=Query)
        waitfortheanswer()
        Text = Resultscrapper()
        speak(Text)
