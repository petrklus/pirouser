#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, with_statement

import threading
import time


class UPSChecker(object):
    INTERVAL = 15
    ACCEPTABLE_CHARGE = 0.2 # 20% minimum charge
    MAX_AGE = 60

    @classmethod
    def get_interval(cls):
        return cls.INTERVAL

    def reset_timestamp(self):
        pass

    def is_ready(self):
        return False

    def has_enough_charge(self):
        return self.get_charge_level() >= self.ACCEPTABLE_CHARGE

    def has_power(self):
        raise NotImplementedError

    def get_charge_level(self):
        raise NotImplementedError


    def update(self):
        raise NotImplementedError

    def is_stale(self):
        return self.age >= self.MAX_AGE

    def mark_update_success(self):
        self.age = 0

    def __init__(self, interval=1):

        self.age = self.MAX_AGE

        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True                            # Daemonize thread
        thread.start()                                  # Start the execution

    def run(self):
        """ Method that runs forever """
        while True:
            self.update()
            time.sleep(self.INTERVAL)


class MockUPSChecker(UPSChecker):
    INTERVAL = 1

    def __init__(self, *args, **kwargs):
        self.tick_counter = 0
        super(MockUPSChecker, self).__init__(*args, **kwargs)

    def is_ready(self):
        return not self.is_stale()

    def get_charge_level(self):
        return min(1, self.tick_counter/10.0)

    def update(self):
        self.tick_counter += 1
        self.mark_update_success()


class PiRouser(object):

    def __init__(self, checker):
        self.checker = checker



if __name__== "__main__":
    print("Initialising pirouser")
    checker = MockUPSChecker()
    print(checker.get_interval())


    print("Has enough charge?", checker.has_enough_charge())

    for _ in range(5):
        print("Has enough charge?", checker.has_enough_charge())
        print(checker.get_charge_level())
        checker.update()
        time.sleep(2)

    #
