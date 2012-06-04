#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shelve

cache_file = os.path.join(os.getenv('HOME'), '.cloudi_cache.db')


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
