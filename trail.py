import random
import pyautogui
import string

chars = string.printable
chars_list = list(chars)

password = pyautogui.password("enter password:")
guess_pass = ""

while (guess_pass != password):
    guess_pass = random.choices(chars_list, k=len(password))

    print("<======="+str(guess_pass)+"=======>")

    if (guess_pass== list(password)):
        print("your password is :"+"".join(guess_pass))
        break

