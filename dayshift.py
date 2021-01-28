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
    show_success_modal=False,
    force_stop_is_error=False,
    optional_cols=2,
    progress_regex=r"^progress: (?P<current>\d+)/(?P<total>\d+)$",
    progress_expr="current / total * 100",
    menu=[{'name': 'Help', 'items': [
        {
            'type': 'Link',
            'menuTitle': 'GitHub Respository',
            'url': 'https://github.com/MrChuckomo/day-shift'
        },
        {
            'type': 'Link',
            'menuTitle': 'Report an issue',
            'url': 'https://github.com/MrChuckomo/day-shift/issues'
        },
        {
            'type': 'AboutDialog',
            'menuTitle': 'About',
            'description': 'Just a small script to do your day shift!',
            'version': '1.0.0',
            'copyright': '2021',
            'license': 'GPL-3.0'
        }]
    }])
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
    timer_group = parser.add_argument_group(
        "Timer Options",
        "Customize the exit timer"
    )
    timer_group.add_argument(
        '--timer',
        metavar='Exit Timer',
        default=None,
        type=int,
        help='Time after which this tool should stop',
        widget='IntegerField'
    )
    timer_group.add_argument(
        '--format',
        metavar='Time Format',
        choices=['Second(s)', 'Minute(s)', 'Hour(s)'],
        default='Minute(s)',
        help='Slect the time format'
    )


    args = parser.parse_args()
    print(f'Run with set args: {args}')

    start = time.time()
    elapsed_time = 0.0
    
    if args.format == 'Minute(s)':
        exit_time = args.timer * 60
    elif args.format == 'Hour(s)':
        exit_time = args.timer * 60 * 60
    else:
        exit_time = args.timer

    # for i in range(100):
    # while True:
    while elapsed_time <= exit_time:
        keyboard.press_and_release(args.key)
        time.sleep(args.sleep_time)

        end = time.time()
        elapsed_time = round(end - start, 2)

        print(f'press [{args.key}]', f'time: {elapsed_time} sec.')
        # print(f'progress: {i}/100')

    print('Done')

if __name__ == "__main__":
    main()
