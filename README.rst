==========================
Cloudi - Cloud Dictionary
==========================
Current version: v0.30


Summary
---------
``Cloudi`` is a convenient online dictionary for command line users.

It can translate between English and Chinese

When you query a word for the first time ``cloudi`` will save the result so there is no need for Internet connection if you query it again.


Dependencies
------------

    python 2.6+

    ``xsel`` is needed for "clipboard" access


Installation Instructions
-------------------------
if you use bash::

    $ sh install.sh

or you should know what to do with ``install.sh``


Usage
------
The following command query the word 'hello'::

    $ d hello

Chinese are the same::

    $ d 你好

phrases are the same, for instance 'Thanksgiving Day'::

    $ d Thanksgiving Day

or::

    $ d "Thanksgiving Day"

If you do not specify what to query, Cloudi will get a word from your "clipboard".
In this case, all you need is::

    $ d
