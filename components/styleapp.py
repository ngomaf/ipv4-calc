from tkinter.ttk import Style

class StyleApp:

	__slots__ = []

	def __init__(self):
		Pfonte = ('Montserrat', 12)
		PLRfonte = ('Montserrat', 11)
		PCfonte = ('Montserrat', 10)
		CTfonte = ('Montserrat', 16)
		Tfonte = ('Orbitron', 12)
		T2fonte = ('Orbitron', 14)
		T3fonte = ('Orbitron', 12)

		style = Style()
		style.theme_use('clam')

		style.configure('TFrame', background='#375777')
		style.configure('Bord.TFrame', padding=15, width=721, height=474)
		style.configure('Base.TFrame', background='#ccc')
		style.configure('Callback.TFrame', background='#e25ca5')
		style.configure('TLabel', font=Pfonte, foreground='#20bcbb', background='#375777')
		style.configure('Title.TLabel', font=Tfonte)
		style.configure('Title2.TLabel', font=T2fonte, foreground='#327c8d')
		style.configure('Title3.TLabel', font=T3fonte, foreground='#5a9ca9')
		style.configure('Comment.TLabel', font=PCfonte, foreground='#7d95ad')
		style.configure('Legend.TLabel', font=PCfonte, foreground='#e25ca5')
		style.configure('LegendRes.TLabel', padding=0, font=Pfonte, foreground='#fff')
		style.configure('CallbTitle.TLabel', padding=0, font=CTfonte, justify='center', foreground='#fff', background='#e25ca5')
		style.configure('CallbCont.TLabel', font=Pfonte, justify='center', foreground='#fff', background='#e25ca5')
		style.configure('TButton', padding=7, font=Pfonte, foreground='#fff', background='#20bcbb', relief='')
		style.configure('Img.TButton', padding=0, background='#375777', relief='')
		style.configure('X.TButton', padding=(10,0), font=Tfonte, width=0, height=0, foreground='#fff', background='#e25ca5', relief='')
		style.configure('Res.TButton', width=8, padding=4)
		style.configure('ResClean.TButton', background='#e25ca5', width=8, padding=4)
		style.configure('Menu.TButton', font=T3fonte, padding=(55,5), foreground='#7d95ad', background='#49698a', relief='')
		style.configure('TSeparator', background='#90ffff')
		style.configure('TEntry', padding=(5,7), background='#375777')

		style.map('TButton',
             foreground=[('pressed', '#e25ca5'), ('active', '#fff')],
             background=[('pressed', '!focus', '#3f8efc'), ('active', '#00cecc')],
             relief=[('pressed', 'flat'), ('!pressed', 'flat')])

		style.map('Img.TButton',
             background=[('pressed', '!focus', '#3f8efc'), ('active', '#375777')],
             relief=[('pressed', 'flat'), ('!pressed', 'flat')])

		style.map('Menu.TButton',
             foreground=[('pressed', '#e25ca5'), ('active', '#bbc1c8')],
             background=[('pressed', '!focus', '#3f8efc'), ('active', '#617d9a')],
             relief=[('pressed', 'flat'), ('!pressed', 'flat')])

		style.map('ResClean.TButton',
             foreground=[('pressed', '#e25ca5'), ('active', '#fff')],
             background=[('pressed', '!focus', '#f3bb30'), ('active', '#e876b4')],
             relief=[('pressed', 'flat'), ('!pressed', 'flat')])

		style.map('X.TButton',
             foreground=[('pressed', '#f3bb30'), ('active', '#fff')],
             background=[('pressed', '!focus', '#3f8efc'), ('active', '#e25ca5')],
             relief=[('pressed', 'flat'), ('!pressed', 'flat')])
