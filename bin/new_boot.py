#!/usr/bin/python3

import os
import time


class Writer:
    def cmd_to_file(m, cmd, fn):
        os.system("%s > %s/%s" % (cmd, m.boot_path, fn))
        
    def run(m):
        year = 1970 + time.time() / (365.256363004 * 24 * 60 * 60)
        m.boot_path = "%s" % year
        os.mkdir(m.boot_path)
        
        m.cmd_to_file("uname -a", "uname.out")
        m.cmd_to_file("dmesg", "dmesg.out")
        m.cmd_to_file("cat /proc/config.gz", "config.gz")

w = Writer()
w.run()
