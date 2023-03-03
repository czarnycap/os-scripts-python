#!/usr/bin/env python3
import re

# Define the regular expression pattern for Polish postal code
# pattern = re.compile(r'^\\d{2}-\\d{3}$')
pattern = re.compile(r"^\d{2}-\d{3}$")

# Read the input from the user and catch errors
while True:
    try:
        code = input('Enter a Polish postal code:')
        print("you entered:", code, "which has ", len(code), "characters")

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
