## - Use: pip install pyautogui
import pyautogui
import time

count = 0
pyautogui.click(10,5)
while True:
    pyautogui.FAILSAFE=True
    pyautogui.write(f"Hey you there viser naaye")
    count +=1
    pyautogui.press("ENTER")
    time.sleep(1)

## - This is a WhatsApp spamming tool developed By Saadh Jawwadh
## - Reference Larymak