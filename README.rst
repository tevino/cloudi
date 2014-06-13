==========================
cloudi - Cloud Dictionary
==========================

This project is based on ``dict.qq.com`` which is closed, so it will not work anymore. 2014-06-13
==================================================================================================


Summary
---------
``cloudi`` is a convenient online EN<->ZH dictionary **without other dependences** for command line users.

``cloudi`` will cache the result every time you use it, so there is no need for Internet connection when you query the same thing again.


Dependencies
------------
**You usually already have at least one of the following in your system.**

- ``xclip``
- ``xsel``
- ``gtk`` (python library)
- ``PyQt4``

One of above is needed for accessing clipboard on linux.


Installation Instructions
-------------------------
Using pip::

    $ pip install cloudi


Usage
------
The following command query the word "hello"::

    $ d hello

Chinese are the same::

    $ d 你好

phrases are the same, for instance "Thanksgiving Day"::

    $ d Thanksgiving Day

or::

    $ d "Thanksgiving Day"

If you do not specify what to query, cloudi will query the text in your clipboard.
In this case, all you need is::

    $ d


FAQ
-----
If something(e.g. ``oh-my-zsh``) you are using have taken the alias ``d`` , try::

    $ unalias d

for ``oh-my-zsh`` users::

    $ echo "unalias d" >> ~/.oh-my-zsh/custom/unalias_cloudi.zsh
