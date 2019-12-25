#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import time

from utils import SimpleUpdaterThread, Command


class MonitoredMachine(SimpleUpdaterThread):
    INTERVAL = 15

    def is_up(self):
        raise NotImplementedError

class MockMonitoredMachine(MonitoredMachine):
    def __init__(self, *args, **kwargs):
        self.up = False
        super(MockMonitoredMachine, self).__init__(*args, **kwargs)

    def is_up(self):
        return self.up

    def update(self):
        time.sleep(self.INTERVAL/2.0)
        self.mark_update_success()

    def turn_on(self):
        time.sleep(3)
        self.up = True
