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

@Gooey(
    program_name='DayShift',
    show_stop_warning=False,
    force_stop_is_error=False,
    optional_cols=1,
    progress_regex=r"^progress: (?P<current>\d+)/(?P<total>\d+)$",
    progress_expr="current / total * 100")
def main():
    parser = GooeyParser(description='Configure your dayshift!')
    parser.add_argument(
        '--key',
        metavar='Key',
        choices=['SHIFT', 'CTRL', 'SPACE'],
        default='SHIFT',
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

    for i in range(100):
    # while True:
        time.sleep(args.sleep_time)

        keyboard.press_and_release(args.key)
        print(f'press [{args.key}]')
        print(f'progress: {i}/100')


if __name__ == "__main__":
    main()
