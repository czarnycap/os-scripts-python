#!/usr/bin/env python3
import re

# Define the regular expression pattern for Polish postal code
# pattern = re.compile(r'^\\d{2}-\\d{3}$')
def check_pl_code():
    pattern = re.compile(r"^[0-9]{2}\-[0-9]{3}$")

    # Read the input from the user and catch errors
    while True:
        try:
            code = input('Enter a Polish postal code:')
    #        print("you entered:", code, "which has ", len(code), "characters")

            if pattern.match(code):
                print('Valid Polish postal code')
    #            break
            else:
                print('Invalid Polish postal code')
        except KeyboardInterrupt:
            print('\\nOperation cancelled by user')
            break
        except:
            print('Invalid input. Please try again.')

def run_forrest(arg):
    if arg == "start":
        check_pl_code()

# run_forrest("start")
#TODO run function if module is executed with proper parameter