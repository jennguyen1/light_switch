#!/usr/bin/env python3
"""
@author: Jennifer Nguyen
"""

import subprocess
import argparse
from light_switch import *

def run(pin = 11, status = 'off'):
    ls = lightSwitch(pin)
    if status == 'on':
        ls.on()
    else:
        ls.off()
    ls.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = '''Light Switch''')
    parser.add_argument('--pin', type = int, help = 'pin position')
    parser.add_argument('--status', help = 'on or off')
    args = parser.parse_args()
    run(pin = args.pin, status = args.status)
