import pyautogui
import time
import string
import random

def rand_id(length):
    caracteres = string.digits
    return ''.join(random.choice(caracteres) for i in range(length))

def run_automation ():
# show desktop
    pyautogui.hotkey('win', 'd')
    time.sleep(1)  

    # find google chrome image icon
    googleChrome = pyautogui.locateCenterOnScreen('googlechrome.png', confidence=0.7)

    # click on google chrome icon
    pyautogui.doubleClick(googleChrome.x, googleChrome.y)

    #open anon tab
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'shift', "n")

    # write roblox and go to site
    pyautogui.write("https://www.roblox.com/pt")
    pyautogui.hotkey("enter")

    pyautogui.press('f11')

    # choose data
    time.sleep(4)
    pyautogui.click(x=200, y=200)
    pyautogui.press('tab')
    pyautogui.press('down', presses=10, interval=0.1)

    # choose month
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.press('down', presses=10, interval=0.1)

    #choose year
    pyautogui.press('tab')
    pyautogui.press('down', presses=20, interval=0.1)

    # password & username input
    rand = rand_id(5)
    rand_pass = "randomizePassword"
    pyautogui.press('tab')
    pyautogui.write("mitigasao" + rand)

    # copy username
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('ctrl', 'c')
    pyautogui.hotkey('win', 'd')

    # search notepad and click
    notepad = pyautogui.locateCenterOnScreen('notepad.png', confidence=0.7)
    pyautogui.doubleClick(notepad.x, notepad.y)
    time.sleep(3)
    pyautogui.press('pagedown')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("enter")

    # insert password 
    pyautogui.hotkey('alt', 'tab')
    pyautogui.press('tab')
    pyautogui.write(rand_pass)
    time.sleep(1)

    # choose gender
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")

    # sign up
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("tab")
    pyautogui.press("enter")

    time.sleep(10)

    # locate settings icon roblox and quit
    settings = pyautogui.locateCenterOnScreen('settings.png', confidence=0.6)
    pyautogui.click(settings.x, settings.y)

    for i in range(5):
        pyautogui.press("tab")

    pyautogui.press("enter")
    time.sleep(5)

    # click accept risks
    risks = pyautogui.locateCenterOnScreen('risks.png', confidence=0.6)
    pyautogui.click(risks.x, risks.y)

    # close google chrome tab
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'w')

    pyautogui.hotkey('alt', 'f4')

    # close last chrome page
    pyautogui.hotkey('alt', 'tab')
    pyautogui.hotkey('ctrl', 'w')    
    print("script rodou em", time.ctime())


while True:
    run_automation()
    wait_time = 14*60
    print("aguardando", wait_time/60, "minutos para a próxima execução")
    time.sleep(wait_time)