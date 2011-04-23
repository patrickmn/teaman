import sys

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
