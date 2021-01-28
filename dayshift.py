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

@Gooey
def main():
    parser = argparse.ArgumentParser(description='Setup your daysift!')
    parser.add_argument(
        '--key',
        type=str,
        default='shift',
        help='A key you want to send'
    )
    parser.add_argument(
        '--time',
        type=int,
        default=3,
        help='Set a pause time in sec.'
    )

    args = parser.parse_args()
    print(f'Run with set args: {args}')

    while True:
        time.sleep(args.time)

        keyboard.press_and_release(args.key)
        print(f'press {args.key}')


if __name__ == "__main__":
    main()
