"""
File         : dayshift.py
Description  :
Creation Date: 20-Jan-2021
"""

import time
import argparse
import keyboard

from gooey import Gooey
from gooey import GooeyParser


# ---------------------------------------------------------------------------------------------------------------------

@Gooey(program_name='DayShift')
def main():
    # parser = argparse.ArgumentParser(description='Configure your dayshift!')
    parser = GooeyParser(description='Configure your dayshift!')
    parser.add_argument(
        '--key',
        metavar='Key',
        choices=['shift', 'ctrl', 'space'],
        default='shift',
        help='A key you want to send'
    )
    parser.add_argument(
        '--sleep-time',
        metavar='Sleep Timer',
        type=int,
        default=3,
        help='Set time between each click (in sec.)',
        widget='IntegerField'
        # widget='Slider'
    )
    parser.add_argument(
        '--timer',
        metavar='Exit Timer',
        # type=int,
        # type=str,
        # choices=range(1000),
        default=None,
        help='Time after which this tool should stop',
        # widget='TimeChooser'
        # widget='Slider'
    )

    args = parser.parse_args()
    print(f'Run with set args: {args}')

    while True:
        time.sleep(args.sleep_time)

        keyboard.press_and_release(args.key)
        print(f'press {args.key}')


if __name__ == "__main__":
    main()
