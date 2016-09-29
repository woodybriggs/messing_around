#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE


def shell_call(_program, _options, _std_arg):

    program = [_program]
    options = []
    for each in _options:
        options.append(each)

    call = Popen(program + options, stdout=_std_arg, stderr=_std_arg)
    stdout_val, stderr_val = call.communicate()
    return stdout_val


def get_playing_song():
    song = shell_call('rhythmbox-client', ['--print-playing'], PIPE)
    rev = song[::-1].split('(', 1)
    body = rev[0][3:][::-1]
    song = rev[1][::-1]
    return [song, body]


shell_call('notify-send', ['--icon=/usr/share/icons/hicolor/48x48/apps/rhythmbox.png'] + get_playing_song(), None)
