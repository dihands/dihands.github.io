import subprocess as sub
import pyfiglet as fi 
import pyautogui as auto

text = fi.figlet_format("Dark   S")
print(text)



while True:
    #command input
    c = input("$ ")

    if c in ("terminal"):
        auto.hotkey('ctrl', 'alt', 't')
        
    elif c in ("ping"):
        e = input("name :")
        sub.run(["ping", e])
    elif c in ("exit","quit","break"):
        break
    if c in ("auto massage"):
        auto.typewrite("Hello, how are you?")
        auto.press("enter")


        
      
      
      
        
    # elif c in (""):    


