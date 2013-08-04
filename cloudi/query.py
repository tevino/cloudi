#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib2
import os
import platform
from HTMLParser import HTMLParser
from .cache import Cache
from .color import lgreen, dgreen, white, lgreen_s, ed, red


def _get_clip():
    pf = platform.system().upper()
    if pf.startswith('LINUX'):
        if os.system('which xclip') == 0:
            # xclip exists
            xclip = os.popen('xclip -selection c -o', 'r')
            clip = xclip.read()
            xclip.close()
        else:
            if os.system('which xsel') == 0:
                # xsel exists
                xsel = os.popen('xsel -o', 'r')
                clip = xsel.read()
                xsel.close()
            try:
                import gtk
                clip = gtk.Clipboard().wait_for_text()
            except:
                try:
                    import PyQt4.QtCore
                    import PyQt4.QtGui
                    cb = PyQt4.QtGui.QApplication.clipboard()
                    clip = str(cb.text())
                except:
                    clip = ''
    elif pf.startswith('CYGWIN'):
        with open('/dev/clipboard') as clipboard:
            clip = clipboard.read()
    elif pf.startswith('WINDOWS'):
        # nobody uses this on windows...
        import win32clipboard
        win32clipboard.OpenClipboard()
        clip = win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
    elif pf.startswith('DARWIN'):
        outf = os.popen('pbpaste', 'r')
        clip = outf.read()
        outf.close()
    return clip


def _wget(url):
    try:
        return urllib2.urlopen(url).read()
    except IOError:
        print 'Please Check your network connection.'
        exit()


def print_result(dct):
    local = dct.get('local', None)
    if local and local[0]:
        local = local[0]
    else:
        print red('Sorry no result.')
        exit()
    prons = (''.join([p + ', ' for p in local.get('pho', [])]))[:-2]
    word = local.get('word', None)
    similar = u'同义词:\n'
    for s in local.get('syn', []):
        similar += s['p'] + '\n'
        for w in s['c']:
            similar += '  ' + w
    mor = ''.join(['%s: %s ' % (d['c'], lgreen(d['m'])) for d in local.get('mor', [])])
    des = ''
    for d in local.get('des', []):
        if dct['lang'] == 'ch':
            des += d
        else:
            des += d.get('p', '') + '\n'
            des += white(d.get('d', ''))
        des += '\n'
    sents = ''
    for sent in local.get('sen', []):
        s_type = sent.get('p', '')
        sents += s_type + '\n'
        for s in sent['s']:
            sents += '  %s\n' % s['es'].replace('<b>', lgreen_s).replace('</b>', ed)
            sents += '  %s\n' % dgreen(s['cs'])

    result = ''
    result += '\n%s [%s]\n' % (lgreen(word), dgreen(prons or 'no soundmark'))
    if mor:
        result += '\n%s\n' % mor
    result += '\n' + des
    result += '\n' + sents
    if len(similar) > 5:
        result += '\n' + similar + '\n'

    print HTMLParser.unescape.__func__(HTMLParser, result)


def query(word=None, print_out=False):
    if not word:
        word = _get_clip()

    en_word = urllib2.quote(word)
    url = 'http://dict.qq.com/dict?q=' + en_word
    json_str = Cache.get(word)
    if not json_str:
        json_str = _wget(url)

    json_d = json.loads(json_str)
    err = json_d.get('err', None)
    if err:
        print _wget('http://dict.qq.com/sug?' + en_word).strip().decode('gbk') or red(err)
    else:
        if print_out:
            print_result(json_d)
        Cache.set(word, json_str)
