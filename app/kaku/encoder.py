class Encoder(object):
    """ a string / byte encoder for kaku """

    @staticmethod
    def encode(val, len):
        spec = '{0:0%sb}' % int(len)
        return spec.format(int(val))
