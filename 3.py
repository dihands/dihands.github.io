import subprocess as sub
import pyautogui as auto
import datetime
import pyfiglet

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

# Function to open terminal
def open_terminal():
    auto.hotkey('ctrl', 'alt', 't')

# Function to ping an address
def ping_address():
    e = input("Enter Domain Name: ")
    sub.run(["ping", e])

# Function to send an automated message
def auto_message():
    while True:
        auto.typewrite("Hello, I am Dark S")
        auto.press("enter")

# Function to display current time
def display_time():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    print("Current Date and Time:", formatted_time)

# Function to scan network using nmap
def nmap_scan():
    target = input("Enter target IP or range: ")
    sub.run(["nmap", "-sP", target])

# Function to perform SQL injection using sqlmap
def sql_injection():
    url = input("Enter the URL to test: ")
    sub.run(["sqlmap", "-u", url])

# Function to audit wireless networks using wifite
def wifite_audit():
    sub.run(["wifite"])

# Main function to handle user commands
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
        elif c in ("am"):
            auto_message()
        elif c in ("time"):
            display_time()
        elif c in ("nmap"):
            nmap_scan()
        elif c in ("sqlmap"):
            sql_injection()
        elif c in ("wifite"):
            wifite_audit()
        else:
            print("Unknown command.")

if __name__ == "__main__":
    # Print colored ASCII art for the start of the program
    print_color_figlet("Dark   S", 'purple')
    main()
