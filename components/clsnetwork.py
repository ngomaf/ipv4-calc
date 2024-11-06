
class ClsNetwork:

    __slots__ = ['_address', '_prefix', '_bits', '_num_subnet', '_num_network']

    def __init__(self, address, prefix):
        self._address = address
        self._prefix = int(prefix)

        self._bits = self.get_bits()
        self._num_subnet = 2**self._bits
        self._num_network = 2**(8 - self._bits)

    def net_address(self):
        network = self.process()
        address = self._address

        if self._prefix <= 8:
            return f'{network["network"]}.0.0.0'
        elif self._prefix <= 16:
            return f'{address[0]}.{network["network"]}.0.0'
        elif self._prefix <= 24:
            return f'{address[0]}.{address[1]}.{network["network"]}.0'
        elif self._prefix <= 32:
            return f'{address[0]}.{address[1]}.{address[2]}.{network["network"]}'

    def bcast_address(self):
        network = self.process()
        address = self._address

        if self._prefix <= 8:
            return f'{network["brodcast"]}.255.255.255'
        elif self._prefix <= 16:
            return f'{address[0]}.{network["brodcast"]}.255.255'
        elif self._prefix <= 24:
            return f'{address[0]}.{address[1]}.{network["brodcast"]}.255'
        elif self._prefix <= 32:
            return f'{address[0]}.{address[1]}.{address[2]}.{network["brodcast"]}'

    def firsthost_address(self):
        network = self.process()
        address = self._address

        if self._prefix <= 8:
            return f'{network["network"]}.0.0.1'
        elif self._prefix <= 16:
            return f'{address[0]}.{network["network"]}.0.1'
        elif self._prefix <= 24:
            return f'{address[0]}.{address[1]}.{network["network"]}.1'
        elif self._prefix <= 32:
            return f'{address[0]}.{address[1]}.{address[2]}.{network["firsthost"]}'

    def lasthost_address(self):
        network = self.process()
        address = self._address

        if self._prefix <= 8:
            return f'{network["brodcast"]}.255.255.254'
        elif self._prefix <= 16:
            return f'{address[0]}.{network["brodcast"]}.255.254'
        elif self._prefix <= 24:
            return f'{address[0]}.{address[1]}.{network["brodcast"]}.254'
        elif self._prefix <= 32:
            return f'{address[0]}.{address[1]}.{address[2]}.{network["lasthost"]}'

    def tot_addresses(self):
        base_address = self._num_network

        if self._prefix <= 8:
            return base_address * 256 * 256 * 256
        elif self._prefix <= 16:
            return base_address * 256 * 256
        elif self._prefix <= 24:
            return base_address * 256
        elif self._prefix <= 32:
            return base_address

    def tot_hosts(self):
        return self.tot_addresses() - 2

    def class_ip(self):
        oct0 = int(self._address[0])

        if oct0 < 0:
            return '[Erro!] valor inválido'
        elif oct0 < 127:
            return 'A'
        elif oct0 < 128:
            return 'L' # Loopback
        elif oct0 < 192:
            return 'B'
        elif oct0 < 223:
            return 'C'
        elif oct0 < 239:
            return 'M' # destinado Multicast
        elif oct0 < 255:
            return 'EP' # destinado Estudos e Projectos

    def type_ip(self):
        oct0 = int(self._address[0])
        oct1 = int(self._address[1])
        oct2 = int(self._address[2])
        if oct0 == 10:
            return 'Privado'
        elif oct0 == 172 and (15 < oct1 < 32):
            return 'Privado'
        elif oct0 == 192 and oct1 == 168:
            return 'Privado'
        else:
            return 'Público'

    def process(self):
        subnet_list = []
        qtdd = 0
        for subnet in range(0, self._num_subnet):
            subnet_list.append(qtdd + self._num_network)
            qtdd += self._num_network

        if self._prefix <= 8:
            for subnet in range(0, len(subnet_list)):
                if subnet_list[subnet] > int(self._address[0]):
                    vrede = subnet_list[subnet] - self._num_network
                    vbrodcast = subnet_list[subnet] - 1
                    v1host = vrede + 1
                    vuhost = vbrodcast - 1
                    break
        elif self._prefix <= 16:
            for subnet in range(0, len(subnet_list)):
                if subnet_list[subnet] > int(self._address[1]):
                    vrede = subnet_list[subnet] - self._num_network
                    vbrodcast = subnet_list[subnet] - 1
                    v1host = vrede + 1
                    vuhost = vbrodcast - 1
                    break
        elif self._prefix <= 24:
            for subnet in range(0, len(subnet_list)):
                if subnet_list[subnet] > int(self._address[2]):
                    vrede = subnet_list[subnet] - self._num_network
                    vbrodcast = subnet_list[subnet] - 1
                    v1host = vrede + 1
                    vuhost = vbrodcast - 1
                    break
        elif self._prefix <= 32:
            for subnet in range(0, len(subnet_list)):
                if subnet_list[subnet] > int(self._address[3]):
                    vrede = subnet_list[subnet] - self._num_network
                    vbrodcast = subnet_list[subnet] - 1
                    v1host = vrede + 1
                    vuhost = vbrodcast - 1
                    break

        return {'network': vrede,
                'brodcast': vbrodcast,
                'firsthost': v1host,
                'lasthost': vuhost
                }

    def get_bits(self):
        pfxo = self._prefix

        if pfxo <= 8:
            return pfxo
        elif pfxo <= 16:
            return pfxo - 8
        elif pfxo <= 24:
            return pfxo - 16
        elif pfxo <= 32:
            return pfxo - 24

