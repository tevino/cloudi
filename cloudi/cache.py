#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shelve

cache_path = os.path.join(os.getenv('HOME'), '.cloudi.cache')


class Cache:
    c = shelve.open(cache_path, 'c')

    @classmethod
    def _is_word_exist(cls, word):
        return word in cls.c

    @classmethod
    def get_exp(cls, word):
        if cls._is_word_exist(word):
            return cls.c[word]

    @classmethod
    def cache_word(cls, word, exp):
        if not cls._is_word_exist(word):
            cls.c[word] = exp
