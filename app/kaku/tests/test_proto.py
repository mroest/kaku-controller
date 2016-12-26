import unittest
import pytest

from ..proto import Proto


class TestProto(unittest.TestCase):

    def test_packet_off(self):
        proto = Proto(1, 0)
        packet = proto.packet_off()

        assert '00000000000000000000000001000000' == packet

    def test_packet_on(self):
        proto = Proto(1, 0)
        packet = proto.packet_on()

        assert '00000000000000000000000001010000' == packet
