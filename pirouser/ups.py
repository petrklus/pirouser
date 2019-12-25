#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

from utils import SimpleUpdaterThread, Command

class UPSChecker(SimpleUpdaterThread):
    INTERVAL = 15
    ACCEPTABLE_CHARGE = 0.2 # 20% minimum charge
    MAX_AGE = 60

    def __init__(self, *args, **kwargs):
        super(UPSChecker, self).__init__(*args, **kwargs)

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




class MockUPSChecker(UPSChecker):

    INTERVAL = 15

    def __init__(self, *args, **kwargs):
        self.tick_counter = 0
        super(MockUPSChecker, self).__init__(*args, **kwargs)

    def is_ready(self):
        return not self.is_stale()

    def get_charge_level(self):
        return min(1, self.tick_counter/10.0)

    def update(self):
        self.tick_counter += 0.5
        self.mark_update_success()
