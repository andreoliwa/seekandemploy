#!/bin/bash

# Need to run as sudo
# TODO: add check for sudo

# Python and dependencies
apt-get -y install python2.7 python2.7-dev python2.7-dbg python-pip pylint

# Config path
echo $HOME'/projects/seekandemploy' >> /usr/local/lib/python2.7/dist-packages/seekandemploy.pth

# Log dir
mkdir /var/log/seekandemploy
chmod a+w /var/log/seekandemploy
