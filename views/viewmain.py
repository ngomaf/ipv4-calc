from tkinter import PhotoImage, filedialog, Text
from tkinter.ttk import Frame, Label, Button, Entry, Separator

import textwrap
from models.modeldocs import ModelDocs


class ViewMain:

	__slots__ = ['_top', '_ctrl', '_bord', '_mother', '_top', '_left', '_right',
				'_callback', '_callb_ipv4', '_address_prefix', '_img_set',
				'_img_humburg', '_img_close', '_bt_humburg', '_default', 
				'_result', '_menu', '_state_callb', '_state_result']

	def __init__(self, ctrl, bord, mother):
		self._ctrl = ctrl
		self._bord = bord
		self._mother = mother

		self._top = Frame(self._bord)
		self._top.pack(fill='x', padx=20, pady=5)

		Separator(self._bord, orient='horizontal').pack(fill='x')

		body = Frame(self._bord)
		body.pack()
		self._left = Frame(body) # campo esquerdo
		self._left.pack(side='left', padx=20, pady=20)

		Separator(body, orient='vertical').pack(side='left', fill='y')

		self._right = Frame(body) # campo direito
		self._right.pack(side='left', padx=20, pady=20)

		#
		# inicializacao
		self._state_callb = 0
		self._state_result = 0
		self.show_widgets()

	def default(self):
		self._default.pack_forget()
		self._default = Frame(self._right)
		self._default.pack()

		img_logo_xenon = PhotoImage(file=r'components/icons/logo_xenon.png')
		lb_logo_xenon = Label(self._default, image=img_logo_xenon)
		lb_logo_xenon.image = img_logo_xenon
		lb_logo_xenon.pack()

		Label(self._default, text='Calculadora IPv4', style='Title2.TLabel').pack()

		topics = Frame(self._default)
		topics.pack(pady=20)

		Label(topics, text='Planejar', style='Title3.TLabel').pack(side='left')
		Label(topics, text='Calcular', style='Title3.TLabel').pack(side='left', padx=45)
		Label(topics, text='Testar', style='Title3.TLabel').pack(side='left', padx=(0,45))
		Label(topics, text='Verificar', style='Title3.TLabel').pack(side='left')

	def show_result(self, address, mask, wildcard, network, bcast, firsthost, lasthost, totadd, tothosts, clsip, typeip):
		self._default.pack_forget()
		self._default = Frame(self._right)
		self._default.pack(pady=(30,0))

		Label(self._default, text='Resultado', style='Legend.TLabel').pack(anchor='w', pady=7)

		#
		# grupos
		groups = Frame(self._default)
		groups.pack()

		# grupo lengendas
		group_legend = Frame(groups)
		group_legend.pack(side='left')	

		group1 = Frame(group_legend)
		group1.pack(anchor='w')
		Label(group1, text='Endereço:' ).pack(anchor='w')
		Label(group1, text='Mascara:' ).pack(anchor='w')
		# Label(group1, text='WildCard:' ).pack(anchor='w')

		group2 = Frame(group_legend)
		group2.pack(anchor='w', pady=7)
		Label(group2, text='Rede:' ).pack(anchor='w')
		Label(group2, text='Difusão:' ).pack(anchor='w')
		Label(group2, text='1ro host:' ).pack(anchor='w')
		Label(group2, text='Últ. host:' ).pack(anchor='w')

		group3 = Frame(group_legend)
		group3.pack(anchor='w')
		Label(group3, text='Total de endereços:' ).pack(anchor='w')
		Label(group3, text='Total de hosts:' ).pack(anchor='w')
		Label(group3, text='Classe:' ).pack(anchor='w')

		# grupo resultados
		group_result = Frame(groups)
		group_result.pack(side='left', padx=(45,5))	

		group1 = Frame(group_result)
		group1.pack(anchor='w')
		Label(group1, text=address[0], style='LegendRes.TLabel').pack(anchor='w')
		Label(group1, text=mask[0], style='LegendRes.TLabel').pack(anchor='w')
		# Label(group1, text=wildcard[0], style='LegendRes.TLabel').pack(anchor='w')

		group2 = Frame(group_result)
		group2.pack(anchor='w', pady=7)
		Label(group2, text=network[0], style='LegendRes.TLabel').pack(anchor='w')
		Label(group2, text=bcast[0], style='LegendRes.TLabel').pack(anchor='w')
		Label(group2, text=firsthost[0], style='LegendRes.TLabel').pack(anchor='w')
		Label(group2, text=lasthost[0], style='LegendRes.TLabel').pack(anchor='w')

		group3 = Frame(group_result)
		group3.pack(anchor='w')
		Label(group3, text=totadd[0], style='LegendRes.TLabel').pack(anchor='w')
		Label(group3, text=tothosts[0], style='LegendRes.TLabel').pack(anchor='w')
		Label(group3, text=f'{clsip[0]}, {typeip[0]}', style='LegendRes.TLabel').pack(anchor='w')

		# save txt
		file_data = f'Endereço: {address[0]}\n'
		file_data += f'Mascara: {mask[0]}\n'
		file_data += f'WildCard: {wildcard[0]}\n'
		file_data += '\n'
		file_data += f'Rede: {network[0]}\n'
		file_data += f'Difusão ou broadcast: {bcast[0]}\n'
		file_data += f'1ro host: {firsthost[0]}\n'
		file_data += f'Últ. host: {lasthost[0]}\n'
		file_data += '\n'
		file_data += f'Total de endereços: {totadd[0]}\n'
		file_data += f'Total de hosts: {tothosts[0]}\n'
		file_data += f'Classe IP: {clsip[0]}, {typeip[0]}\n'

		# ver binario
		def on_tosee_bin():
			self._address_prefix.focus_force()
			# other lines

		img_show_bin = PhotoImage(file=r'components/icons/right.png')
		bt_show_bin = Button(groups, command=on_tosee_bin, cursor='hand1', image=img_show_bin, style='Img.TButton')
		bt_show_bin.image = img_show_bin
		bt_show_bin.pack(side='left', anchor='s', padx=(0,31))

		bts = Frame(self._default)
		bts.pack(fill='x', pady=(10,0))

		def on_save():
			self._address_prefix.focus_force()
			file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
			if file != None:
				file.write(file_data.rstrip())

		def on_clean():
			self._address_prefix.focus_force()

			self._default.pack_forget()
			self._state_result = 0
			self.default()

		Button(bts, text='Salvar', command=on_save, cursor='hand1', style='Res.TButton').pack(side='left')
		Button(bts, text='Limpar', command=on_clean, cursor='hand1', style='ResClean.TButton').pack(side='left', padx=10)

	def show_menu(self):
		self._default.pack_forget()
		self._default = Frame(self._right)
		self._default.pack(fill='x')

		menu_bts = Frame(self._default)
		menu_bts.pack(fill='y', padx=100, pady=(80,143))

		def on_docs():
			self._address_prefix.focus_force()
			self.show_docs()

		def on_about():
			self._address_prefix.focus_force()
			self.show_about()

		def on_goback():
			self._address_prefix.focus_force()

		# Button(menu_bts, text='Histórico', cursor='hand1', style='Menu.TButton').pack(pady=(0,5))
		Button(menu_bts, text='Docs', command=on_docs, cursor='hand1', style='Menu.TButton').pack(pady=(0,5))
		Button(menu_bts, text='Sobre', command=on_about, cursor='hand1', style='Menu.TButton').pack(pady=(0,5))
		Button(menu_bts, text='<!>', command=on_goback, cursor='hand1', style='Menu.TButton').pack(pady=(0,5))

	def show_docs(self):
		self._default.pack_forget()
		self._default = Frame(self._right)
		self._default.pack(fill='x')

		doc = ModelDocs()
		tx_doc = Text(self._default, font=('Montserrat', 12), fg='#20bcbb', bg='#375777', highlightthickness=0,
            highlightcolor='#375777', highlightbackground='#375777', relief='flat', padx=5)

		tx_doc.insert('insert', doc.get_doc())

		'''for line in textwrap.wrap(doc.get_doc(), 45):
			tx_doc.insert('insert', line+'\n')'''

		tx_doc['state'] = 'disabled'
		tx_doc.pack()

	def show_about(self):
		self._default.pack_forget()
		self._default = Frame(self._right)
		self._default.pack(fill='x')

		about = ModelDocs()
		tx_about = Text(self._default, font=('Montserrat', 12), fg='#20bcbb', bg='#375777', highlightthickness=0,
            highlightcolor='#375777', highlightbackground='#375777', relief='flat', padx=5)
		tx_about.insert('insert', about.get_about())
		
		'''for line in textwrap.wrap(about.get_about(), 30):
			tx_about.insert('insert', line+'\n')'''

		tx_about['state'] = 'disabled'
		tx_about.pack()

	def show_widgets(self):
		logo = Frame(self._top)
		logo.pack(side='left')

		img_logo = PhotoImage(file=r'components/icons/logo.png')
		lb_logo = Label(logo, image=img_logo)
		lb_logo.image = img_logo
		lb_logo.pack(side='left')

		lb_title = Label(logo, text='Calculadora IPv4', style='Title.TLabel')
		lb_title.pack(side='left', padx=10)

		# botao info
		def on_info():
			self._address_prefix.focus_force()
			self.show_docs()

		img_info = PhotoImage(file=r'components/icons/info.png')
		bt_info = Button(self._top, command=on_info, cursor='hand1', image=img_info, style='Img.TButton')
		bt_info.image = img_info
		bt_info.pack(side='right')

		#
		# esquerda
		self._callback = Frame(self._left)
		self._callback.pack(fill='both')

		img_callb_ipv4 = PhotoImage(file=r'components/icons/ipv4.png')
		self._callb_ipv4 = Label(self._callback, image=img_callb_ipv4)
		self._callb_ipv4.image = img_callb_ipv4
		self._callb_ipv4.pack(pady=20)

		Label(self._left, text='Endereço/Prefixo').pack(anchor='w')
		self._address_prefix = Entry(self._left, font=('Montserrat', 12, 'bold'), justify='center', width=17)
		self._address_prefix.focus_force()
		self._address_prefix.pack(pady=(3,0))
		Label(self._left, text='Exemplo: 192.168.0.1/24', style='Comment.TLabel').pack(anchor='e')

		def on_close_callb():
			self._address_prefix.focus_force()
			error.pack_forget()
			self._callb_ipv4.pack(pady=20)
			self._state_callb = 0

		def on_calculer():
			self._address_prefix.focus_force()
			data = self._address_prefix.get()

			# validacao
			result = {'title': ''}
			if data != '':
				result = self._ctrl.prepar(data)

			if 'Erro' in result['title']: # accao caso retorne errro
				global error
				if self._state_callb == 0:
					self._callb_ipv4.pack_forget()
				else:
					error.pack_forget()

				error = Frame(self._callback, style='Callback.TFrame')
				error.pack(fill='both', pady=(5,10))

				Button(error, text='x', command=on_close_callb, cursor='hand1', style='X.TButton').pack(anchor='e')
				Label(error, text=result['title'], style='CallbTitle.TLabel').pack(pady=(0))
				Label(error, text=result['content'], style='CallbCont.TLabel').pack(pady=(0,13))

				self._state_callb = 1
			elif 'Sucesso' in result['title']: # accao caso caso haja sucesso
				
				# callback default
				if self._state_callb == 1:
					on_close_callb()

				#
				# apresentar os resultados
				result = result['content']

				if self._state_result == 1:
					self._default.pack_forget()

				self.show_result(result[0], result[1], result[2], result[3], result[4], result[5], 
								result[6], result[7], result[8], result[9], result[10],)

				self._state_result = 1

		Button(self._left, text='Calcular', command=on_calculer, cursor='hand1').pack(fill='x', pady=(10, 27))

		img_bar = PhotoImage(file=r'components/icons/color_bar.png')
		lb_bar = Label(self._left, image=img_bar)
		lb_bar.image = img_bar
		lb_bar.pack(pady=(0,70))

		#
		# direita
		top_rigth = Frame(self._right, style='Test.TFrame')
		top_rigth.pack(fill='x', anchor='ne') # , padx=(0,390)

		# botao menu humburg
		def on_menu():
			self._address_prefix.focus_force()

			if self._img_set == 1:
				self._bt_humburg['image'] = self._img_close
				self._img_set = 0
				self.show_menu()
			else:
				self._bt_humburg['image'] = self._img_humburg
				self._img_set = 1
				self.default()

		self._img_set = 1
		self._img_humburg = PhotoImage(file=r'components/icons/humburg.png')
		self._img_close = PhotoImage(file=r'components/icons/x.png')

		self._bt_humburg = Button(top_rigth, command=on_menu, cursor='hand1', 
			image=self._img_humburg, style='Img.TButton')
		self._bt_humburg.image = self._img_humburg
		self._bt_humburg.pack(side='left')

		self._default = Frame(self._right)
		self._default.pack()

		self.default()
		# self.show_result()
		# self.show_menu()
