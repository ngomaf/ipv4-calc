from views.viewmain import ViewMain

from components.clsmask import ClsMask
from components.clswildcard import ClsWildCard
from components.clsnetwork import ClsNetwork


class CtrlMain:

	__slots__ = ['_view']

	def __init__(self, bord, root):
		self._view = ViewMain(self, bord, root)

	def prepar(self, data):
		array = data.split()
		data = data.split('/')

		if len(data) > 1:
			address = data[0]
			prefix = data[1]
		else:
			address = data[0]
			prefix = 24

		address = address.split('.')

		if len(address) == 4:
			oct1 = address[0]
			oct2 = address[1]
			oct3 = address[2]
			oct4 = address[3]

			if str(prefix).isnumeric() and oct1.isnumeric() and oct2.isnumeric() and oct3.isnumeric() and oct4.isnumeric():
				mask = ClsMask(int(prefix)).get_mask()
				mask_pref = mask+' = '+str(prefix)

				wildcard = ClsWildCard(mask).get_wildcard()

				clsnet = ClsNetwork(address,prefix)
				network = clsnet.net_address()
				bcast = clsnet.bcast_address()
				firsthost = clsnet.firsthost_address()
				lasthost = clsnet.lasthost_address()
				totadresses = clsnet.tot_addresses()
				tothosts = clsnet.tot_hosts()
				clsip = clsnet.class_ip()
				clstype = clsnet.type_ip()

				return {'title': 'Sucesso!', 
						'content': [
										[array[0]],
										[mask_pref],
										[wildcard],
										[network],
										[bcast],
										[firsthost],
										[lasthost],
										[totadresses],
										[tothosts],
										[clsip],
										[clstype]
									],
						}
			else:
				return {'title': 'Erro!', 'content': 'Dados inválidos.\nCorrija e volte a tentar.'}
		else:
			return {'title': 'Erro!', 'content': 'Octeto incompleto.\nCorrija e volte a tentar.'}
