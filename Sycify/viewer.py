"""
viewer.py: 
    Paquete de vista Sycify App.
"""
from tkinter import Frame, PhotoImage, StringVar
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import ttk
from models import Abmc

class Window:
    def __init__(self, ventana):
        self.ventana = ventana
        # Titles
        self.ventana.title("Sycify")
        self.titulo = Label(self.ventana, text="Canciones", height=2, width=1, bg='#000000', fg='white')
        self.titulo.grid(row=0, column=2, sticky="w" + "e")

        # Properties window tkinter
        self.ventana.geometry('735x400')
        #self.ventana.state('zoomed')
        self.ventana.config(background='#eff5f6')
        icon = PhotoImage(file='Sycify\\images\\logo.png')
        self.ventana.iconphoto(True, icon)

        self.header = Frame(self.ventana, bg='#000000')
        self.header.place(x=0, y=0, width=1070, height=1070)

        # Instances
        instancing=Abmc()

        # Variables
        var_link = StringVar()
        var_name = StringVar()
        var_song = StringVar()
        var_duration = StringVar()
        var_types = StringVar()
        var_visualization = StringVar()
        var_likes = StringVar()

        # Treeview
        link = Label(self.ventana, text="Link", bg='#000000', fg='white')
        link.grid(row=1, column=0, sticky="w")
        link_format=Label(self.ventana, text="(Ex: https://www.youtube.com)", font=("bold", 7), bg='#000000', fg='white')
        link_format.grid(row=1, column=2, sticky="w")
        name = Label(self.ventana, text="Artista", bg='#000000', fg='white')
        name.grid(row=1, column=3, sticky="w")
        name_format=Label(self.ventana, text="(Ex: Fernando)", font=("bold", 7), bg='#000000', fg='white')
        name_format.grid(row=1, column=5, sticky="w")
        song = Label(self.ventana, text="Canción", bg='#000000', fg='white')
        song.grid(row=3, column=0, sticky="w")
        song_format=Label(self.ventana, text="(Ex: La Rave)", font=("bold", 7), bg='#000000', fg='white')
        song_format.grid(row=3, column=2, sticky="w")
        duration = Label(self.ventana, text="Duración", bg='#000000', fg='white')
        duration.grid(row=3, column=3, sticky="w")
        duration_format=Label(self.ventana, text="(Ex: 00:20:32 *hs-mins-seg*)", font=("bold", 7), bg='#000000', fg='white')
        duration_format.grid(row=3, column=5, sticky="w")
        types = Label(self.ventana, text="Estilo Música", bg='#000000', fg='white')
        types.grid(row=5, column=0, sticky="w")
        types_format=Label(self.ventana, text="(Ex: Techno)", font=("bold", 7), bg='#000000', fg='white')
        types_format.grid(row=5, column=2, sticky="w")
        visualization = Label(self.ventana, text="Visualizaciones", bg='#000000', fg='white')
        visualization.grid(row=5, column=3, sticky="w")
        visualization_format=Label(self.ventana, text="(Ex: 20000)", font=("bold", 7), bg='#000000', fg='white')
        visualization_format.grid(row=5, column=5, sticky="w")
        likes = Label(self.ventana, text="Likes", bg='#000000', fg='white')
        likes.grid(row=7, column=0, sticky="w")
        likes_format=Label(self.ventana, text="(Ex: 15000)", font=("bold", 7), bg='#000000', fg='white')
        likes_format.grid(row=7, column=2, sticky="w")
        
        
        entry_link = Entry(self.ventana, textvariable=var_link, width=25)
        entry_link.grid(row=1, column=1, sticky="w")
        entry_name = Entry(self.ventana, textvariable=var_name, width=25)
        entry_name.grid(row=1, column=4, sticky="w")
        entry_song = Entry(self.ventana, textvariable=var_song, width=25)
        entry_song.grid(row=3, column=1, sticky="w")
        entry_duration = Entry(self.ventana, textvariable=var_duration, width=25)
        entry_duration.grid(row=3, column=4, sticky="w")
        entry_types = Entry(self.ventana, textvariable=var_types, width=25)
        entry_types.grid(row=5, column=1, sticky="w")
        entry_visualization = Entry(self.ventana, textvariable=var_visualization, width=25)
        entry_visualization.grid(row=5, column=4, sticky="w")
        entry_likes = Entry(self.ventana, textvariable=var_likes, width=25)
        entry_likes.grid(row=7, column=1, sticky="w")
        
        # Information Loader
        tree = ttk.Treeview(self.ventana)
        tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6", "col7",)

        tree.column("#0", width=30, minwidth=30, anchor="w")
        tree.column("col1", width=100, minwidth=80, anchor="w")
        tree.column("col2", width=100, minwidth=80, anchor="w")
        tree.column("col3", width=70, minwidth=80, anchor="w")
        tree.column("col4", width=40, minwidth=80, anchor="w")
        tree.column("col5", width=130, minwidth=80, anchor="w")
        tree.column("col6", width=80, minwidth=80, anchor="w")
        tree.column("col7", width=120, minwidth=80, anchor="w")

        tree.heading("#0", text="ID")
        tree.heading("col1", text="Link")
        tree.heading("col2", text="Nombre")
        tree.heading("col3", text="Canción")
        tree.heading("col4", text="Duración")
        tree.heading("col5", text="Visualizaciones")
        tree.heading("col6", text="Estilo música")
        tree.heading("col7", text="Likes")
        tree.grid(column=0, row=15, columnspan=100)

        # Buttons
        button = Button(
            self.ventana,
            text="Cargar",
            width=10,
            command=lambda: instancing.load( var_link, var_name, var_song, var_duration, var_types, var_visualization, var_likes, tree, ),
            bg='#FFFFFF', fg='black'
        )
        button.grid(row=10, column=1, sticky="e")
        button_2 = Button(
            self.ventana, text="Eliminar", width=5, command=lambda: instancing.delete(tree),
            bg='#FFFFFF', fg='black'
        )
        button_2.grid(row=10, column=2, sticky="e" + "w")
        button_3 = Button(
            self.ventana,
            text="Consultar",
            width=10,
            command=lambda: instancing.query(tree),
            bg='#FFFFFF', fg='black'
        )
        button_3.grid(row=10, column=3, sticky="e" + "w")
        button_4 = Button(
            self.ventana,
            text="Modificar",
            width=10,
            command=lambda: instancing.modify(var_link, tree),
            bg='#FFFFFF', fg='black'
        )
        button_4.grid(row=10, column=4, sticky="w")
