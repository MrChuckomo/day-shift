"""
File         : dayshift.py
Description  :
Creation Date: 20-Jan-2021
"""

import time
import argparse
import keyboard

from gooey import Gooey


# ---------------------------------------------------------------------------------------------------------------------

key = 'shift'

@Gooey
def main():
    parser = argparse.ArgumentParser(description='Setup your daysift!')
    parser.add_argument(
        '--key',
        type=str,
        default='shift',
        help='A key you want to send'
    )

    print(parser.parse_args())

    while True:
        time.sleep(3)

        keyboard.press_and_release(key)
        print(f'press {key}')


if __name__ == "__main__":
    main()
