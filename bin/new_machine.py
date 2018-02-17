#!/usr/bin/python3
import os

os.system("""
echo "Nice name: " > README
echo "Description: " >> README
echo "Designed year: " >> README
echo "Weight: " >> README
echo "Approximate price USD: " >> README
echo "Wikipedia link: " >> README
echo "(delete lines you don't know)" >> README
lspci > lspci.out
lsusb > lsusb.out
cat /proc/cpuinfo > cpuinfo.out
""")
