import pyautogui, threading
global last
global startButton

last = None
startButton = pyautogui.locateOnScreen('target.png', confidence = 0.5, region = (400,0,1230,1000))

def SetLocation():
    while(1):
        try:
            startButton = pyautogui.locateOnScreen('target.png', confidence = 0.5, region = (400,0,1230,1000))

        except KeyboardInterrupt:
            break;
def findTarget():
    while(1):
        startButton = pyautogui.locateOnScreen('target.png', confidence = 0.4, region = (350,0,1150,840))
        if startButton != None:
            pyautogui.click(startButton[0], startButton[1])
            print(startButton)
#threading.Thread(target=SetLocation).start()
findTarget()
