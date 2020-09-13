"""
Author: Jason D'Oyley
Date: Sept. 13, 2020
Source: Automate the Boring Stuff with Python by Al Sweigart
"""

import time
import sys

indent_by = 0  # How many spaces to indent
isincrease = True  # Check if to increase the indentation or not

try:
    while True:
        # Print indentation and then eight asterisks (*) to the screen
        print(' ' * indent_by, end='')
        print('********')

        # Pause program for 0.1s
        time.sleep(0.1)

        if isincrease:
            # Increase the number of indents
            indent_by += 1

            if indent_by == 20:
                isincrease = False
        else:
            # Decrease if isincrease is false
            indent_by -= 1

            if indent_by == 0:
                isincrease = True
except KeyboardInterrupt:
    # Exit program when the stop button or CTRL-C is pressed
    sys.exit()
