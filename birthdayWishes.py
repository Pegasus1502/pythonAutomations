import pywhatkit
import pyautogui as pg



number = input("Enter Target Phone Number: ")
message = input("Enter Your Message: ")

print("Enter Which Time You Want To Send The Message,First Hours then Minutes \n")

hour =  int(input("Enter Hours: "))
min =  int(input("Enter Minutes: "))

# Send the birthday wish using pywhatkit
pywhatkit.sendwhatmsg(number, message, hour, min) 
pg.press('enter')




