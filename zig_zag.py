import time
import sys

indent_by = 0  # how many spaces to indent
isincrease = True  # check if to increase the indentation or not

try:
    while True:
        # TODO print indentation and then eight asterisks (*) to the screen
        print(' ' * indent_by, end='')
        print('********')

        # TODO: Pause program for 0.1s
        time.sleep(0.1)

        # TODO: Increase the number of indents
        indent_by += 1
except KeyboardInterrupt:
    # Code to execute in the event of an exception
    # Exit program when the stop button or CTRL-C is pressed
    sys.exit()
