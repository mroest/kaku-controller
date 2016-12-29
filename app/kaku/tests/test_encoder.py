import unittest
from app.kaku.encoder import Encoder


class TestEncoder(unittest.TestCase):
    """ Testing the encoder """

    def test_encode(self):
        """ Run a number of encodings """
        bstr = Encoder.encode(1, 3)
        self.assertEqual('001', bstr)

        bstr = Encoder.encode(2, 10)
        self.assertEqual('0000000010', bstr)

        bstr = Encoder.encode(0, 0)
        self.assertEqual('0', bstr)

        bstr = Encoder.encode(False, False)
        self.assertEqual('0', bstr)

        bstr = Encoder.encode(True, True)
        self.assertEqual('1', bstr)

        bstr = Encoder.encode(10, 10)
        self.assertEqual('0000001010', bstr)

        bstr = Encoder.encode(728364872632872, 64)
        self.assertEqual(
            '0000000000000010100101100111000110101001100000000000101000101000',
            bstr)

        bstr = Encoder.encode(3, 1)
        self.assertEqual('11', bstr)
