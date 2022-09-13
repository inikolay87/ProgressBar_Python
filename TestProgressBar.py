# -*- coding: utf-8 -*-
#
import time, sys

PROGRESS_BAR_WIDTH=50

# LINUX (1/8, 2/8, 3/8 ... bar-symbols)
PROGRESS_SYMBOLS = ["", chr(0x258F), chr(0x258E), chr(0x258D), chr(0x258C), chr(0x258B), chr(0x258A), chr(0x2589)]

# WINDOWS (only half and full bar-symbols)
#PROGRESS_SYMBOLS = [""] + [chr(0x258C)]

def print_progress_bar(percentage: float, width: int = 20):
    count = min(width * percentage / 100, width)
    count_full = int(count)
    bar = chr(0x2588) * count_full
    rest_char_id = int((count - count_full) * len(PROGRESS_SYMBOLS))
    bar += PROGRESS_SYMBOLS[rest_char_id]
    bar += " " * (width - len(bar))
    print(f"\r[{bar}] {percentage:5.1f}%", end="") sys.stdout.flush()
    
def clear_progress_bar(width: int = 20):
    print("\r" + " " * (width + 10) + "\r", end="") sys.stdout.flush()
    
if __name__ == "__main__":
    complete = 0
    file_size = 100
    while (complete<=file_size):
        print_progress_bar(complete / file_size * 100, PROGRESS_BAR_WIDTH)
        complete += 0.1
        time.sleep(0.01)
    clear_progress_bar(PROGRESS_BAR_WIDTH)
    
