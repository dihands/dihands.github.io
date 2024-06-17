import subprocess as sub
import pyfiglet 
import pyautogui as auto
import datetime

# Display the text using pyfiglet
# text = fi.figlet_format("Dark   S")
# print(text)
# Function to print figlet text in color





def print_color_figlet(text, color):
    figlet_text = pyfiglet.figlet_format(text)

    # ANSI escape codes for colors
    color_code = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'purple': '\033[95m',
        'cyan': '\033[96m',
        'white': '\033[97m'
    }

    # Reset ANSI escape code
    reset_code = '\033[0m'

    # Print each line of figlet text with color
    for line in figlet_text.splitlines():
        print(color_code.get(color.lower(), '\033[97m') + line + reset_code)

# Example usage
if __name__ == "__main__":
    text = "Dark  S"
    color = "purple" 
    print_color_figlet(text, color)














def open_terminal():
    auto.hotkey('ctrl', 'alt', 't')

def ping_address():
    e = input("Enter Domain Name: ")
    sub.run(["ping", e])
def auto_massage():
    while True:
        auto.typewrite("Hello, I am Dark S")
        auto.press("enter")
def time_a():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_time)
                

def main():
    while True:
        # Command input
        c = input("$ ")

        if c in ("exit", "quit"):
            print("Exit...")
            break
        elif c in ("terminal"):
            open_terminal()
        elif c in ("ping"):
            ping_address()
        elif c in ("aM"):
            auto_massage()
        elif c in ("time"):
            time_a()
            
                
            
            
            
            
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()









