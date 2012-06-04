#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import shelve
import os.path

currentdir = sys.path[0]
cache_file = os.path.join(currentdir, '.cache.db')


class Cache:
    db = shelve.open(cache_file, 'c')

    @classmethod
    def _is_word_exist(cls, word):
        return word in cls.db

    @classmethod
    def get_exp(cls, word):
        if cls._is_word_exist(word):
            return cls.db[word]

    @classmethod
    def cache_word(cls, word, exp):
        if not cls._is_word_exist(word):
            cls.db[word] = exp
