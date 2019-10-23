import json
import numpy as np
import os
import sys

import ok

import labrad
from twisted.internet.defer import inlineCallbacks, returnValue
from twisted.internet.threads import deferToThread

ok_server = 'polarkrb_okfpga'
device_id = 'KRbStable01'
mode_wire = 0x00
modes = {'idle': 0, 'reset': 1, 'init': 2}

@inlineCallbacks
def main():
    cxn = yield labrad.connect()

    server = cxn.servers[ok_server]
    yield server.select_interface(device_id)

    settings = ['idle', 'reset', 'idle', 'init', 'idle']
    for s in settings:
        yield server.set_wire_in(mode_wire, modes[s])
        yield server.update_wire_ins()
        print "Device {} set to mode {}".format(device_id, s)

if __name__ == "__main__":
    main()
