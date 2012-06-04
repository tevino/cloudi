#!/usr/bin/env bash

CWD="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

chmod +x ${CWD}/cloudi.py
echo \#Start alias for Cloudi >>~/.bashrc
echo alias\ d\="$CWD/cloudi.py" >>~/.bashrc 
echo \#End alias for Cloudi >>~/.bashrc
echo Installation finished.
