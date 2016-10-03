#!/usr/bin/env python
from subprocess import Popen, PIPE
import time

def shell_call(prog, _std_arg):
    call = Popen(prog, stdout=_std_arg, stderr=_std_arg)
    stdout_val, stderr_val = call.communicate()
    return stdout_val


def get_playing():
    return get_playing_song() + get_playing_body()


def get_playing_song():
    song = shell_call(['rhythmbox-client', '--print-playing-format', '%st'], PIPE).rstrip()
    return [song]


def get_playing_body():
    body = shell_call(['rhythmbox-client', '--print-playing-format', '%tt'], PIPE).rstrip()
    return [body]


def log_playing_song():
    # format data
    info_in = get_playing()
    time = shell_call(['date', '+%d/%m/%Y, %T'], PIPE)
    info_in.append(time)
    info_out = ', '.join(info_in)

    # write data
    f = open('song_list.csv', 'a')
    f.write(info_out)
    f.close()


shell_call(['notify-send', '--icon=/usr/share/icons/hicolor/48x48/apps/rhythmbox.png'] + get_playing(), None)
log_playing_song()
