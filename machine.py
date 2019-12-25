#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

class MonitoredMachine(SimpleUpdaterThread):
    INTERVAL = 30

    def is_up(self):
        raise NotImplementedError

class MockMonitoredMachine(MonitoredMachine):
    def __init__(self, *args, **kwargs):
        self.up = False
        super(MockMonitoredMachine, self).__init__(*args, **kwargs)

    def is_up(self):
        return self.up

    def update(self):
        pass

    def turn_on(self):
        time.sleep(3)
        self.up = True
