#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shelve

cache_path = os.path.join(os.getenv('HOME'), '.cloudi.cache')


class Cache:
    c = shelve.open(cache_path, 'c')

    @classmethod
    def exists(cls, word):
        return word in cls.c

    @classmethod
    def get(cls, word):
        if cls.exists(word):
            return cls.c[word]

    @classmethod
    def set(cls, word, exp):
        if not cls.exists(word):
            cls.c[word] = exp
