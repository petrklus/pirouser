#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import threading
import sys

if (sys.version_info > (3, 0)):
    import subprocess
else:
    import subprocess32 as subprocess

class Command(object):
    def __init__(self, cmd, timeout):
        self.cmd = cmd
        self.output = None
        self.timeout = timeout

    def run(self):
        #print('-Thread started')
        try:
            self.output = subprocess.check_output(self.cmd, shell=True,
                timeout=self.timeout)
            return 0, self.output
            #print('-Done')
        except subprocess.CalledProcessError as ce:
            return 1, b"Failed"
        except subprocess.TimeoutExpired as e:
            return 2, b"Timed out"


if __name__ == "__main__":
    cmd = b"echo 'Process started'; sleep 2; echo 'Process finished'"

    print(Command(cmd, timeout=3).run())
    print(Command(cmd, timeout=1).run())
    print(Command(b"exit 1", timeout=1).run())
