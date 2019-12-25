#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import threading
import sys
import time

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
        # THIS IS NOT SECURE - USES SHELL TRUE. INTERNAL USE ONLY.
        try:
            self.output = subprocess.check_output(self.cmd, shell=True,
                timeout=self.timeout)
            return 0, self.output
            #print('-Done')
        except subprocess.CalledProcessError as ce:
            return 1, b"Failed"
        except subprocess.TimeoutExpired as e:
            return 2, b"Timed out"



class SimpleUpdaterThread(object):

    INTERVAL = 30
    MAX_AGE = 60

    @classmethod
    def get_interval(cls):
        return cls.INTERVAL

    def __init__(self):
        self.age = self.MAX_AGE

        thread = threading.Thread(target=self._run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def _run(self):
        """ Method that runs forever """
        while True:
            self.update()
            time.sleep(self.INTERVAL)

    def is_stale(self):
        return self.age >= self.MAX_AGE

    def mark_update_success(self):
        self.age = 0

    def update(self):
        raise NotImplementedError

if __name__ == "__main__":
    cmd = b"echo 'Process started'; sleep 2; echo 'Process finished'"

    print(Command(cmd, timeout=3).run())
    print(Command(cmd, timeout=1).run())
    print(Command(b"exit 1", timeout=1).run())
