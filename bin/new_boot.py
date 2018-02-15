#!/usr/bin/python3

import os

os.system("uname -a > uname.out")
os.system("dmesg > dmesg.out")
os.system("cat /proc/config.gz > config.gz")
