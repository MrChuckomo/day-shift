"""
File         : dayshift.py
Description  : 

Author       : Alexander Kettler
Version      : v0.1.0
Creation Date: 20-Jan-2021
"""

import time
import keyboard


# ---------------------------------------------------------------------------------------------------------------------

key = 'shift'

while True:
    keyboard.press_and_release(key)
    print(f'press {key}')
    time.sleep(3)
