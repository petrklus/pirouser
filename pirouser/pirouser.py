#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, with_statement

import time
import datetime
from utils import SimpleUpdaterThread


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
        has_mainspower = self.checker.has_power()

        print("T{}".format(datetime.datetime.now()))
        print("Checking....")

        if self.machine.is_stale():
            print(" Machine is reading is stale, cannot tell "
                  "if it's up or down")
        elif self.checker.is_stale():
            print(" UPS reading is stale, cannot tell "
                "if it's up or down")
        else:
            # neither the UPS or machine reading is stale
            if self.machine.is_up():
                print(" Machine is up, no operation needed")
            else:
                print(" Machine is not up")
                print(" Charge level:", self.checker.get_charge_level())

                if has_enough_charge and has_mainspower:
                    print(" Enough charge, attempting machine power-on...")
                    ret = self.machine.turn_on()
                    print(" Attempted turn on result: ", ret)
                elif not has_enough_charge:
                    print(" Not enougn charge, waiting further...")
                elif not has_mainspower:
                    print(" Mains power not restored, waiting further...")
