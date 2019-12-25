#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, with_statement

import time

from pirouser.machine import MockMonitoredMachine
from pirouser.ups import MockUPSChecker
from pirouser.pirouser import PiRouser

if __name__== "__main__":
    print("Initialising PiRouser")
    checker = MockUPSChecker()
    machine = MockMonitoredMachine()
    rouser = PiRouser(checker, machine)

    while True:
        time.sleep(10)
    #
