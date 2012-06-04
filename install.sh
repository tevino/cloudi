#!/usr/bin/env bash

chmod +x ./cloudi.py
current_dir=$(dirname -- $(readlink -f -- "$0")) 
echo \#Start alias for Cloudi >>~/.bashrc
echo alias\ d\="$current_dir/cloudi.py" >>~/.bashrc 
echo \#End alias for Cloudi >>~/.bashrc
echo Installation finished.
