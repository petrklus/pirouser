#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, with_statement

import threading
import time
import datetime

from machine import MockMonitoredMachine
from ups import MockMonitoredMachine


class PiRouser(SimpleUpdaterThread):
    INTERVAL = 4

    def __init__(self, checker, machine, *args, **kwargs):

        self.checker = checker
        self.machine = machine

        super(PiRouser, self).__init__(*args, **kwargs)

    def run(self):
        """ Method that runs forever """
        while True:
            self._run()
            time.sleep(self.INTERVAL)

    def update(self):
        has_enough_charge = self.checker.has_enough_charge()

        print("T{}".format(datetime.datetime.now()))
        print("Checking....")

        if machine.is_up():
            print(" Machine is up, no operation needed")
        else:
            print(" Machine is not up")
            print(" Charge level:", self.checker.get_charge_level())

            if has_enough_charge:
                print(" Enough charge, attempting machine power-on...")
                ret = self.machine.turn_on()
                print(" Attempted turn on result: ", ret)
            else:
                print(" Not enougn charge, waiting further...")



if __name__== "__main__":
    print("Initialising PiRouser")
    checker = MockUPSChecker()
    machine = MockMonitoredMachine()
    rouser = PiRouser(checker, machine)

    time.sleep(10*60)

    #
