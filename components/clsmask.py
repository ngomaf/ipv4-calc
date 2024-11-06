
class ClsMask:

    __slots__ = ['_prefix']

    def __init__(self, prefix):
        self._prefix = prefix

    def get_mask(self):
        if self._prefix < 1:
            return 404
        elif self._prefix <= 8:
            oct1 = self.decimal(self._prefix)
            return f'{oct1}.0.0.0'
        elif self._prefix <= 16:
            pfixo = self._prefix - 8
            oct2 = self.decimal(pfixo)
            return f'255.{oct2}.0.0'
        elif self._prefix <= 24:
            pfixo = self._prefix - 16
            oct3 = self.decimal(pfixo)
            return f'255.255.{oct3}.0'
        elif self._prefix <= 32:
            pfixo = self._prefix - 24
            oct4 = self.decimal(pfixo)
            return f'255.255.255.{oct4}'
        else:
            return 404

    def decimal(self, val):
        if val == 0:
            return 0
        elif val == 1:
            return 128
        elif val == 2:
            return 192
        elif val == 3:
            return 224
        elif val == 4:
            return 240
        elif val == 5:
            return 248
        elif val == 6:
            return 252
        elif val == 7:
            return 252
        elif val == 8:
            return 255
