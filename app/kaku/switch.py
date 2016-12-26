from proto import Proto
from transmitter import Transmitter


class Switch(object):

    def __init__(self, proto, transmitter):
        self.__proto = proto
        self.__transmitter = transmitter

    def switch_on(self):
        packet = self.__proto.packet_on()
        self.__transmitter.transmit(packet)

    def switch_off(self):
        packet = self.__proto.packet_off()
        self.__transmitter.transmit(packet)


def switch_off(pin, addr, unit):
    transmitter = Transmitter(pin)
    proto = Proto(addr, unit)
    switch = Switch(proto, transmitter)
    switch.switch_off()


def switch_on(pin, addr, unit):
    transmitter = Transmitter(pin)
    proto = Proto(addr, unit)
    switch = Switch(proto, transmitter)
    switch.switch_on()
