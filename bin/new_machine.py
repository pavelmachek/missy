#!/usr/bin/python3

os.system("""
echo "Nice name: " > README
echo "Description: " >> README
echo "Manufacture year: " >> README
echo "Approximate price USD: " >> README
echo "Wikipedia link: " >> README
echo "(delete lines you don't know)" >> README
lspci > lspci.out
lsusb > lsusb.out
cat /proc/cpuinfo > cpuinfo.out
""")
