#!/usr/bin/env python
#coding: utf-8

import sys
import time
from datetime import datetime
from daemon import DaemonContext

import smbus

bus_number  = 1
lcd_address = 0x71


class LCD:
    def __init__(self, bus_number, lcd_address, brightness=0xFF):
        self.bus_number = bus_number
        self.lcd_address = lcd_address
        self.bus = smbus.SMBus(bus_number)

    def set_brightness(self, v):
        if 0 <= v <= 255:
            self.bus.write_i2c_block_data(self.lcd_address, 0x7A, [v])

    def output(self, s):
        while True:
            try:
                self.bus.write_i2c_block_data(self.lcd_address,0x76,map(int, s))
                self.bus.write_i2c_block_data(self.lcd_address,0x77,[0x10])
                break
            except IOError:
                pass


class DiffNotifer:
    def __init__(self, func):
        self.func = func
        self.prev_data = None

    def __call__(self):
        now_data = self.func()
        if now_data != self.prev_data:
            self.prev_data = now_data
            return now_data
        return None


def main():
    lcd = LCD(bus_number, lcd_address)
    lcd.set_brightness(0xFF)

    dn = DiffNotifer(lambda: datetime.now().strftime("%H%M"))

    while True:
        data = dn()
        if data is not None:
            lcd.output(data)
        time.sleep(0.2)


if __name__ == '__main__':
    if "-f" in sys.argv:
        main()
    else:
        with DaemonContext():
            main()
