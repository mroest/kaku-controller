from encoder import Encoder


class Proto(object):
    """
    Build the packet/protocol for KaKu device

    Dim is not yet supported!
    """
    def __init__(self, address, unit):
        self.__address = address
        self.__unit = unit

    def packet_off(self):
        packet = self.__get_addr()

        # Group bit
        packet += '0'

        # Switch off bit
        packet += '0'

        # Device unit
        packet += self.__get_unit()

        return packet

    def packet_on(self):
        packet = self.__get_addr()

        # Group bit
        packet += '0'

        # Switch on bit
        packet += '1'

        # Device unit
        packet += self.__get_unit()

        return packet

    def __get_addr(self):
        """ 26 bit address header """
        return Encoder.encode(self.__address, 26)

    def __get_unit(self):
        return Encoder.encode(self.__unit, 4)
