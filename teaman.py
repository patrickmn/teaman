#!/usr/bin/env python
"""
  Teaman

  Simple console app that alerts you (with sound) when your cup of tea is ready.

  by Patrick Mylund Nielsen
  https://github.com/pmylund/teaman
"""

__version__ = '1.0'

import sys
import time
import datetime

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
        return

def countdownToTea(duration):
    print "\r\nYour tea will be ready at %s." % (datetime.datetime.now() + datetime.timedelta(seconds=duration)).strftime('%X')
    time.sleep(duration)
    print("\r\nYour tea is ready!")
    if play_ready_sound:
        try:
            util.playSound(ready_sound_file)
        except:
            pass
    answer = raw_input("\r\nHaving another cup? (Y/N/secs) ").lower()
    if answer == 'y' or not answer:
        countdownToTea(duration)
    elif answer == 'n':
        pass
    else:
        try:
            duration = int(answer)
        except:
            pass
        else:
            countdownToTea(duration)

def isLinux():
    return 'linux' in sys.platform

def isWindows():
    return sys.platform == 'win32'

def playSound(sound_file):
    if isWindows():
        import winsound
        winsound.PlaySound(sound_file, winsound.SND_FILENAME)
    elif isLinux():
        from wave import open as waveOpen
        from ossaudiodev import open as ossOpen
        s = waveOpen(sound_file, 'rb')
        (nc, sw, fr, nf, comptype, compname) = s.getparams( )
        dsp = ossOpen('/dev/dsp', 'w')
        try:
            from ossaudiodev import AFMT_S16_NE
        except ImportError:
            if byteorder == "little":
                AFMT_S16_NE = ossaudiodev.AFMT_S16_LE
            else:
                AFMT_S16_NE = ossaudiodev.AFMT_S16_BE
                dsp.setparameters(AFMT_S16_NE, nc, fr)
                data = s.readframes(nf)
                s.close()
                dsp.write(data)
                dsp.close()

if __name__ == '__main__':
    main()
