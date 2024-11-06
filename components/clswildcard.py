
class ClsWildCard:

    __slots__ = ['_mask']

    def __init__(self, mask):
        self._mask = mask

    def get_wildcard(self):
        wc_arr = self._mask.split('.')

        wc_arr[0] = 255 - int(wc_arr[0])
        wc_arr[1] = 255 - int(wc_arr[1])
        wc_arr[2] = 255 - int(wc_arr[2])
        wc_arr[3] = 255 - int(wc_arr[3])

        return f'{wc_arr[0]}.{wc_arr[1]}.{wc_arr[2]}.{wc_arr[3]}'
