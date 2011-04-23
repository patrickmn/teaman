#!/usr/bin/env python
"""
  Teaman

  Simple tea timer

  by Patrick Mylund Nielsen
  http://github.com/pmylund/teaman

"""

__version__ == '1.0'

import sys
import time

import util

# Linux and Windows only
play_ready_sound = True
ready_sound_file = 'ready.wav'

def main():
    argument = None
    duration = None
    if len(sys.argv) == 2:
        argument = sys.argv[1]
    if argument:
        try:
            duration = int(argument)
        except:
            pass
    if not duration:
        duration = int(raw_input("How long (in seconds) until your cup of tea is ready? "))
    try:
        countdownToTea(duration)
    except KeyboardInterrupt:
        pass

def countdownToTea(duration):
    print "\r\nYour tea will be ready at %s." % time.strftime('%X', time.gmtime(time.time() + duration))
    time.sleep(duration)
    print("\r\nYour tea is ready!")
    if play_ready_sound:
        try:
            util.playSound(ready_sound_file)
        except:
            pass
    input = raw_input("\r\nHaving another cup? (Y/N/secs) ").lower()
    if input == 'y' or not input:
        countdownToTea(duration)
    elif input == 'n':
        pass
    else:
        try:
            duration = int(input)
        except:
            pass
        else:
            countdownToTea(duration)

if __name__ == '__main__':
    main()
