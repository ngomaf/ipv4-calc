from tkinter import Tk, PhotoImage
from tkinter.ttk import Frame

from controllers.ctrlmain import CtrlMain

from components.styleapp import StyleApp


class App:

	__slots__ = ['_root']

	def __init__(self):
		self._root = Tk()

		base = Frame(self._root, style='Base.TFrame')
		base.pack(fill='x', expand=True)

		bord = Frame(base, style='Bord.TFrame')
		bord.pack()

		# 
		# controllers em accao
		CtrlMain(bord, self._root)

		# 
		# estilos
		StyleApp()

	def run(self):
		self._root.title('Calculadora IPV4')
		self._root.geometry('721x474+50+100')
		self._root.minsize(721,474)
		self._root.iconphoto(False, PhotoImage(file='components/icons/logo_ico.png'))
		self._root.configure(bg='#ccc')
		self._root.mainloop()
