#!/usr/bin/env python
# -*- coding: utf-8 -*-

red_s = u'\033[0;31m'
lgreen_s = u'\033[1;32m'
dgreen_s = u'\033[0;32m'
white_s = u'\033[1m'

ed = u'\033[0m'


def _rig(st, s):
    return u'%s%s%s' % (st, s, ed)


def red(s):
    return _rig(red_s, s)


def lgreen(s):
    return _rig(lgreen_s, s)


def dgreen(s):
    return _rig(dgreen_s, s)


def white(s):
    return _rig(white_s, s)

if __name__ == '__main__':
    print 'normal'
    print lgreen('light green')
    print dgreen('dark green')
    print white('white')
