"""
File         : dayshift.py
Description  : 

Author       : Alexander Kettler
Version      : v0.1.0
Creation Date: 20-Jan-2021
"""

import time
import keyboard

from gooey import Gooey


# ---------------------------------------------------------------------------------------------------------------------

key = 'shift'

# @Gooey
def main():
    keyboard.press_and_release(key)
    print(f'press {key}')
    

if __name__ == "__main__":
    while True:
        main()
        time.sleep(3)    
