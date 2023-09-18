import pyautogui as pg
import webbrowser
import time

phone = input("Enter Target Phone Number: ")
text = input("Enter Your Message: ")
amount = int(input("Enter how many time you want to send Message: "))

webbrowser.open(f"https://web.whatsapp.com/send?phone={phone}&app_absent=0")

time.sleep(9) # wait for whatsapp web

for i in range (amount):
    pg.click()
    time.sleep(1)
    pg.write(text)
    pg.press("enter")